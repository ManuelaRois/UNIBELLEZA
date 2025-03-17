from setuptools import setup, find_packages

setup(
    name="Unibelleza",
    version="1.0.0",
    description="Sistema de inventario para tienda de maquillaje",
    author="Manuela Rois, Maria Antonia Montoya",
    author_email="manuela.rois@upb.edu.co, mariaa.montoyas@upb.edu.co",
    url="https://github.com/ManuelaRois/UNIBELLEZA",
    packages=find_packages(),
    install_requires=[
        "sqlite3",  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "unibelleza=main:main",  
        ],
    },
    python_requires='>=3.8',
)