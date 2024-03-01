PYTEST AND HYPOTESIS TESTS AND TUTORIAL
=============
[![python 3.10](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://www.python.org/)
[![pytest 8.0.2](https://img.shields.io/badge/pytest-8.0.2-green.svg)](https://docs.pytest.org/en/latest/)
[![allure_pytest 2.13.2](https://img.shields.io/badge/allure_pytest-2.13.2-yellow.svg)](https://github.com/allure-framework/allure-python)
[![pytest_html 1.19.0](https://img.shields.io/badge/pytest_html-1.19.0-yellowgreen.svg)](https://github.com/pytest-dev/pytest-html)
[![hypothesis 6.98.14](https://img.shields.io/badge/hypothesis-6.98.14-blue.svg)](https://hypothesis.readthedocs.io/en/latest/)
[![xdist 3.5.0](https://img.shields.io/badge/xdist-3.5.0-orange.svg)](https://pypi.org/project/pytest-xdist/)
[![Build Status](https://travis-ci.org/wallaceespindola/python-pytest-hypothesis-tests.svg?branch=master)](https://travis-ci.org/wallaceespindola/python-pytest-hypothesis-tests)
[![Coverage Status](https://coveralls.io/repos/github/wallaceespindola/python-pytest-hypothesis-tests/badge.svg?branch=master)](https://coveralls.io/github/wallaceespindola/python-pytest-hypothesis-tests?branch=main)

[//]: # ([![Updates]&#40;https://pyup.io/repos/github/wallaceespindola/python-pytest-hypothesis-tests/shield.svg&#41;]&#40;https://pyup.io/repos/github/wallaceespindola/python-pytest-hypothesis-tests/&#41;)

[//]: # ([![Python 3]&#40;https://pyup.io/repos/github/wallaceespindola/python-pytest-hypothesis-tests/python-3-shield.svg&#41;]&#40;https://pyup.io/repos/github/wallaceespindola/python-pytest-hypothesis-tests/&#41;)

Python tests using pytest and hypothesis.
Contains pytest scripts which helps in understanding different pytest functionalities and features.

The [pytest](https://docs.pytest.org/en/latest/) framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

An example of a simple test:

```python
# content of test_sample.py
def inc(x):
    return x + 1


# make sure the test function's name starts with 'test_' to be a unit-test
def test_answer():
    assert inc(3) == 5
```

How to Run the project?
=====

1. Clone/download this repo

2. Install all the dependencies using-

```shell
pip install -r requirements.txt
```

3. Tests are located inside `src/tests/`

```shell
pytest src/tests
```

4. To run tests and generate html report

```shell
pytest src/tests --html=report.html --self-contained-html
```

![alt text](img/report_html.png)

5. To run tests and generate allure report

```shell
#make sure report directory exists in the root folder
pytest src/tests --alluredir=report/

#To view the allure report
allure serve report/
```

![alt text](img/report_allure.png)

6. To run tests with code coverage report

```shell
pytest --cov=src --verbose
```

![alt text](img/cov_report.png)

7. To run tests with multiple cpu cycles(will speed up the test execution by running them in parallel)

```shell
pytest src/tests -n 5
```

8. To fix linting errors the project uses [autopep8](https://github.com/hhatto/autopep8).
   To modify a file in place (with aggressive level 2):

```shell
$ autopep8 --in-place --aggressive --aggressive <filename>
```