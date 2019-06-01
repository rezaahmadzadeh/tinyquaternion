import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-your-username",
    version="0.0.1",
    author="Reza Ahmadzadeh",
    author_email="reza.ahmadzadeh.iit@gmail.com",
    description="A Tiny Python Package for Quaternions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rezaahmadzadeh/tinyquaternion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)