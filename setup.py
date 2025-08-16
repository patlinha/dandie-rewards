# setuptools
from setuptools import setup, find_packages

setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    aothor="Pati LinA",
    packages=find_packages(), #vai retornar todos os pacotes q tenham o __init__ dentro
)

# pyproject

# external build tools (poetry, flit)