from setuptools import find_packages, setup, Extension

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pySorts",
    version="0.0.10",
    description="An application that compares sorting algorithm implentations by language and algorithm",
    package_dir={"": "src/python"},
    packages=find_packages(where="src/python"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jon Atkinson",
    license="MIT",
    classifiers=[
        "License :: OSI Appproved :: MIT License",
        "Programming Language :: Python :: 3.11.5",
        "Programming Language :: C",
        "Operating System :: OS Independent",
    ],
    ext_modules=[
        Extension(
            "cSorts",
            sources=["src/c/cSorts.c"]
        )
    ],
    install_requires=[
        "matplotlib",
        "numpy",
    ],
    extras_require={
        "dev": [
            "unittest"
        ],
    },
    python_requires=">=3.10",
    include_package_data=True,
    zip_safe=False,
)