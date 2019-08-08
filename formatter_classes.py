from selectorlib import Formatter
import re


class Url(Formatter):
    def format(self, text):
        url = 'https://www.tripadvisor.com' + text
        return url


class Reviews(Formatter):
    def format(self, text):
        reviews = text.replace('reviews', '').replace(',', '').strip()
        return reviews


class Rating(Formatter):
    def format(self, text):
        raw_rating = re.findall(r'\d+\.?\d?', text)
        if raw_rating:
            rating = raw_rating[0]
            return rating


class Name(Formatter):
    def format(self, text):
        clened_name = re.sub(r"^\d+.", "", text).strip()
        return clened_name


formatters = Formatter.get_all()
