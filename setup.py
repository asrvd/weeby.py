import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weeby.py",                     
    version="0.1.6",                        
    author="Ashish Bhushan",                     
    author_email="asheeshh9@gmail.com",
    description="API wrapper library for WeebyAPI",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    project_urls={
        'Homepage': 'https://github.com/asheeeshh/weeby.py',
    },
    packages=setuptools.find_packages(),    
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],                                      
    include_package_data=True,
    install_requires=["requests"]                    
)