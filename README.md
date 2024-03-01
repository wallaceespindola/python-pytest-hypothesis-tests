<p align="center">
  <img src="https://github.com/pytest-dev/pytest/raw/main/doc/en/img/pytest_logo_curves.svg" alt="Pytest" width="300"/>
  <img src="https://avatars.githubusercontent.com/u/18481919?s=200&v=4" alt="Hypothesis" width="300"/>
</p>

PYTEST AND HYPOTESIS TESTS AND TUTORIAL
=============
[![python 3.10](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://www.python.org/)
[![pytest 8.0.2](https://img.shields.io/badge/pytest-8.0.2-green.svg)](https://docs.pytest.org/en/latest/)
[![allure_pytest 2.13.2](https://img.shields.io/badge/allure_pytest-2.13.2-yellow.svg)](https://github.com/allure-framework/allure-python)
[![pytest_html 1.19.0](https://img.shields.io/badge/pytest_html-1.19.0-yellowgreen.svg)](https://github.com/pytest-dev/pytest-html)
[![hypothesis 6.98.14](https://img.shields.io/badge/hypothesis-6.98.14-blue.svg)](https://hypothesis.readthedocs.io/en/latest/)
[![xdist 3.5.0](https://img.shields.io/badge/xdist-3.5.0-orange.svg)](https://pypi.org/project/pytest-xdist/)
[![Build Status](https://app.travis-ci.com/wallaceespindola/python-pytest-hypothesis-tests.svg?branch=main)](https://travis-ci.org/wallaceespindola/python-pytest-hypothesis-tests)
[![Coverage Status](https://coveralls.io/repos/github/wallaceespindola/python-pytest-hypothesis-tests/badge.svg?branch=main)](https://coveralls.io/github/wallaceespindola/python-pytest-hypothesis-tests?branch=main)

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

Hypothesis shrinking
=====

Hypothesis shrinking is a process that occurs after a test failure is detected. When Hypothesis finds an example that causes your test to fail, it doesn't stop there. Instead, it tries to simplify or "shrink" the example to the smallest or simplest form that still causes the test to fail. This feature is incredibly useful because it often uncovers the minimal scenario that triggers the bug, making it easier to understand and fix.

Here's a detailed breakdown of how shrinking works in Hypothesis:

Initial Failure Discovery: First, Hypothesis generates various random inputs based on the strategies you've defined to test your code until it finds a set of inputs that causes a test to fail.

Shrinking Process: Once a failure is found, Hypothesis enters the shrinking phase. It tries to reduce the complexity of the failing input while still keeping the test in a failing state. This is done iteratively, attempting many smaller variations of the original failing input and checking if they still produce the failure.

Minimal Failure Example: The process continues until Hypothesis cannot simplify the example any further without the test passing. The result is a "minimal" example that demonstrates the failure. This example is minimal in the sense that changing any single element of the input (reducing a number, shortening a string, etc.) would cause the test not to fail.

Benefits: The primary benefit of shrinking is that it often points directly to the root cause of the issue. For instance, if your function fails with a list of 100 integers, shrinking might reveal that it actually fails with just a single specific integer. This makes bugs much easier to diagnose and fix, especially when dealing with complex inputs.

Consistency: The shrinking process in Hypothesis is deterministic. Given the same initial failure, Hypothesis will always shrink to the same minimal example. This consistency is helpful for debugging and ensures that the minimal example is not dependent on random chance.

Customization: While the default shrinking behavior is usually sufficient, Hypothesis allows you to customize aspects of the process for advanced scenarios. However, in many cases, the out-of-the-box shrinking provides significant value without any need for customization.

To illustrate, if you have a test that fails for a list of integers [10, 0, -5, 30, 20] that causes a division by zero in your function, Hypothesis might shrink this list down to just [0] if the zero alone is enough to trigger the bug, clearly pointing out that the issue arises from division by zero, not the other values in the array.
