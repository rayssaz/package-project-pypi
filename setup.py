from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="bubble",
    version="0.0.1",
    author="Rayssa Pereira",
    author_email="rayssacristinne23@gmail.com",
    description="O pacote contém o algoritmo de ordenação Bubble Sort, o qual pode ser aplicado em arrays e listas dinâmicas.. ",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rayssaz/package-project-pypi"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
