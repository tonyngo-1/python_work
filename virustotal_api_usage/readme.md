# VirusTotal API usage

This project utilizes the [VirusTotal](virustotal.com) API to parse for a dictionary object which contains results pulled from the official VirusTotal library.

## Reasoning:

In security, a large portion of work revolves around parsing and figuring out how to interface an API with SOAR platforms to enhance data (i.e. XSOAR, Archer, etc..) This project utilizes the VirusTotal Official Library, which will be graciously provided for us (in some cases) for ease of use in python. 

## Requirements: 

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