from setuptools import setup, find_packages

setup(
    name="get_secret_manager",
    version="1.0",
    python_requires='>=3.11',
    packages=find_packages(),
    install_requires=[
        'boto3>=1.35,<2.0'
    ]

)
