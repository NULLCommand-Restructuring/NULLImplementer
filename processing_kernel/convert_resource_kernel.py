import processing_kernel.extract_text_kernel as extract

def main(resource_array):
    resource_convert = {}
    resource_convert['err'] = ''
    resource_convert['data'] = ''
    data = ''
    for resource in resource_array:
        handle_resource_result = handle(resource)
        if handle_resource_result['err'] == '':
            if resource.startswith("http"):
                name_replace = "text"
            else:
                name_replace = "from file " + resource
            data = data + "- Resource " + name_replace + ":\n" + handle_resource_result['convert_text'] + "\n"
            if len(data) > 30000:
                resource_convert['err'] = 'Error: The resources provided are too numerous, please reduce or divide them into smaller parts and study them individually ❌'
                return resource_convert
        else: 
            resource_convert['err'] = handle_resource_result['err']
            return resource_convert
    resource_convert['data'] = "From all resources:\n" + data
    return resource_convert

def handle(resource):
    handle_resource_result = {}
    handle_resource_result['err'] = ''
    
    try:
        if resource[-4:] == '.pdf':
            handle_resource_result['convert_text'] = extract.pdf_extract_text(resource)
        elif resource[-5:] == '.docx':
            handle_resource_result['convert_text'] = extract.docx_extract_text(resource)
        elif resource[-5:] == '.xlsx':
            handle_resource_result['convert_text'] = extract.excel_extract_text(resource)
        elif resource.startswith("http"): 
            handle_resource_result['convert_text'] = extract.web_extract_text(resource)
        else:
            with open(resource, 'r', encoding='utf-8') as file:
                handle_resource_result['convert_text']= file.read()
    except Exception as e:
        handle_resource_result['err'] = 'Error: ' + str(e) + ' ❌'

    return handle_resource_result