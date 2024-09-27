def aggregate_experience(projects):
    experience_dict = {}

    for project in projects:
        if 'duration' in project:
            project_duration = project['duration']
        else:
            project_duration = 0  # Default if neither duration nor dates provided

        for tech, months in project['technologies'].items():
            # If the duration is omitted, use the project's duration
            if months is None:
                experience_time = project_duration
            elif isinstance(months, int):  # Direct numeric duration
                experience_time = months
            else:
                experience_time = project_duration

            # Accumulate the experience across projects for the same technology
            if tech in experience_dict:
                experience_dict[tech] += experience_time
            else:
                experience_dict[tech] = experience_time

    return experience_dict
