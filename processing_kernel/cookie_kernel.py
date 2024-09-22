import browser_cookie3
import os

RESEARCH_RESOURCE_LINK = '.google.com'

def get_research_resource(browser_type):
    global RESEARCH_RESOURCE_LINK
    target_resource = {}
    target_resource['err'] = ''
    cj = ''
    if browser_type == 'edge':
        cj = browser_cookie3.edge(domain_name=RESEARCH_RESOURCE_LINK)
    elif browser_type == 'firefox':
        cj = browser_cookie3.firefox(domain_name=RESEARCH_RESOURCE_LINK)
    elif browser_type == 'chrome':
        cj = browser_cookie3.chrome(domain_name=RESEARCH_RESOURCE_LINK)
    else:
       target_resource['err'] = f'Error: Browser type "{browser_type}" configured in NULL Implementer is not supported, please use "config --browser BROWSER" command to reconfigure another browser type ❌'
    for cookie in cj:
        if cookie.name == '__Secure-1PSID' or cookie.name == '__Secure-1PSIDTS':
            target_resource[cookie.name] = cookie.value
    return target_resource

def get_imager_resource(null_implementer_parameters_dir):
    target_resource = {}
    target_resource['err'] = ''
    try:
        with open(os.path.join(null_implementer_parameters_dir, "BING_COOKIE"), 'r') as file:
            target_resource['_U'] = file.read()
    except Exception as e:
         target_resource['err'] = 'Error: ' + str(e) + ' ❌'
    return target_resource