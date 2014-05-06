import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    '''
    from: http://pytest.org/latest/goodpractises.html#integration-with-setuptools-test-commands
    '''

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="Evolutionary Rubik Solver",
    version="0.1",
    packages=find_packages(),

    install_requires=[],

    tests_require=['pytest'],
    cmdclass={'test': PyTest},

    # metadata for upload to PyPI
    author='Jan Stypka, Wojciech Krzystek',
    author_email='see committer emails :-)',
    description="This is an Example Package",
    # TODO(vucalur): License
    license='BSD License',  # sample license
    keywords="Evolutionary Rubik Solver (Herdy's Algorithm used)",
    url="https://github.com/jstypka/evolutionary_rubik",

    # could also include long_description, download_url, classifiers, etc.
)