"""Setup module to install package."""
from setuptools import setup, find_packages


# README.md file
# ==============
def readme():
    """Readme file."""
    with open("README.md") as f:
        return f.read()


# requirements.txt file
# =====================
def requirements():
    """Requirement file."""
    with open("requirements.txt") as f:
        return f.read()


# Dependency links
# ================
dependency_links = []

# Description
# ===========
description = "Cash register of a clothing store"

# setup
# =====
setup(
    name="cashRegister",
    version="0.0.1",
    author=["Rabi Ouallam Jamladi"],
    author_email=["rabaixa@gmail.com"],
    description=description,
    classifiers=[],
    long_description=readme(),
    packages=find_packages(),
    install_requires=requirements(),
    include_package_data=True,
    dependency_links=dependency_links,
    entry_points={
        "console_scripts": [
            "scan_clothes=cashRegister.main:main"
        ]
    },
)




