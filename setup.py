from setuptools import setup, find_packages

setup(
    name="jsonlines-dropkeys",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["jsonlines"],
    entry_points={
        "console_scripts": [
            "jsonlines-dropkeys=jsonlines_dropkeys.dropkeys:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
