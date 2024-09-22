from g4f.cookies import set_cookies
from g4f.Provider import (
    BingCreateImages
)
from colorama import init, Fore
init()
import threading
import os
import time
import sys
from g4f.client import Client
import processing_kernel.cookie_kernel as cookie_kernel
api_done = False

def main(null_implementer_parameters_dir, prompt):
    research_resource = cookie_kernel.get_imager_resource(null_implementer_parameters_dir)
    if research_resource['err']!='':
        print(Fore.RED + research_resource['err'] + Fore.RESET)
        sys.exit(1)
    handle(prompt, research_resource)
    sys.exit(0)

def handle(prompt, research_resource):
    global api_done
    set_cookies(".bing.com", {
        "_U": research_resource['_U']
    })
    client = Client(
        image_provider=BingCreateImages
    )
    threading.Thread(target=loading).start()
    err = ''
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt
        )
    except Exception as e:
        err = str(e)
        response = ''
    api_done = True
    time.sleep(0.5)
    if response != '':
        image_url = response.data[0].url
        print(Fore.GREEN + "Create images successfully!✔️" + Fore.RESET)
        print(Fore.BLUE + "Visit this link to view images: " + image_url + Fore.RESET)
    else:
        print(Fore.RED + f'Error: An error occurred while creating the image, please read the error description below for more details ❌\n{err}' + Fore.RESET)
        sys.exit(1)
    sys.exit(0)

def loading():
    global api_done
    try:
        time.sleep(0.2)
        os.system('cls')
        sys.stdout.write("\033[32mAI is currently generating images... ")
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