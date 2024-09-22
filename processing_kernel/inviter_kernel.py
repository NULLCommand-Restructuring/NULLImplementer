import threading
import os
import time
import sys
import requests
import re
from colorama import init, Fore
init()
api_done = False

URL = 'https://gpteam-openfxt.vercel.app/unlock_key_source/first_source.txt'

def main(email):
    global URL
    response = requests.get(URL)
    if response.status_code == 200:
        unlock_key = response.text
        unlock_key = unlock_key.replace('\\"', '"')
        data = pattern_data(unlock_key)
        handle(email, data, data['url_pattern'])
    else:
        raise Exception("Unlock key source has problem, please try again later")

def pattern_data(unlock_key):
    patterns = {
        "authorization": r'"authorization":\s*"([^"]+)"',
        "url_pattern": r'fetch\("([^"]+)"',
        "account_id_pattern": r'"chatgpt-account-id":\s*"([^"]+)"',
        "oai_device_id_pattern": r'"oai-device-id":\s*"([^"]+)"',
        "cookie": r'"cookie":\s*"(.*?)"\s*,'
    }
    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, unlock_key)
        if match:
            value = match.group(1)
            data[key] = value
        else:
            raise Exception('Unlock key data is incomplete, please try again later')
    return data

def handle(email_data, data, url):
    global api_done
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": data['authorization'],
        "chatgpt-account-id": data['account_id_pattern'],
        "chatgpt-residency-region": "no_constraint",
        "content-type": "application/json",
        "oai-device-id": data['oai_device_id_pattern'],
        "oai-language": "en-US",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": data['cookie'],
        "Referer": "https://chatgpt.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    body = {
        "email_addresses": [email_data],
        "role": "standard-user",
        "resend_emails": False
    }
    threading.Thread(target=loading).start()
    response = requests.post(url, headers=headers, json=body)
    api_done = True
    time.sleep(0.5)
    if response.status_code == 200:
        print(Fore.GREEN + f"ChatGPT (Email: {email_data}) unlocked successfully, please reload your ChatGPT to display Plus features!✔️" + Fore.RESET)
    else:
        raise Exception(response.text)

def loading():
    global api_done
    try:
        time.sleep(0.2)
        os.system('cls')
        sys.stdout.write("\033[32mUnlocking... ")
        sys.stdout.flush()
        
        spinner = ['/', '-', '\\', '|']
        start_time = time.time()
        
        while not api_done:
            for symbol in spinner:
                sys.stdout.write(symbol)
                sys.stdout.flush()
                time.sleep(0.1)
                sys.stdout.write("\b")
        
        sys.stdout.write("\033[2K\r\033[0m")
        sys.stdout.flush()

    except KeyboardInterrupt:
        sys.stdout.write("\033[2K\r\033[0m")
        sys.stdout.flush()
        sys.exit(1)