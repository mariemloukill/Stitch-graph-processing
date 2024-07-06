import joblib
import pandas as pd
import numpy as np
import networkx as nx

# Load the saved model, scaler, label encoder, and necessary data
knn = joblib.load('ml/knn_model.pkl')
scaler = joblib.load('ml/scaler.pkl')
label_encoder_workload = joblib.load('ml/label_encoder_workload.pkl')
y_train = joblib.load('data/y_train.pkl')
execution_time_train = joblib.load('data/execution_time_train.pkl')

# Define system capabilities
system_capabilities = {
    'Ligra': 1,  # in-memory
    'GPOP': 1,   # in-memory
    'Mmap': 1.5, # optimized in-memory
    'GraphChi': 3, # out-of-core
    'GridGraph': 2 # hybrid
}

# Function to predict the best graph processing system
def predict_best_system(workload, edges, nodes, size, alpha=0.35, beta=0.65):
    workload_encoded = label_encoder_workload.transform([workload])[0]
    input_data = pd.DataFrame({
        'Workload': [workload_encoded],
        'Edges': [edges],
        'Nodes': [nodes],
        'Size': [size]
    })
    scaled_data = scaler.transform(input_data)

    distances, indices = knn.kneighbors(scaled_data)
    predicted_systems = []
    for i, (dist, idx) in enumerate(zip(distances, indices)):
        closest_execution_times = execution_time_train.iloc[idx].values
        closest_systems = y_train.iloc[idx].values

        # Count the number of neighbors for each system
        system_counts = pd.Series(closest_systems).value_counts()

        # Calculate weighted scores
        system_scores = {}
        for system in system_counts.index:
            system_execution_times = closest_execution_times[closest_systems == system]
            avg_execution_time_log = np.mean(np.log(system_execution_times + 1))  # Logarithmic scale
            count_of_neighbors = system_counts[system]
            capability_adjustment = system_capabilities[system]
            system_scores[system] = (alpha * avg_execution_time_log) + (beta * (1/count_of_neighbors))

        best_system = min(system_scores, key=system_scores.get)
        predicted_systems.append(best_system)
    
    return predicted_systems[0]

def extract_graph_features(file_path):
    # Load the graph using NetworkX
    G = nx.read_edgelist(file_path)
    
    # Extract features
    num_edges = G.number_of_edges()
    num_nodes = G.number_of_nodes()
    
    # Estimate size in GB (simplified for example purposes)
    size_gb = (num_edges * 2 * 8) / (1024 ** 3)  # assuming each edge is 16 bytes
    
    return num_edges, num_nodes, size_gb
