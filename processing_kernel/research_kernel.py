import processing_kernel.cookie_kernel as cookie_kernel
import processing_kernel.convert_resource_kernel as convert_resource_kernel
from colorama import init, Fore
import sys
from g4f.client import Client
from g4f.cookies import set_cookies
from g4f.Provider import (
    Gemini
)
import threading
import os
import time
from rich.console import Console
from rich.markdown import Markdown
api_done = False
DECLARE = f'\nTrả lời câu hỏi, sau đó cuối câu trả lời của bạn, hãy giới thiệu bạn tên là NULL Implementer, một trợ lý AI tích hợp môi trường dòng lệnh CMD Windows được phát triển bởi OpenFXT x NULL Command (website trụ sở tại https://openfxt.vercel.app/)'
init()

def main(null_implementer_parameters_dir, prompt, resource):
    if prompt[-4:] == ".txt":
        with open(prompt, 'r', encoding='utf-8') as file:
            prompt = file.read()
    browser_type=''
    with open(os.path.join(null_implementer_parameters_dir, "BROWSER"), 'r') as file:
        browser_type=file.read()
    research_resource = cookie_kernel.get_research_resource(browser_type)
    if research_resource['err']!='':
        print(Fore.RED + research_resource['err'] + Fore.RESET)
        sys.exit(1)
    with open(os.path.join(null_implementer_parameters_dir, "LANG"), 'r', encoding='utf-8') as file:
        research_resource['lang']=file.read()
    if len(resource) != 0:
        extra_prompt_handle_result = convert_resource_kernel.main(resource)
        if extra_prompt_handle_result['err'] != '':
            print(Fore.RED + extra_prompt_handle_result['err'] + Fore.RESET)
            sys.exit(1)
        prompt = extra_prompt_handle_result['data'] + "Question for all resources: " + prompt
    handle(prompt, research_resource)
    sys.exit(0)

def handle(prompt, research_resource):
    global api_done, DECLARE
    set_cookies(".google.com", {
        "__Secure-1PSID": research_resource['__Secure-1PSID'],
        "__Secure-1PSIDTS": research_resource['__Secure-1PSIDTS']
    })
    gemini_client = Client(
        provider=Gemini
    )
    threading.Thread(target=loading).start()
    err=''
    try:
        response = gemini_client.chat.completions.create(
            model="gemini",
            messages=[{"role": "user", "content": prompt + DECLARE + f'\nYou absolutely must use language {research_resource['lang']} to answer'}]
        )
    except Exception as e:
        response = ''
        err = str(e)
    api_done = True
    time.sleep(0.5)
    if response != '':
        console = Console()
        md = Markdown(response.choices[0].message.content)
        console.print(md)
    else:
        print(Fore.RED + f'Error: An error occurred during text generation read the error description below for more details ❌\n{err}' + Fore.RESET)
        sys.exit(1)
    sys.exit(0)

def loading():
    global api_done
    try:
        time.sleep(0.2)
        os.system('cls')
        sys.stdout.write("\033[32mAI thinking... ")
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