# SkillChrono

**SkillChrono** is a Python-based tool designed to help developers organize and visualize their technical skills across various projects. It processes structured data, aggregates experience per technology, and generates markdown reports sorted both alphabetically and by experience duration.

## Features

- Aggregates technical experience across multiple projects.
- Generates two markdown reports:
  1. **Alphabetically Sorted Report** (`hard_skills.md`).
  2. **Experience-Time Sorted Report** (`hard_skills_by_time.md`).
- Converts months of experience into "Y yr M mo" format.

## Installation

To install the project, first clone the repository and install the dependencies:

```bash
git clone <repository-url>
cd SkillChrono
pip install -r requirements.txt
```

## Usage

To generate the markdown reports, run the main script:

```bash
python main.py
```

This will generate two reports under the `output/` directory:

- `hard_skills.md`: Technologies sorted alphabetically.
- `hard_skills_by_time.md`: Technologies sorted by experience duration.

### Input Structure

The tool reads data from a structured YAML file (`data/experience_data.yaml`). Here's a sample structure:

```yaml
jobs:
  - job_title: 'Full Stack Developer @ Company XYZ'
    duration: 'Jan 2020 – Dec 2021'
    projects:
      - name: 'Project A'
        duration: 12
        technologies:
          Python: 12
          Django: 12
```

### Output Example

#### Alphabetically Sorted:

```
| Technology | Experience Time |
|------------|-----------------|
| Python     | 1 yr 2 mo       |
| Django     | 1 yr 2 mo       |
```

#### Experience-Time Sorted:

```
| Technology | Experience Time |
|------------|-----------------|
| Python     | 1 yr 2 mo       |
| Django     | 1 yr 2 mo       |
```

## Contributing

If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License.
