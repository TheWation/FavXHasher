# FavXHasher

[![made-with-python](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://forthebadge.com/images/badges/built-with-love.svg)](https://gitHub.com/TheWation/)

FavXHasher is a simple command-line tool designed to calculate the hash value of a favicon from a given URL. This tool can be particularly useful for detecting potential phishing websites by leveraging Shodan's search capabilities.

## Prerequisites

- Python 3.7 or later
- `pip` package manager

## Installation

1. Clone this repository:

```bash
git clone https://github.com/TheWation/FavXHasher.git
cd FavXHasher
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
To use FavXHasher, simply run the script with the `-u` or `--url` option followed by the URL of the favicon you want to generate the hash for. For example:

```bash
python FavXHasher.py -u http://example.com/favicon.ico
```

After executing the command, FavXHasher will fetch the favicon from the provided URL, calculate its hash value, and display the result along with a tip on how to use it with Shodan to detect potential phishing sites.

## Disclaimer
FavXHasher is provided for educational and informational purposes only. The authors do not condone or support any illegal activities that may be carried out using this tool. It is the responsibility of the user to ensure that they have appropriate authorization before using this tool on any website.

## License
`FavXHasher` is made with ♥  by [Wation](https://github.com/TheWation) and it's released under the `MIT` license.
