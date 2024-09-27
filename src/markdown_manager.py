def generate_markdown(experience_dict, sort_by_time=False):
    md_content = "### Total Skill Experience:\n\n"
    
    # Table header
    md_content += "| Technology | Experience Time |\n"
    md_content += "|------------|-----------------|\n"

    # Helper function to convert months to "Y yr m mo" format
    def format_duration(months):
        years = months // 12
        remaining_months = months % 12
        result = ""
        if years > 0:
            result += f"{years} yr "
        if remaining_months > 0 or years == 0:
            result += f"{remaining_months} mo" if remaining_months > 0 else f"{months} mo"
        return result.strip()

    # Sort the technologies based on the chosen method (alphabetically or by time)
    sorted_items = sorted(experience_dict.items(), key=lambda item: item[1], reverse=True) if sort_by_time else sorted(experience_dict.items())

    # Format the markdown content into a table
    for tech, months in sorted_items:
        md_content += f"| {tech} | {format_duration(months)} |\n"

    return md_content



def save_markdown(md_content, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
