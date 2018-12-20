# web scraper that utilizes BeautifulSoup
# checks to see if term exists on Merriam-Webster.com by trying to access expected URL
# if exists, pulls the HTML of that page and parses for pronunciation
# outputs pronunciation and URL (from initial check)

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import time

# open two output files for diacritics and URL
diacriticsFile = open('diacritics.txt', 'w', encoding='utf-8')
srcURLFile = open('srcURLFile.txt', 'w', encoding='utf-8')

print("initializing...")

# open input file and interate through lines
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        # read line from input and plug into URL format
        current_term = line.replace(' ', '%20')
        try_URL = 'https://www.merriam-webster.com/dictionary/' + current_term

        # try to get page
        try:
            req = Request(try_URL, headers={'User-Agent': 'Mozilla/5.0'})
            web_byte = urlopen(req).read()
            page_html = web_byte.decode('utf-8')

            # parse html
            page_soup = soup(page_html, 'html.parser');

            diacritics = page_soup.find('span', {'class': 'pr'}).text
            print(diacritics)
            link = try_URL
            print(link)

        # if cannot open URL, write empty strings to leave blank like for easy pasting into Excel
        except:
            diacritics = ''
            link = '\n'

        finally:
            # if connection not successful, then write empty strings
            diacriticsFile.write(diacritics + '\n')
            srcURLFile.write(link)
            time.sleep(5)

# close
diacriticsFile.close
srcURLFile.close
