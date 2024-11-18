"""
This script analyzes must-gather logs for non-standard configurations 
by comparing them against predefined standards.

It scans specific YAML files from a given directory, 
identifies deviations from the standards, 
and outputs the results on console or in JSON format.
"""

import argparse
import os
import json
from utils.parser import parse_yaml, gather_files
from utils.compare import load_standards, compare_with_standards

def analyze_configs(input_dir, output_file=None):
    """
    Analyzes configuration files in the specified directory 

    Args:
        input_dir (str): Path to the directory containing must-gather logs.
        output_file (str, optional): Path to save the output JSON file with deviations.
                                     If not specified, prints the output to the console.

    Raises:
        FileNotFoundError: If the input directory doesn't exist.
    """
    # Check if the input directory exists
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"The input directory '{input_dir}' does not exist.")

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
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(deviations, f, indent=4)
        print(f"Deviations saved to {output_file}")
    else:
        print(json.dumps(deviations, indent=4))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Analyze must-gather logs for non-standard configurations"
    )
    parser.add_argument(
        '--input', 
        type=str,
        required=True,
        help='Path to the must-gather directory'
    )
    parser.add_argument(
        '--output', 
        type=str,
        help='Path to the output JSON file'
    )
    args = parser.parse_args()
    try:
        analyze_configs(args.input, args.output)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
