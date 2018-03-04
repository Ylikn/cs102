import requests
from bs4 import BeautifulSoup
import re

def get_page(url):
    try:
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            print("Error " + str(response.status_code))
            return False
    except requests.exceptions.ConnectTimeout:
        print('Oops. Connection timeout occured!')
    except requests.exceptions.ReadTimeout:
        print('Oops. Read timeout occured')
    except requests.exceptions.ConnectionError:
        print('Seems like dns lookup failed..')


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    for i in range(0, 90, 3):
        news = {'author': parser.table.findAll('table')[1].findAll('tr')[i + 1].findAll('td')[1].a.contents[0],
                'title': parser.table.findAll('table')[1].findAll('tr')[i].findAll('td')[2].a.contents[0],
                'comments': parser.table.findAll('table')[1].findAll('tr')[i + 1].findAll('td')[1].findAll('a')[5].contents[0],
                'points': parser.table.findAll('table')[1].findAll('tr')[i + 1].findAll('td')[1].span.contents[0],
                'url': parser.table.findAll('table')[1].findAll('tr')[i].findAll('td')[2].a['href']}
        news_list.append(news)
    return news_list

    
def extract_next_page(parser):
    """ Extract next page URL """
    more_link = parser.table.findAll('table')[1].findAll('a')[-1].get('href')
    return more_link


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = get_page(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news


def split_row(string):
    return list(filter(None, re.split('\W|\d', string)))

