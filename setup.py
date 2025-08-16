# setuptools
from setuptools import setup, find_packages

setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    author="Pati LinA",
    packages=find_packages(), #vai retornar todos os pacotes q tenham o __init__ dentro
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    }
)

# pyproject

# external build tools (poetry, flit)
