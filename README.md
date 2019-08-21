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

Execute the full code by typing the script name followed by a -h in command prompt or terminal:

```usage: tripadvisor.py [-h] url

positional arguments:
  url         Tripadvisor Listing URL

optional arguments:
  -h, --help  show this help message and exit
```

Here is the command to extract the first-page of restaurant listings in Boston, MA.:


```
python3 tripadvisor.py https://www.tripadvisor.com/Restaurants-g60745-Boston_Massachusetts.html
```

## Output
[Sample Output](https://github.com/scrapehero-code/tripadvisor-scraper/blob/master/tripadvisor-restaurants.csv)
