import unittest
import json
import os
from analyze_configs import analyze_configs

class TestAnalyzeConfigs(unittest.TestCase):
    def test_generate_report(self):
        """
        Test end-to-end analysis and JSON report generation.
        """
        input_dir = 'tests/sample_data/'
        output_file = 'tests/sample_data/test_output.json'

        # Run the analysis
        analyze_configs(input_dir, output_file)

        # Check if output file exists and validate the report
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, 'r') as f:
            output_data = json.load(f)
        
        expected_data = {
            "valid_cephcluster.yaml": {
                "deviceClass": {
                    "current_value": "custom",
                    "expected_value": "default"
                }
            }
        }
        self.assertEqual(output_data, expected_data)

        # Clean up
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()