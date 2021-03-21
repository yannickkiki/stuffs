from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    README = readme.read()

setup(
    name="yannorm_usage_template",
    version="0.0.1",
    author="xxx",
    author_email="xxx@gmail.com",
    description="Usage template of yannorm",
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
    ],
)
