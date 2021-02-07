import requests
from bs4 import BeautifulSoup

wikipedia_url = 'https://en.wikipedia.org/wiki/2020_Nagorno-Karabakh_war'


def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations_needed = soup.findAll(title="Wikipedia:Citation needed")
    return len(citations_needed)


def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations_needed = soup.findAll(title="Wikipedia:Citation needed")
    target_passages = [citation.find_parent(
        'p').text for citation in citations_needed]
    passages_string = ''
    for passage in target_passages:
        passage = passage.strip('\n ')
        passages_string += passage + '\n\n'

    return passages_string[:-2]


print(get_citations_needed_count(wikipedia_url))
print(get_citations_needed_report(wikipedia_url))
