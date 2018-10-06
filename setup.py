import setuptools

# Just for keep in touch
# python3 setup.py sdist bdist_wheel
# twine upload dist/*

with open("READMEPYPI.md", "r") as fh:
    long_description = fh.read()

version = "1.0.1"

setuptools.setup(
    name="gdf_formatter",
    version=version,
    author="Gabriel Martins Trettel",
    author_email="gabrielmtrettel@gmail.com",
    description="GDF formatter for networks representation",
    long_description=long_description,
    url="https://github.com/GabrielTrettel/GDF_Formatter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
)
