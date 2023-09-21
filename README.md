[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml)
# Individual Project#1: Continuous Integration using GitHub Actions of Python Data Science Project
## Youtube link for demo video:

## Purpose:
This project aims to automates data analysis using 'Pandas' and 'matplotlib'. The dataset 'bmi.csv' is from Kaggle (https://www.kaggle.com/datasets/rukenmissonnier/age-weight-height-bmi-analysis), which comprises 741 individual records.)

## This repo contains:
* `.devcontainer`: including a 'Dockerfile' speicifies how the container should be built

* `Github Actions`: contain configuration files (performs all four Makefile commands with badges) for setting up automated build, test and deployment pipelines for the project

* `Dockerfile`: specifies how the container should be built

* `Makefile`:  with tests, format, lint, and installation of dependencies

Run `make lint` which runs `ruff check`

* 'requirement.txt': to specify the dependencies required to run the project

* `desc.ipynb`: a jupyternotebook with 1) cells that perform descriptive statistics using Pandas 2) tested by using nbval plugin for pytest

* `lib.py' and 'test_lib.py': 'lib.py' shares the common code between the script and notebook, and 'test_lib.py' to test library

* `script.py` and 'test_scrip.py': 'script.py' is a python script performing the descriptive statistic tasks using Pandas, and 'test_script' to test script







