import yaml


def parse_input(file_path):
    """
    Parses the YAML input file and returns the project data.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Dictionary containing a list of all projects with their respective technologies and durations.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)  # Parse the single YAML document

    all_projects = []

    # Check if the YAML data has a 'jobs' key and iterate through it
    if 'jobs' in data:
        for job_entry in data['jobs']:
            if 'projects' in job_entry:
                all_projects.extend(job_entry['projects'])

    # Debugging: Print collected projects
    # print("Collected projects:", all_projects)

    return {'projects': all_projects}
