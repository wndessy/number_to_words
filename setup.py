import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='number_to_words',
     version='0.1.2',
     scripts=['number_to_words_script'],
     author="Winnie Ndessy",
     author_email="wndessy@gmail.com",
     description="Python converter of numbers in figures to words",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/wndessy/number_to_words",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )