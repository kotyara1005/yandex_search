#! python3
# Yandex search
import webbrowser

import requests
import bs4


def search(subject):
    request = requests.get("https://yandex.ru/search/?text=" + subject)
    try:
        request.raise_for_status()
    except:
        print("Sorry, some errors occurred.")

    soup = bs4.BeautifulSoup(request.text, "html.parser")
    results = [{'text': tag.get_text(), 'link': tag["href"]}
               for tag in soup.select("a.link_cropped_no")]
    return results


def main():
    print("Enter your response: ", end='')
    request = input()
    results = search(request)
    print('\n'.join(
        (str(num) + ". " + result['text']
         for (num, result) in enumerate(results))
    ))

    flag = True
    while flag:
        print("Enter your choice: ", end='')
        try:
            choice = results[int(input())]['link']
        except:
            print("Sorry, some errors occurred. Check your input.")
        else:
            webbrowser.open(choice)
            flag = False

if __name__ == "__main__":
    main()
