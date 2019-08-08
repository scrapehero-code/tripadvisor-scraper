# Tripadvisor Restaurant Scraper
Scraper to extract restaurant details from Tripadvisor.com using Python and SelectorLib
## Details to extract
1. Restaurant Name
2. Restaurant Link
3. Cuisine
4. Price
5. Rating
6. Number of reviews

## Prerequisites
Install Python 3 and Pip. Follow the guides below:

- Linux – http://docs.python-guide.org/en/latest/starting/install3/linux/
- Mac – http://docs.python-guide.org/en/latest/starting/install3/osx/
- Windows  – https://www.scrapehero.com/how-to-install-python3-in-windows-10/
Packages
- PIP to install the following packages in Python (https://pip.pypa.io/en/stable/installing/ )
- Python Requests, to make requests and download the HTML content of the pages ( http://docs.python-requests.org/en/master/user/install/).
- SelectorLib to take the YAML file as input and parse the HTML. (Learn how to install that here https://selectorlib.readthedocs.io/en/latest/installation.html

## Code
https://github.com/scrapehero-code/tripadvisor-scraper/blob/master/tripadvisor_restaurants.py

## Export Product Data into CSV
To store the output as a CSV file: python3 tripadvisor.py <url>

Example

`python3 tripadvisor.py https://www.tripadvisor.com/Restaurant_Review-g60745-d537940-Reviews-Picco_Restaurant-Boston_Massachusetts.html`

## Output
[Sample Output](https://github.com/scrapehero-code/tripadvisor-scraper/blob/master/tripadvisor-restaurants.csv)
