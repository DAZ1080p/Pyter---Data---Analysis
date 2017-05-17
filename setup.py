from setuptools import setup, find_packages

setup(
        name='data_analysis',
        version='0.0.1',
        url='www.github.com/DAZ1080p/Pyer---Data---Analysis',
        Author='DAZ1080p',
        packages=find_packages(),
        install_requires=['PyQt5',
                          'pandas',
                          'sqlalchemy',
                          'nltk',
                          'numpy',
                          'jupyter',
                          'pyhton-twitter'],
        entry_points={},
        extras_require={'dev':['flake8',]},
)
