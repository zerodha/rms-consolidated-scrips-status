from setuptools import setup


README = open("README.md").read()

setup(
    name="consolidatedrms",  
    version="0.4",
    author="Rakesh R",
    author_email="rrrakesh265@gmail.com",
    description="Python library for Zerodha RMS consolidated scrips",
    long_description=README,
    url="https://github.com/zerodhatech/rms-consolidated-scrips-status",
    packages=['consolidatedrms'],
    install_requires=["pandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries"
    ],
)