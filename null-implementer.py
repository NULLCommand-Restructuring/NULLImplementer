import argparse
from colorama import init, Fore
import sys
import os
import processing_kernel.research_kernel as research_kernel
import processing_kernel.imager_kernel as imager_kernel
import processing_kernel.inviter_kernel as inviter_kernel

VERSION_NUMBER = '0.1.0'
null_implementer_parameters_dir = 'D:\\null-implementer-config'
default_parameters = {
    "BING_COOKIE": "",
    "BROWSER": "firefox",
    "LANG": "English",
    "GPT_EMAIL": "project.someone@hotmail.com"
}

def handle_config(args):
    try:
        if not os.path.exists(null_implementer_parameters_dir):
            os.makedirs(null_implementer_parameters_dir)
            print(Fore.GREEN + f'The {null_implementer_parameters_dir} folder has been automatically created to store parameters ✔️')
        for file_name, content in default_parameters.items():
            file_path = os.path.join(null_implementer_parameters_dir, file_name)
            if not os.path.exists(file_path):
                print(Fore.GREEN + f'Initialized to default value "{content}" for "{file_name}" ✔️' + Fore.RESET)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
        if args.browser == None and args.bingcookie == None and args.lang == None and args.gptemail == None:
            config_info = 'Current configuration information of NULL Implementer ✔️\n'
            with open(os.path.join(null_implementer_parameters_dir, "BROWSER"), 'r') as file:
                config_info = config_info + 'The browser uses cookie data collection to serve requests to Gemini: ' + file.read() + '\n'
            with open(os.path.join(null_implementer_parameters_dir, "BING_COOKIE"), 'r') as file:
                config_info = config_info + 'The .bing.com site\'s _U cookie value to serve imaging requests: ' + file.read() + '\n'
            with open(os.path.join(null_implementer_parameters_dir, "LANG"), 'r', encoding='utf-8') as file:
                config_info = config_info + 'The language the AI ​​will use to present responses: ' + file.read() + '\n'
            with open(os.path.join(null_implementer_parameters_dir, "GPT_EMAIL"), 'r', encoding='utf-8') as file:
                config_info = config_info + 'ChatGPT account default email needs to unlock Plus feature: ' + file.read() + '\n'
            print(Fore.GREEN + config_info + Fore.RESET)
            sys.exit(0)
        if args.browser:
            with open(os.path.join(null_implementer_parameters_dir, "BROWSER"), 'w') as file:
                file.write(args.browser)
        if args.bingcookie:
            with open(os.path.join(null_implementer_parameters_dir, "BING_COOKIE"), 'w') as file:
                file.write(args.bingcookie)  
        if args.lang:
            with open(os.path.join(null_implementer_parameters_dir, "LANG"), 'w', encoding='utf-8') as file:
                file.write(args.lang)  
        if args.gptemail:
            with open(os.path.join(null_implementer_parameters_dir, "GPT_EMAIL"), 'w', encoding='utf-8') as file:
                file.write(args.gptemail)  
        print(Fore.GREEN + f'Successful configuration of NULL Implementer, please use "config" without parameters to view current configuration information ✔️' + Fore.RESET)
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + 'Error: ' + str(e) + ' ❌' + Fore.RESET)
        sys.exit(1)

def handle_research(args):
    try:
        research_kernel.main(null_implementer_parameters_dir, args.prompt, args.resource)
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + 'Error: ' + str(e) + ' ❌' + Fore.RESET)
        sys.exit(1)   

def handle_imager(args):
    try:
        imager_kernel.main(null_implementer_parameters_dir, args.prompt)
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + 'Error: ' + str(e) + ' ❌' + Fore.RESET)
        sys.exit(1)   

def handle_unlocker(args):
    try:
        inviter_kernel.main(args.email)
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + 'Error: ' + str(e) + ' ❌' + Fore.RESET)
        sys.exit(1)

def main():
    global VERSION_NUMBER
    parser = argparse.ArgumentParser(description='NULL Implementer - Unleashing The Power Of Artificial Intelligence', allow_abbrev=False)
    parser.add_argument('--v', action='version', version=Fore.GREEN + f'NULL Implementer - v{VERSION_NUMBER} by OpenFXT x NULL Command' + Fore.RESET + ' ✔️')
    parser.add_argument('--version', action='version', version=Fore.GREEN + f'NULL Implementer - v{VERSION_NUMBER} by OpenFXT x NULL Command' + Fore.RESET + ' ✔️')

    subparsers = parser.add_subparsers(dest='command', required=True)
    config_parser = subparsers.add_parser('config', help='Configuration-related options')
    config_parser.add_argument('--browser', help='Set the browser type value used to collect the necessary cookie data for generative AI to function', default=None)
    config_parser.add_argument('--bingcookie', help='Setting the value of the _U cookie for the .bing.com site is required for AI image generation to function', default=None)
    config_parser.add_argument('--lang', help='Set the language that the generative AI will use to respond to text generation requests', default=None)
    config_parser.add_argument('--gptemail', help='Set the email address of the default ChatGPT account that will be used to unlock Plus features when you do not provide a specific parameter', default=None)
    config_parser.set_defaults(func=handle_config)

    research_parser = subparsers.add_parser('research', help="Option to use generative AI for research tasks and responding to text requests")
    research_parser.add_argument('--resource', help='Set one or more resources used in text generation requests for generative AI (optional)', nargs='+', default=[])
    research_parser.add_argument('--prompt', help='Set a prompt for the generating AI', required=True, default=None)
    research_parser.set_defaults(func=handle_research)

    imager_parser = subparsers.add_parser('imager', help="Option to use AI for image generation")
    imager_parser.add_argument('--prompt', help='Set a prompt for the generating AI to create images', required=True, default=None)
    imager_parser.set_defaults(func=handle_imager)

    default_email = 'email@domain'
    try:
        with open(os.path.join(null_implementer_parameters_dir, "GPT_EMAIL"), 'r') as file:
            default_email = file.read()
    except:
        pass 
    gpt_plus_unlocker = subparsers.add_parser('gptunlocker', help="Option used to unlock Plus features on a regular ChatGPT account")
    gpt_plus_unlocker.add_argument('--email', help='Set the email address of the ChatGPT account to be unlocked to Plus account', default=default_email)
    gpt_plus_unlocker.set_defaults(func=handle_unlocker)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)

if __name__ == "__main__":
    main()