import requests
from colorama import Fore

fg = Fore.GREEN
fr = Fore.RED

def make_request(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.ConnectionError:
        return None

with open(input("Enter a list: "),"r",encoding="utf-8") as domain_list:
    save_file = "found.txt"
    for word in domain_list:
        word = word.strip()
        url = "http://" + word
        response = make_request(url)
        if response and response.status_code == 200:
            print(Fore.GREEN + "yea ->" + url)
        else:
            print(Fore.RED + "nope ->" + url)
