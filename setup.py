import setuptools

with open ("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CeleryFlask",
    version="0.0.1",
    author="Ganggas95",
    author_email="subhannizar25@gmail.com",
    description="""Extension Flask for integration with celery""",
    long_description=long_description,
    license="MIT",
    long_description_content_type="text/markdown",
    url="https://github.com/ganggas95/celery-flask",
    packages=setuptools.find_packages(),
    py_module=["celery_flask"],
    include_package_data=True,
    install_requires=[
        'Flask >= 1.0',
        'Celery >= 4.4.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database"
    ],
)