import argparse
import os
import json
from utils.parser import parse_yaml, gather_files
from utils.compare import load_standards, compare_with_standards

def analyze_configs(input_dir, output_file=None):
    # Define file types to gather (CephCluster, StorageCluster, CSVs)
    file_types = ['CephCluster', 'StorageCluster', 'ClusterServiceVersion']
    
    # Find relevant files
    yaml_files = gather_files(input_dir, file_types)
    
    # Load the standards
    standards = load_standards('config/standards.json')

    deviations = {}
    # Parse and compare each relevant file
    for yaml_file in yaml_files:
        data = parse_yaml(yaml_file)
        if data:
            deviation = compare_with_standards(data, standards)
            if deviation:
                deviations[os.path.basename(yaml_file)] = deviation

    # Output results
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(deviations, f, indent=4)
        print(f"Deviations saved to {output_file}")
    else:
        print(json.dumps(deviations, indent=4))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Analyze must-gather logs for non-standard configurations")
    parser.add_argument('--input', type=str, required=True, help='Path to the must-gather directory')
    parser.add_argument('--output', type=str, help='Path to the output JSON file')
    args = parser.parse_args()

    analyze_configs(args.input, args.output)