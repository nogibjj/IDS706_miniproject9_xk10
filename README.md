[![Format](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_individualproject1_xk10/actions/workflows/test.yml)

## Individual Project#1: Continuous Integration using GitHub Actions of Python
### 📺YouTube link for demo video:
https://youtu.be/xEIdOFCpTH8

### Purpose:
This project aims to automates data analysis using 'Pandas', including reading a dataset , obtaining its summary statistics and visualization, and realizing continuous integration using Github Actions. The dataset 'bmi.csv' is from Kaggle (https://www.kaggle.com/datasets/rukenmissonnier/age-weight-height-bmi-analysis), which comprises 741 individual records).

### This repo contains:
* `.devcontainer`: including a 'Dockerfile' specifies how the container should be built

* `Github Actions`: contain configuration files (performs all four Makefile commands with badges) for setting up automated build, test and deployment pipelines for the project

* `Dockerfile`: specifies how the container should be built

* `Makefile`:  with tests, format, lint, and installation of dependencies
Run `make test` (test notebook and script and lib):
![Screen Shot 2023-09-21 at 00 16 50](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/0246407e-f70e-4611-b6e4-23c36b5a935b)

Testing jupyter notebook by nbval plugin for pytest
![Screen Shot 2023-09-21 at 00 17 42](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/feb2a578-c4a0-456f-8fe6-df09d72f6a79)

Run `make lint` which runs `ruff check`:
![Screen Shot 2023-09-21 at 00 19 40](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/dedf538b-963c-4f53-9cec-0c884e17b57c)

Run `make format` which formats code with python black:
![Screen Shot 2023-09-21 at 00 21 08](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/136430a1-c602-4048-b0d0-438e3dbb7dfd)

* `requirement.txt`: to specify the dependencies required to run the project (run 'make install')

* `desc.ipynb`: a jupyternotebook with 1) cells that perform descriptive statistics using Pandas 2) tested by using nbval plugin for pytest

* `lib.py` and `test_lib.py`: 'lib.py' shares the common code between the script and notebook, and 'test_lib.py' to test library

* `script.py` and `test_scrip.py`: 'script.py' is a python script performing the descriptive statistic tasks using Pandas, and 'test_script' to test script

### Summary statistics:
The dataset contains 741 records with the following key statistics: Age: Average age is 31.6 years, ranging from 15 to 61 years. Height: Average height is 1.709 meters, ranging from 1.46 to 2.07 meters. Weight: Average weight is 78.4 kilograms, ranging from 25.9 to 270 kilograms. BMI: Average BMI is 26.4, ranging from 12.15 to 66.30. These statistics summarize the dataset's age, height, weight, and BMI attributes.
![image](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/71b0fb5f-b532-4a38-bf91-632215227b80)

### Data visualizations:
For this project, I created a histogram for age distribution.
![age_histogram](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/46310d94-e459-41ca-9e7c-4fdf13c3099a)

Also a scatterplot of Age vs Bmi
![agebmi_scatterplot](https://github.com/nogibjj/IDS706_individualproject1_xk10/assets/143849077/9aae0e92-2ed4-4af8-85d9-f37cc4c9e142)






