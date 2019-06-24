# Tripadvisor Scraper
Scraper to extract restaurant details from Tripadvisor.com using Scrapy

## Details to extract
1. Restaurant Name
2. Restaurant Link
3. Cuisine
4. Price
5. Rank
6. Rating
7. Number of reviews

## Prerequisites
Install Python 3 and Pip. Follow the guides below:

Linux – http://docs.python-guide.org/en/latest/starting/install3/linux/
Mac – http://docs.python-guide.org/en/latest/starting/install3/osx/
Windows  – https://www.scrapehero.com/how-to-install-python3-in-windows-10/

## Export Product Data into JSON or CSV using Scrapy

To store the output as a CSV file:

scrapy crawl tripadvisor -o tripadvisor.csv -t csv

For a JSON file:

scrapy crawl tripadvisor -o tripdvisor.csv -t json

## Code
https://gist.github.com/scrapehero-code/4e82feacd1dbe8dc5124478a5f9fa0ba

## Output
[Output](https://github.com/scrapehero-code/tripadvisor-scraper/blob/master/tripadvisor-restaurants.csv)
