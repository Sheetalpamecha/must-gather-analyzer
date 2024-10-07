import unittest
from utils.parser import parse_yaml, gather_files
import os

class TestYAMLParsing(unittest.TestCase):
    def test_parse_valid_yaml(self):
        """
        Test parsing of a valid YAML file.
        """
        yaml_path = 'tests/sample_data/valid_cephcluster.yaml'
        parsed_data = parse_yaml(yaml_path)
        self.assertIsNotNone(parsed_data)
        self.assertEqual(parsed_data['deviceClass'], 'custom')

    def test_parse_invalid_yaml(self):
        """
        Test handling of an invalid YAML file.
        """
        yaml_path = 'tests/sample_data/invalid_cephcluster.yaml'
        parsed_data = parse_yaml(yaml_path)
        self.assertIsNone(parsed_data)

    def test_gather_files(self):
        """
        Test gathering relevant files from directory.
        """
        input_dir = 'tests/sample_data/'
        file_types = ['CephCluster']
        files = gather_files(input_dir, file_types)
        self.assertEqual(len(files), 1)
        self.assertTrue(os.path.basename(files[0]), 'valid_cephcluster.yaml')

if __name__ == '__main__':
    unittest.main()
