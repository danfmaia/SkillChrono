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

The tool reads data from a structured YAML file (`data/experience_data.yaml`). Each job can have multiple projects, and each project can list several technologies with an optional duration in months. If the experience time for a technology is omitted, it defaults to the project's duration.

Here’s a sample structure:

```yaml
jobs:
  - job_title: 'Full Stack Developer @ Company XYZ'
    duration: 'Jan 2020 – Dec 2021'
    projects:
      - name: 'E-commerce Platform Development'
        duration: 12
        technologies:
          Python:
          Django:
          PostgreSQL:
          Docker: 8 # Technology-specific duration
      - name: 'Internal Tooling Project'
        duration: 6
        technologies:
          React:
          Node.js:
          Jenkins:
          Kubernetes: 4 # Technology-specific duration

  - job_title: 'Senior Developer @ ABC Corp'
    duration: 'Jan 2022 – Present'
    projects:
      - name: 'Cloud Infrastructure Migration'
        duration: 10
        technologies:
          AWS:
          Terraform:
          Docker:
      - name: 'Microservices API Development'
        duration: 8
        technologies:
          FastAPI:
          Python:
          Kafka:
          Redis: 5 # Technology-specific duration
```

### Output Example

#### Alphabetically Sorted:

```
| Technology | Experience Time |
|------------|-----------------|
| AWS        | 10 mo           |
| Docker     | 1 yr 6 mo       |
| Django     | 1 yr            |
| FastAPI    | 8 mo            |
| Kafka      | 8 mo            |
| Kubernetes | 4 mo            |
| Node.js    | 6 mo            |
| PostgreSQL | 1 yr            |
| Python     | 1 yr 8 mo       |
| React      | 6 mo            |
| Redis      | 5 mo            |
| Terraform  | 10 mo           |
```

#### Experience-Time Sorted:

```
| Technology | Experience Time |
|------------|-----------------|
| Python     | 1 yr 8 mo       |
| Docker     | 1 yr 6 mo       |
| Django     | 1 yr            |
| PostgreSQL | 1 yr            |
| AWS        | 10 mo           |
| Terraform  | 10 mo           |
| FastAPI    | 8 mo            |
| Kafka      | 8 mo            |
| React      | 6 mo            |
| Node.js    | 6 mo            |
| Redis      | 5 mo            |
| Kubernetes | 4 mo            |
```

## Development Approach

SkillChrono was developed using a **Test-Driven Development (TDD)** approach to ensure code reliability and functionality. Additionally, the project was built with the assistance of AI tools such as **CodeQueryGPT** and **CodeQueryAPI**.

- **CodeQueryGPT**: An AI assistant that contributed significantly to the development of this project. CodeQueryGPT assisted in feature development, testing, debugging, and helped streamline the documentation process. It provided real-time code analysis, suggestions for refactoring, and helped ensure that good coding practices were maintained throughout the project.

- **CodeQueryAPI**: A Python API for querying project structures and content in real-time. You can explore the **CodeQueryAPI** repository [here](https://github.com/danfmaia/CodeQuery-API).

## Contributing

If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License.
