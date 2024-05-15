from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='car_model_fixtures',
    version='0.1.0',
    description='Aims to add popular continental car models by continent and '
                'year for realistic test data in the mobility sector',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Imperatus/car_model_fixtures',
    author='Jurgen Buisman',
    author_email='jurgen@twodamdigital.nl',
    license='MIT',
    packages=['car_model_fixtures'],
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
)