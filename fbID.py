import xml , os , time , re
from bs4 import BeautifulSoup

try:
    import requests as reqs 
    from colorama import Fore , init
    from bs4 import BeautifulSoup as bSoup
    init()

except ModuleNotFoundError as e :

    print("Missing Modules !")
    exit()

banner = """
█▀▀ ▄▀█ █▀▀ █▀▀ █▄▄ █▀█ █▀█ █▄▀   █ █▀▄
█▀░ █▀█ █▄▄ ██▄ █▄█ █▄█ █▄█ █░█   █ █▄▀"""
title = """--------- [+] By GH0STH4CK3R ----------\n"""

try:
    print(Fore.GREEN + banner)
    print(Fore.LIGHTGREEN_EX + title)
    extracted_number = ''

    print("Example Input :- https://www.facebook.com/ghost.hacker.21 or ghost.hacker.21 \n")

    Uname = input("Facebook acount link or username : ")

    if "http" in Uname or "/" in Uname or "www" in Uname :
        url = Uname
    else :    
        url = "https://www.facebook.com/" + Uname

    resp = reqs.get(url)
    
    if resp.status_code == 200 :

        data = resp.text
        
        soup = BeautifulSoup(data, 'html.parser')
        meta_tag = soup.find('meta', {'property': 'al:ios:url'})
        content_value = meta_tag.get('content')
        meta_tag2 = soup.find('meta', {'property': 'al:android:url'})
        content_value2 = meta_tag2.get('content')
        

        pattern = r'fb://profile/(\d+)'
        match = re.search(pattern, content_value)
        match2 = re.search(pattern, content_value2)

        if match:
            extracted_number = match.group(1)
            print('\nYour Facebook ID : ',extracted_number)
        else:
            if match2 :
                print('\nYour Facebook ID : ',match2.group(1))
            else:
                print("FB ID not found.")

        if extracted_number != '' :

            url = "https://www.facebook.com/profile.php?id="+extracted_number 
            response = reqs.get(url, allow_redirects=True)
            redirected_url = response.url

            response = reqs.get(redirected_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_tag3 = soup.find('meta', {'name': 'description'})
            content_value3 = meta_tag3.get('content')
            print('\nFacebook Profile Name : ',content_value3[0:content_value3.find('is on Facebook')])

    else:
        print(Fore.LIGHTRED_EX +"\nEither username doesnt exist or url is incorrect !")
        print("\nError code",resp.status_code)    

except Exception as ee:

    print(Fore.LIGHTRED_EX +"\nSomething went wrong",ee)

input("\nExit >")
