Preparing the environment
-------------------------

First let's get pytest.

Let's get `pipenv` tool. It installs virtual environment and takes care of dependencies, without installing them into your system. Like that you may have multiple versions of some libraries on your pc.

- `pip install pipenv` or `pip3 install pipenv`, depends on python version that you have on system.

Now, we can install any dependencies that we want. Our dependencies for pipenv are stored in `Pipfile`, and "locked" versions are in `Pipfile.lock`.
`Pipfile.lock` is generated file, don't touch it :-).
- `pipenv update --dev`

The command `pipenv update --dev` installed all packages including `[dev-packages]`. Otherwise, we'll not get packages in `[dev-packages]` section.

And finally let's get into our new development environment.

- `pipenv shell`

________________________________________________________

Unittests vs Integrity tests
Unittest library vs pytest library

Step 1.

- Example.

Simple test demonstration. Show how it would look like. Unittest vs pytest tests examples.

Forget unittest library as the history :-).

Tasks:

- Write your first simple test
- Write current date test.

________________________________________________________

Step 2.

Configure your environment, to have right paths.

- What is project root?
- Can we have multiple project roots?
- How to extend `PYTONPATH` and how `sys.path` is involved?
- What is `conftest.py`?

Tasks:

- Fix the `conftest.py`
- Fix the tests

________________________________________________________

Step 3.

Learning the fixtures.

- What is `fixture` in `pytest`?
- Principles behind it.
- Dependency tree, and how it works.
- What types of fixtures we have
- Understanding the fixtures scope
- Fixture autouse

Tasks:

- Fix the tests
- Write your fixture examples.

________________________________________________________

Step 4.

Continue learning fixtures, fixture parametrization, tests parametrization, and magic behind it.
https://docs.pytest.org/en/7.1.x/how-to/mark.html

- `request` fixture and fixture parametrization.
- `@pytest.mark.*` decorators.

Tasks:

- Fix the tests

________________________________________________________

Step 5.

Good practices.

- `with raises`
- commandline tool `-k`, `-k "not "`, `--lf`
- Pytest coverage - how to get html? `pytest --cov-report html --cov=.`
- `pytest --cov-report html --cov=some_evil_code --cov-branch`

________________________________________________________

Step 6. 

Mocking.
https://docs.python.org/3/library/unittest.mock.html

- Mocks, how do they work and what they're used for?
- What is `unittest.mock` library?
- What is `pytest-mock` and how to use `mocker`?
- When do we mock and how to convert integration test into unittest? :-)
- `Mock` vs `monkeypatch`, and how to mock a `datetime.now()`?

Task:

- Force `datetime.now` to return "1970-01-01 00:00"
- Mock the object method
- Mock the object

________________________________________________________

- What the tox is?
- What are pytest plugins?
- TODO: https://github.com/ripexz/python-tkinter-minesweeper test
- What's next? Start programming from writing the tests. Find the project, where you can write the tests.
