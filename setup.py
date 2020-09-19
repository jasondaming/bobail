import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "imparaai-bobail",
    version = "1.4.2",
    license = 'MIT',
    author = "ImparaAI",
    author_email = "author@example.com",
    description = "Library for playing a standard game of bobail/draughts",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ImparaAI/bobail",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)