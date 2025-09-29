# sandbox_py

A standardized project structure for **data science**, **analytics**, and **multi-language workflows** using Python and R. This repository is designed for reproducibility, scalability, and collaboration, following industry-standard conventions.

[![License](https://img.shields.io/badge/License-Private-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.0%2B-blue)](https://www.r-project.org/)

## 📖 Overview

This template provides a robust, reproducible framework for data science projects, supporting both Python and R workflows. It includes a well-organized directory structure, dependency management, and guidelines for version control to streamline collaboration and deployment.

## 📂 Project Structure

```
analytics-template/
│
├── .venv/                 # Python virtual environment (excluded from Git)
├── data/                  # Raw and processed datasets
│   ├── raw/               # Original, immutable data sources
│   └── processed/         # Cleaned and transformed datasets
│
├── notebooks/             # Jupyter Notebooks and R Markdown files
│   ├── exploratory/       # Initial data exploration and EDA
│   └── reports/           # Polished notebooks for presentation
│
├── scripts/               # Standalone Python or R scripts
│   ├── data_processing/   # ETL and data wrangling scripts
│   ├── analysis/          # Statistical analysis and modeling
│   └── utils/             # Helper functions and utilities
│
├── tests/                 # Unit tests for project code
│
├── renv/                  # R dependency management (renv)
├── requirements.txt        # Python dependencies
├── renv.lock              # R package lock file
├── README.md              # Project documentation
├── LICENSE                # License file (private repository)
└── .gitignore             # Git ignore rules
```

## 🛠️ Prerequisites

- **Python**: 3.8 or higher
- **R**: 4.0 or higher
- **Jupyter**: For running notebooks with Python and R kernels
- **Git**: For version control
- **Optional**: Docker for containerized environments

## 🔧 Environment Setup

### Python

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   # macOS/Linux
   source .venv/bin/activate
   # Windows
   .venv\Scripts\activate
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### R

1. Install `renv` if not already installed:
   ```r
   install.packages("renv")
   ```

2. Activate and restore the R environment:
   ```r
   renv::activate()
   renv::restore()
   ```

### Jupyter Notebooks with Multi-Language Support

This project supports multi-kernel Jupyter Notebooks for Python and R:

- **Python kernel**: Install `ipykernel`:
  ```bash
  pip install ipykernel
  python -m ipykernel install --user --name=analytics-template
  ```

- **R kernel**: Install `IRkernel`:
  ```r
  install.packages("IRkernel")
  IRkernel::installspec(user = TRUE)
  ```

Switch between Python and R kernels in Jupyter Notebook via the interface.

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd analytics-template
   ```

2. Set up the Python environment (see above).
3. Set up the R environment (see above).
4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

5. Start exploring data in `notebooks/exploratory/` or run scripts in `scripts/`.

## 📜 Version Control

Adhere to the [Conventional Commits](https://www.conventionalcommits.org/) specification for clear and consistent commit messages:

- `feat`: New feature
- `fix`: Bug fix
- `chore`: Maintenance tasks
- `docs`: Documentation updates

Example:
```bash
git add .
git commit -m "feat: add data cleaning script for sales data"
git push
```

## 🧪 Testing

Unit tests are located in the `tests/` directory. Run tests to ensure code reliability:

- For Python:
  ```bash
  pytest tests/
  ```

- For R:
  ```r
  library(testthat)
  test_dir("tests/")
  ```

## 📄 License

This is a private repository intended for internal development. Licensing terms apply to authorized collaborators only. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or contributions, reach out to:

- **Name**: Miguel Calvo Morrison
- **Email**: mcalvomorrison@gmail.com

## 🙏 Acknowledgments

This template is inspired by best practices from the data science community, including [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) and [R for Data Science](https://r4ds.had.co.nz/).
