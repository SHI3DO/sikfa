import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="sikfa",
    version="0.0.2",
    author="shi3do",
    author_email="shi3doemail@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/SHI3DO/sikfa",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
