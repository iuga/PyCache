from setuptools import setup, find_packages

setup(
    name="PyStorage",
    version="0.4.1",
    description="Lightweight Python Cache Storage Library",
    author="@iugax",
    packages=find_packages(exclude=["tests", "tools"]),
    install_requires=[
        'pylru==1.0.9'
    ]
)
