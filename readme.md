
# Cybersecurity Python Projects 🔐

These python projects will all incorporate and use the different realm of Cybersecurity concepts.

I'm creating these "mini" projects to establish my footing in development again to utilize my knowledge as a Cybersecurity Analyst with my software development skills.


## urlscan.io API usage

This project utilizes the [urlscan.io](urlscan.io) API to parse for a dictionary object which contains results pulled from .

Reasoning:

In security, a large portion of work revolves around parsing and figuring out how to interface an API with SOAR platforms to enhance data (i.e. XSOAR, Archer, etc..) I wanted to present a challenge to myself to utilize the urlscan.io API without pulling down a third party library, and just utilizing the requests library from Python. 

Requirements to run: 

- urlscan.io API key
    1. Create an account @ [urlscan.io](urlscan.io)
    2. Get API key under `Profile` > `Settings & API`

- creation of config.py file
    1. Grab urlscan.io API key
    2. Create variable `URLSCANIO_KEY = <api_key>`

- requests library
    1. Ensure pip is installed, reference [here](https://pip.pypa.io/en/stable/cli/pip_install/).
    2. `pip install requests`

- json library
    1. Ensure pip is installed, reference [here](https://pip.pypa.io/en/stable/cli/pip_install/).
    2. `pip install json`

- time library
    1. Ensure pip is installed, reference [here](https://pip.pypa.io/en/stable/cli/pip_install/).
    2.  `pip install json`

