from setuptools import setup

setup(name="cyberark",
  version="0.1.1",
  description="CyberArk API functions without certificate validation",
  url="https://github.com/LikeZer0/python-cyberark",
  author="Erik Bonizzoni",
  author_email="erik.bonizzoni@gmail.com",
  license="MIT",
  packages=["cyberark"],
  install_requires=["requests"],
  zip_safe=False)
