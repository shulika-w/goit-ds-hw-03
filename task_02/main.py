import json
import requests
from bs4 import BeautifulSoup


def get_author_details(author_url):
    response = requests.get(author_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    fullname = soup.find('h3', class_='author-title').text.strip()
    born_date = soup.find('span', class_='author-born-date').text.strip()
    born_location = soup.find('span', class_='author-born-location').text.strip()
    description = soup.find('div', class_='author-description').text.strip()

    return {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }


def scrape_authors(url):
    authors = []
    author_set = set()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        author_name = quote.find('small', class_='author').text
        author_url = quote.find('a')['href']
        if author_name not in author_set:
            author_details = get_author_details("https://quotes.toscrape.com" + author_url)
            authors.append(author_details)
            author_set.add(author_name)

    return authors


def scrape_quotes(url):
    quotes_data = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text.strip()
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        quote_details = {
            "tags": tags,
            "author": author,
            "quote": text
        }

        quotes_data.append(quote_details)

    return quotes_data


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    url = "https://quotes.toscrape.com/"
    authors = scrape_authors(url)
    save_to_json(authors, 'authors.json')
    quotes = scrape_quotes(url)
    save_to_json(quotes, 'quotes.json')
