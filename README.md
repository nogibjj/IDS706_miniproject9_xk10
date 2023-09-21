[![Format](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/test.yml)

## Individual Project#1: Continuous Integration using GitHub Actions of Python
### 📺YouTube link for demo video:

### Purpose:
This project aims to automates data analysis using 'Pandas' and 'matplotlib'. The dataset 'bmi.csv' is from Kaggle (https://www.kaggle.com/datasets/rukenmissonnier/age-weight-height-bmi-analysis), which comprises 741 individual records.)

### This repo contains:
* `.devcontainer`: including a 'Dockerfile' speicifies how the container should be built

* `Github Actions`: contain configuration files (performs all four Makefile commands with badges) for setting up automated build, test and deployment pipelines for the project

* `Dockerfile`: specifies how the container should be built

* `Makefile`:  with tests, format, lint, and installation of dependencies
Run 'make test' (test notebook and script and lib):
![Screen Shot 2023-09-21 at 00 16 50](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/0246407e-f70e-4611-b6e4-23c36b5a935b)
testing jupyter notebook by nbval plugin for pytest
![Screen Shot 2023-09-21 at 00 17 42](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/feb2a578-c4a0-456f-8fe6-df09d72f6a79)

Run `make lint` which runs `ruff check`:

![Screen Shot 2023-09-21 at 00 19 40](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/dedf538b-963c-4f53-9cec-0c884e17b57c)

Run 'make format' which formats code with python black:
![Screen Shot 2023-09-21 at 00 21 08](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/136430a1-c602-4048-b0d0-438e3dbb7dfd)

* 'requirement.txt': to specify the dependencies required to run the project (run 'make install')

* `desc.ipynb`: a jupyternotebook with 1) cells that perform descriptive statistics using Pandas 2) tested by using nbval plugin for pytest

* `lib.py' and 'test_lib.py': 'lib.py' shares the common code between the script and notebook, and 'test_lib.py' to test library

* `script.py` and 'test_scrip.py': 'script.py' is a python script performing the descriptive statistic tasks using Pandas, and 'test_script' to test script







