from unittest.mock import mock_open, patch
import unittest
from src.input_parser import parse_input
from src.experience_aggregator import aggregate_experience
from src.markdown_manager import generate_markdown, save_markdown


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

        # Update the expected markdown without strict spacing
        expected_md = (
            "### Total Skill Experience:\n\n"
            "| Technology | Experience Time |\n"
            "|------------|-----------------|\n"
            "| FastAPI    | 6 mo |\n"
            "| Flask      | 3 mo |\n"
            "| Python     | 9 mo |\n"
        )

        # Normalize whitespace to focus on content
        self.assertEqual("".join(md_content.split()),
                         "".join(expected_md.split()))

    def test_generate_markdown_alphabetical(self):
        experience_dict = {'Python': 9, 'Flask': 3, 'FastAPI': 6}
        md_content = generate_markdown(experience_dict, sort_by_time=False)

        expected_md = (
            "### Total Skill Experience:\n\n"
            "| Technology | Experience Time |\n"
            "|------------|-----------------|\n"
            "| FastAPI    | 6 mo |\n"
            "| Flask      | 3 mo |\n"
            "| Python     | 9 mo |\n"
        )
        self.assertEqual("".join(md_content.split()),
                         "".join(expected_md.split()))

    def test_generate_markdown_by_time(self):
        experience_dict = {'Python': 9, 'Flask': 3, 'FastAPI': 6}
        md_content = generate_markdown(experience_dict, sort_by_time=True)

        expected_md = (
            "### Total Skill Experience:\n\n"
            "| Technology | Experience Time |\n"
            "|------------|-----------------|\n"
            "| Python     | 9 mo |\n"
            "| FastAPI    | 6 mo |\n"
            "| Flask      | 3 mo |\n"
        )
        self.assertEqual("".join(md_content.split()),
                         "".join(expected_md.split()))

    def test_generate_markdown_empty(self):
        experience_dict = {}
        md_content = generate_markdown(experience_dict)

        expected_md = (
            "### Total Skill Experience:\n\n"
            "| Technology | Experience Time |\n"
            "|------------|-----------------|\n"
        )
        self.assertEqual("".join(md_content.split()),
                         "".join(expected_md.split()))

    def test_save_markdown(self):
        # Mock content and file saving
        mock_md_content = "### Total Skill Experience:\n\n| Technology | Experience Time |\n|------------|-----------------|\n| Python | 9 mo |\n"
        with patch('builtins.open', mock_open()) as mocked_file:
            save_markdown(mock_md_content, 'output/test_skills.md')
            mocked_file.assert_called_once_with(
                'output/test_skills.md', 'w', encoding='utf-8')
            mocked_file().write.assert_called_once_with(mock_md_content)


if __name__ == '__main__':
    unittest.main()
