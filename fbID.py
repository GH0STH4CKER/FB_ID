import xml , os , time
from xml import etree
from xml.etree import ElementTree

try:
    import requests as reqs 
    from colorama import Fore , init
    from bs4 import BeautifulSoup as bSoup
    init()

except ModuleNotFoundError as e :

    print("Missing Modules !")
    minstall = input("\nDo you want to install them ? (yes/no) ")
    
    if minstall == "yes" or minstall == "YES" or minstall == "Yes"  :
        os.system("pip install -r requirements.txt")
        print("\n Re-Run the program .")
        input("\nExit >")
    else :
        print(e)    
        input("\nExit >")

banner = """
█▀▀ ▄▀█ █▀▀ █▀▀ █▄▄ █▀█ █▀█ █▄▀   █ █▀▄
█▀░ █▀█ █▄▄ ██▄ █▄█ █▄█ █▄█ █░█   █ █▄▀"""
title = """--------- [+] By GH0STH4CK3R ----------\n"""

try:
    print(Fore.GREEN + banner)
    print(Fore.LIGHTGREEN_EX + title)

    print("Example Input :- https://www.facebook.com/ghost.hacker.21 or ghost.hacker.21 \n")

    Uname = input("Facebook acount link or username : ")

    def rem_tags (st) :         # Removing html tag function

        return ''.join(xml.etree.ElementTree.fromstring(str(st)).itertext())

    if "http" in Uname or "/" in Uname or "www" in Uname :
        url = Uname
    else :    
        url = "https://www.facebook.com/" + Uname

    resp = reqs.get(url)
    
    if resp.status_code == 200 :

        data = resp.text

        id_loc = data.find("fb://profile/")
        F_id =  data[(id_loc+13):(id_loc+33)]

        while True :

            if F_id.isnumeric() :
                break
            F_id = F_id[:-1]

        page_html = data         
        page_soup = bSoup(page_html,"html.parser")

        names = page_soup.find("div",{"class":"fsxl fwb"})     

        print("")
        print(rem_tags(names))
        print("\nFacebook id :",F_id)

    else:
        print(Fore.LIGHTRED_EX +"\nEither username doesnt exist or url is incorrect !")
        print("\nError code",resp.status_code)    

except Exception as ee :

    print(Fore.LIGHTRED_EX +"\nSomething went wrong",ee)

input("\nExit >")
