from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='landscapes',
    version='0.0.3',
    author='Nathan A. Rooy',
    author_email='nathanrooy@gmail.com',
    url='https://github.com/nathanrooy/landscapes',
    description='A Python library of standardized optimization test functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['landscapes'],
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
