import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-debauto-br",
    version="0.0.1",
    author="Flavio Milan",
    author_email="flaviomilan@outlook.com",
    description="Criar remessas de débito automático brasil",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flaviomilan/python-debauto-br",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)