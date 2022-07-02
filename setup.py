import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calc",
    version="0.0.1",
    author="Alberto Ramírez",
    author_email="alberto.r.caballero.87@gmail.com",
    description="Ejemplo de como crear un paquete",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/albertorc87/subir-paquete-pypi",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.9, <4",
)