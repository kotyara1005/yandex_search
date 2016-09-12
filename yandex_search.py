#! python3
# Yandex search

import requests, bs4, webbrowser

def search(response):
    request = requests.get("https://yandex.ru/search/?text=" + response)
    try:
        request.raise_for_status()
    except:
        print("Sorry, some errors occurred.")

    soup = bs4.BeautifulSoup(request.text, "lxml")
    results = [{'text': tag.get_text(), 'link': tag["href"]} for tag in soup.select("a.link_cropped_no")]
    return results

if __name__ == "__main__":
    print("Enter your response:", end='')
    response = input()
    results = search(response)
    print('\n'.join((str(num) + ". " + result['text'] for (num, result) in enumerate(results))))

    flag = True
    while flag:
        print("Enter your choice:", end='')
        try:
            choice = results[int(input())]['link']
        except:
            print("Sorry, some errors occurred. Check your input.")
        else:
            webbrowser.open(choice)
            flag = False
