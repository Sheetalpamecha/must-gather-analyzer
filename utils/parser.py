import os
import yaml

def parse_yaml(file_path):
    """
    Parse a given YAML file and return the data as a dictionary.
    """
    with open(file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            return data
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {file_path}, Error: {e}")
            return None

def gather_files(input_dir, file_types):
    """
    Traverse the must-gather directory to find relevant files (CRDs/CSVs) to parse.
    """
    relevant_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if any(file_type in file for file_type in file_types):
                relevant_files.append(os.path.join(root, file))
    return relevant_files
