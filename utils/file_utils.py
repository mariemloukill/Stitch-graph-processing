def verify_edgelist(file_name):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 2 or not all(part.isdigit() for part in parts):
                    return False
        return True
    except:
        return False
