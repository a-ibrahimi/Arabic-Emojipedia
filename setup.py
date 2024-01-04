from setuptools import setup, find_packages

setup(
    name='arabic_emojipedia',
    version='1.0.4',
    packages=find_packages(),
    install_requires=[],
    description='A Python package to get emoji descriptions in Arabic',
    author='Anass Ibrahimi',
    author_email='a.ibrahimi@tum.de',
    url='https://github.com/a-ibrahimi/Arabic-Emojipedia',
    include_package_data=True,
    package_data={
        'arabic_emojipedia': ['data/*.csv'],
    },
)
