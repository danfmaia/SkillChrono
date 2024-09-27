from unittest.mock import mock_open, patch
import unittest
from src.input_parser import parse_input
from src.experience_aggregator import aggregate_experience
from src.markdown_generator import generate_markdown


class TestExperienceAggregator(unittest.TestCase):

    def test_parse_input(self):
        mock_yaml_content = '''
        jobs:
          - job_title: 'Junior Full Stack Developer @ Radix Engineering & Software'
            duration: 'May 2019 – Oct 2020'
            projects:
              - name: 'Development Project for US-based Oil and Gas Company'
                duration: 9
                technologies:
                  C#: 9
                  .NET: 9
                  Angular: 5
        '''

        with patch('builtins.open', mock_open(read_data=mock_yaml_content)):
            data = parse_input('data/experience_data.yaml')
            self.assertIsInstance(data, dict)
            self.assertIn('projects', data)
            self.assertGreater(len(data['projects']), 0)

    def test_aggregate_experience(self):
        projects = [
            {'name': 'Project 1', 'technologies': {'Python': 5, 'Flask': 3}},
            {'name': 'Project 2', 'technologies': {'Python': 4, 'FastAPI': 6}}
        ]
        result = aggregate_experience(projects)
        expected = {'Python': 9, 'Flask': 3, 'FastAPI': 6}
        self.assertEqual(result, expected)

    def test_aggregate_experience_with_omitted_durations(self):
        projects = [
            {
                'name': 'CodeQuery API Development',
                'duration': 4,  # Use project duration for some techs
                'technologies': {
                    'Python': None,  # Omitted, should use project duration
                    'Flask': 2,      # Explicit duration
                    'FastAPI': 3,    # Explicit duration
                    'GenAI': None    # Omitted, should use project duration
                }
            }
        ]
        result = aggregate_experience(projects)
        expected = {'Python': 4, 'Flask': 2, 'FastAPI': 3, 'GenAI': 4}
        self.assertEqual(result, expected)

    def test_aggregate_experience_across_projects(self):
        projects = [
            {
                'name': 'Project 1',
                'duration': 5,  # Use project duration for some techs
                'technologies': {
                    'Python': 5,
                    'Flask': 3
                }
            },
            {
                'name': 'Project 2',
                'duration': 4,  # Use project duration for some techs
                'technologies': {
                    'Python': 4,
                    'FastAPI': 6
                }
            },
            {
                'name': 'CodeQuery API Development',
                'duration': 4,  # Use project duration for omitted techs
                'technologies': {
                    'Python': None,  # Omitted, should use project duration
                    'Flask': 2,      # Explicit duration
                    'FastAPI': 3,    # Explicit duration
                    'GenAI': None    # Omitted, should use project duration
                }
            }
        ]
        result = aggregate_experience(projects)
        expected = {'Python': 13, 'Flask': 5, 'FastAPI': 9, 'GenAI': 4}
        self.assertEqual(result, expected)

    def test_generate_markdown(self):
        experience_dict = {'Python': 9, 'Flask': 3, 'FastAPI': 6}
        md_content = generate_markdown(experience_dict)
        expected_md = "### Total Skill Experience:\n\n- **FastAPI**: 6 mo\n- **Flask**: 3 mo\n- **Python**: 9 mo\n"
        self.assertEqual(md_content, expected_md)


if __name__ == '__main__':
    unittest.main()
