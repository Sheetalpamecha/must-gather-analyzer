"""
Utilities for loading standards and comparing YAML data against them.
"""

import json

def load_standards(standards_file):
    """
    Load the predefined standard configurations.
    """
    with open(standards_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def compare_with_standards(data, standards):
    """
    Compare the data from YAML with predefined standards.
    """
    deviations = {}
    for key, standard_value in standards.items():
        if key in data and data[key] != standard_value:
            deviations[key] = {
                "current_value": data[key],
                "expected_value": standard_value
            }
    return deviations
