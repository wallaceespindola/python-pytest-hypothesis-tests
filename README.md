<p align="center">
  <img src="https://github.com/pytest-dev/pytest/raw/main/doc/en/img/pytest_logo_curves.svg" alt="Pytest" width="300"/>
  <img src="https://avatars.githubusercontent.com/u/18481919?s=200&v=4" alt="Hypothesis" width="300"/>
</p>

PYTEST AND HYPOTESIS TESTS AND TUTORIAL FOR PROPERTY-BASED TESTING
=============
[![python 3.10](https://img.shields.io/badge/python-3.10-green.svg)](https://www.python.org/)
[![pytest 8.0.2](https://img.shields.io/badge/pytest-8.0.2-purple.svg)](https://docs.pytest.org/en/latest/)
[![pytest_html 1.19.0](https://img.shields.io/badge/pytest_html-1.19.0-yellowgreen.svg)](https://github.com/pytest-dev/pytest-html)
[![hypothesis 6.98.14](https://img.shields.io/badge/hypothesis-6.98.14-blue.svg)](https://hypothesis.readthedocs.io/en/latest/)
[![xdist 3.5.0](https://img.shields.io/badge/xdist-3.5.0-orange.svg)](https://pypi.org/project/pytest-xdist/)
[![Build Status](https://app.travis-ci.com/wallaceespindola/python-pytest-hypothesis-tests.svg?branch=main)](https://travis-ci.org/wallaceespindola/python-pytest-hypothesis-tests)

Python tests using pytest and hypothesis.
Contains pytest scripts which helps in understanding different pytest functionalities and features.

## Introduction

This project is dedicated to testing and validating various scenarios using property based testing (PBT) in Python. It
showcases different algorithms and their usage, providing a practical insight into property based testing with pytest
and hypothesis.

## Property-based testing (PBT)

Property-based testing (PBT) is a testing technique where you define the general properties your code should satisfy and
then run tests against a wide range of inputs to ensure the properties hold. In Python, Hypothesis is a popular library
for
PBT. Below are varied code examples demonstrating the use of PBT, ranging from basic to advanced scenarios.

## Pytest

The [pytest](https://docs.pytest.org/en/latest/) framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

An example of a simple test:

```python
def increase(x):
    return x + 1


def test_increase():
    assert increase(3) == 4
```

How to run the project?
=====

1. Clone and open this repo:

```bash
git clone git@github.com:wallaceespindola/python-pytest-hypothesis-tests.git

cd python-pytest-hypothesis-tests
```

2. Create and activate your python virtual environment:

```shell
python3.10 -m virtualenv .venv

source .venv/bin/activate
```

3. Install all the dependencies using:

```shell
pip install -r requirements.txt
```

4. Tests are located inside `src/tests/`

```shell
pytest src/tests
```

![pytest_execution_1](img%2Fpytest_execution_1.png)

![pytest_execution_2](img%2Fpytest_execution_2.png)

![pytest_execution_3](img%2Fpytest_execution_3.png)

5. To run tests and generate html report

```shell
pytest src/tests --html=report.html --self-contained-html
```

![html report](img/report_html.png)

6. To run tests with code coverage report

```shell
pytest --cov=src --verbose
```

![coverage_report](img/cov_report.png)

7. To run tests with multiple cpu cycles(will speed up the test execution by running them in parallel)

```shell
pytest src/tests -n 5
```

![pytest_exec_parallel_1](img%2Fpytest_exec_parallel_1.png)

![pytest_exec_parallel_2](img%2Fpytest_exec_parallel_2.png)

8. To fix linting errors the project uses [autopep8](https://github.com/hhatto/autopep8).
   To modify a file in place (with aggressive level 2):

```shell
$ autopep8 --in-place --aggressive --aggressive <filename>
```

## Hypothesis shrinking

> Hypothesis shrinking is a process that occurs after a test failure is detected. When Hypothesis finds an example that
causes your test to fail, it doesn't stop there. Instead, it tries to simplify or "shrink" the example to the smallest
or simplest form that still causes the test to fail. This feature is incredibly useful because it often uncovers the
minimal scenario that triggers the bug, making it easier to understand and fix.

Here's a detailed breakdown of how shrinking works in Hypothesis:

Initial Failure Discovery: First, Hypothesis generates various random inputs based on the strategies you've defined to
test your code until it finds a set of inputs that causes a test to fail.

Shrinking Process: Once a failure is found, Hypothesis enters the shrinking phase. It tries to reduce the complexity of
the failing input while still keeping the test in a failing state. This is done iteratively, attempting many smaller
variations of the original failing input and checking if they still produce the failure.

Minimal Failure Example: The process continues until Hypothesis cannot simplify the example any further without the test
passing. The result is a "minimal" example that demonstrates the failure. This example is minimal in the sense that
changing any single element of the input (reducing a number, shortening a string, etc.) would cause the test not to
fail.

Benefits: The primary benefit of shrinking is that it often points directly to the root cause of the issue. For
instance, if your function fails with a list of 100 integers, shrinking might reveal that it actually fails with just a
single specific integer. This makes bugs much easier to diagnose and fix, especially when dealing with complex inputs.

Consistency: The shrinking process in Hypothesis is deterministic. Given the same initial failure, Hypothesis will
always shrink to the same minimal example. This consistency is helpful for debugging and ensures that the minimal
example is not dependent on random chance.

Customization: While the default shrinking behavior is usually sufficient, Hypothesis allows you to customize aspects of
the process for advanced scenarios. However, in many cases, the out-of-the-box shrinking provides significant value
without any need for customization.

To illustrate, if you have a test that fails for a list of integers [10, 0, -5, 30, 20] that causes a division by zero
in your function, Hypothesis might shrink this list down to just [0] if the zero alone is enough to trigger the bug,
clearly pointing out that the issue arises from division by zero, not the other values in the array.

## References

* An introduction to property based
  testing: https://medium.com/criteo-engineering/introduction-to-property-based-testing-f5236229d237
* Hypothesis, PBT for Python: https://hypothesis.readthedocs.io/en/latest/
* A PBT article focused on
  python: https://www.freecodecamp.org/news/intro-to-property-based-testing-in-python-6321e0c2f8b/
* Property testing definition: https://en.wikipedia.org/wiki/Property_testing
* Another python lib for PBT called testing/quick: https://www.mayhem.security/blog/what-is-property-based-testing
* What is PBT, another point of view: https://hypothesis.works/articles/what-is-property-based-testing/

## Author

* Wallace Espindola, Sr. Software Engineer & Architect / Java & Python Dev
* E-mail: wallace.espindola@gmail.com
* LinkedIn: https://www.linkedin.com/in/wallaceespindola/
* Website: https://wtechitsolutions.com/
* Gravatar: https://gravatar.com/wallacese

## License

* This project is released under the Apache 2.0 License. For more details, see [LICENSE](LICENSE).
* Copyright © 2024 [Wallace Espindola](https://github.com/wallaceespindola/).