from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = ' '

setup(
   name="my-package",
   version=VERSION,
   author="Kim Boren",
   author_email="kimb@r-stealth.com",
   description=DESCRIPTION,
   packages=find_packages(),
   install_requires=["sourcedefender", "pandas"],
   setup_requires=['setuptools'],
   python_requires='>=3.9.0',

   include_package_data=True
)
