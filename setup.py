from setuptools import setup, find_packages

setup(
    name="Credit_Card",
    version="0.1.0",
    python_requires='==3.9.19',
    install_requires=[
        "numpy",
        "pandas",
        "notebook",
        "tensorflow",
        "matplotlib",
        "python-box",
        "pyYAML",
        "seaborn",
        "scikit-learn",
        "imbalanced-learn",
        "joblib",
        "Flask",
        "ensure",
        "Flask-Cors",
        "types-pyYAML"
    ],
    packages=find_packages(),
)
