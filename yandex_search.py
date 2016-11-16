#! python3
# -*- coding: UTF-8 -*-
# Yandex search
import webbrowser
from collections import namedtuple

import requests
import bs4

__author__ = 'Artem Krivonos'
__version__ = '1.0.0'

SearchResult = namedtuple('SearchResult', 'title link')


def search(subject):
    """
    >>> search('python') # doctest: +ELLIPSIS
    [SearchResult(...)...]
    """
    request = requests.get("https://yandex.ru/search/?text=" + subject)
    request.raise_for_status()

    soup = bs4.BeautifulSoup(request.text, "html.parser")
    results = [SearchResult(tag.get_text(), tag["href"])
               for tag in soup.select("a.link_cropped_no")]
    return results


def main():
    print("Enter your response: ", end='')
    request = input()
    try:
        results = search(request)
    except requests.exceptions.HTTPError:
        print("Sorry, some errors occurred.")
    else:
        for num, result in enumerate(results):
            print(str(num) + ". " + result.title)

        flag = True
        while flag:
            print("Enter your choice: ", end='')
            try:
                index = int(input())
                choice = results[index].link
            except (ValueError, IndexError):
                print("Sorry, some errors occurred. Check your input.")
            else:
                webbrowser.open(choice)
                flag = False

if __name__ == "__main__":
    main()
