from src.input_parser import parse_input
from src.experience_aggregator import aggregate_experience
from src.markdown_generator import generate_markdown, save_markdown


def main():
    # Step 1: Parse the input data
    data = parse_input('data/experience_data.yaml')

    # Step 2: Aggregate experience
    projects = data['projects']
    experience_dict = aggregate_experience(projects)

    # Step 3: Generate and save alphabetically sorted markdown report
    md_content_alpha = generate_markdown(experience_dict)
    save_markdown(md_content_alpha, 'output/hard_skills.md')

    # Step 4: Generate and save experience-time sorted markdown report
    md_content_time_sorted = generate_markdown(
        experience_dict, sort_by_time=True)
    save_markdown(md_content_time_sorted, 'output/hard_skills_by_time.md')


if __name__ == "__main__":
    main()
