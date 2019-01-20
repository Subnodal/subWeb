import os

try:
    from setuptools import setup
except ImportError:
    print("Getting setuptools...")
    os.system("sudo pip3 install python-setuptools > /dev/null")

    from setuptools import setup

setup(
    name = "subWeb",
    version = "0.1.0",
    description = "Custom website engine for the terminal.",
    url = "https://subnodal.com",
    author = "Subnodal Technologies",
    author_email = "hi@subnodal.com",
    packages = ["subWeb"],
    zip_safe = False
)
