from setuptools import setup, find_packages

setup(
    name="tennis-kata",
    version="1.0.0",
    description="Tennis scoring kata with BDD approach",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest>=7.4.3",
        "pytest-bdd>=7.0.0",
        "pytest-cov>=4.1.0",
    ],
    python_requires=">=3.8",
)