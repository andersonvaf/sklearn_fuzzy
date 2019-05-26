import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='sklearn_fuzzy',
     version='0.0.8',
     author="Anderson Vinicius",
     author_email="andersonvaf@gmail.com",
     description="`sklearn_fuzzy` is a fork from `scikit-fuzzy` package with sklearn-ish methods.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/andersonvaf/sklearn_fuzzy",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
