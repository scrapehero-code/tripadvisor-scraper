import argparse
import csv

import requests
from selectorlib import Extractor
from formatter_classes import formatters


def write_to_file(response):
    # writes HTML response to a file for debugging purpose
    with open("response.html", "w") as fp:
        fp.write(response.text)


def process_page(url):
    # Create an Extractor by reading from the YAML file
    e = Extractor.from_yaml_file(
        'tripadvisor_restaurants.yml',
        formatters=formatters)
    # Download the page using requests
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}  # noqa
    print('Downloading Page')
    r = requests.get(url, headers=headers, timeout=30)
    # Pass the HTML of the page and create
    print("Parsing Page")
    data = e.extract(r.text)
    if not data['restaurants']:
        write_to_file(r)
    return data


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('url', help='Tripadvisor Listing URL')
    args = argparser.parse_args()
    scraped_data = process_page(args.url)

    if scraped_data:
        print("Writing scraped data to restaurants.csv")
        with open('restaurants.csv', 'w') as csvfile:
            fieldnames = ["name", "reviews", "cusine",
                          "rating", "price_range", "url"]
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for data in scraped_data['restaurants']:
                writer.writerow(data)
    else:
        print("No data scraped")
