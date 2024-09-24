# NULL Implementer
## Overview
**NULL Implementer** is an artificial intelligence assistant program developed to operate within the Windows CMD command-line environment. It has the capability to generate text responses for tasks such as answering questions, researching resources (which may include code files, .pdf documents, .docx files, .xlsx spreadsheets, or even content from any website URL), and creating instant images based on text ideas provided by the user. Additionally, it features a highly useful unlocker for users of the ChatGPT tool, enabling quick access to Plus functions on a standard ChatGPT account. **NULL Implementer** offers a flexible user experience directly on a command-line-only platform.

![NULL Implementer](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/main.jpg)

The **NULL Implementer** operates based on the robust foundation of the popular GitHub repository [xtekky/gpt4free](https://github.com/xtekky/gpt4free). This repository serves as a crucial core, the heart of the program, providing essential modules for its functionality and long-term development. To learn more about this repository, please refer to [here](https://github.com/xtekky/gpt4free).

## Features
- **Flexible Configuration**: Allows you to configure the data settings that the program will use to provide services to you. This includes configuring the type of browser used to collect cookies for AI generative purposes, the _U cookie from .bing.com for image-generating AI, the language used by AI generative text for response creation, and finally, the email address of the ChatGPT account used to unlock Plus features for that account.
- **AI Text Generation**: Handles various text generation tasks such as answering questions, researching programming code, analyzing content in .docx, .pdf, or .xlsx files, or even processing content from a web page.
- **AI Image Generation**: Allows you to submit your image idea as text, then generates an image based on your idea and returns the result as a cloud-based image link.
- **ChatGPT Plus Feature Unlocker**: Allows you to unlock and use ChatGPT Plus features on a standard account (each instance lasts between 10 - 15 minutes), simply by providing your ChatGPT account email address and the program will handle the rest.

![Features](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/features.png)

## Getting Started
To quickly start using **NULL Implementer**, follow these steps:

1. Download the latest version and add it to your Windows system path environment as described in the [Installation](#installation) section.
2. Open CMD and run the following command to configure the program quickly. You can modify any value if you are familiar with them:
    ```bash
    null-implementer config --browser firefox --bingcookie "" --lang "English"
    ```
    ![Features](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/demo_1_getting_started.png)
3. Try asking your first question:
    ```bash
    null-implementer research --prompt "Who are you?"
    ```
    ![Features](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/demo_2_getting_started.png)

[Click here to view the demo video for this section.](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/demo_1_getting_started.mp4)

## Installation
To install NULL Implementer, follow these steps:
1. **Download the Release**:
- Go to the [Releases](https://github.com/NULLCommand1/NULLImplementer/releases) page of this repository.
- Download the latest version of the `null-implementer.exe` file.
2. **Add `null-implementer.exe` to Path Environment**:
- Move the downloaded `null-implementer.exe` file to a directory that is included in the system’s PATH environment variable.
- To add this file to PATH for all users:
    - Open the **Control Panel**.
    - Go to **System and Security** > **System**.
    - Click on **Advanced system settings**.
    - In the **System Properties** window, click the **Environment Variables** button.
    - In the **System Variables** section, find the **Path** variable and click **Edit**.
    - Click **New** and add the path to the directory where you placed the `null-implementer.exe` file.
    - Click **OK** to close all dialog boxes.
3. **Verify the Installation**:
- Open a CMD window in Windows and type `null-implementer --version`. If it displays version information, then everything is set up correctly.
![Version](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/version.png)

## System Requirements
- **Operating System**: Windows 10 or later.

## Configuration
- **NULL Implementer** requires four parameters for its operation. The first parameter is `--browser`, which specifies the type of browser to be used for collecting cookies for the AI text generation model. The next parameter is `--bingcookie`, used to provide the _U cookie from the site .bing.com, which is necessary for the AI image generation model. Then, `--lang` indicates the language to be used for the AI text generation model to respond to requests. Lastly, `--gptemail` provides the email address for the ChatGPT account that will have Plus features unlocked when using the `gptunlocker` option without specifying the `--email` parameter.

- If you want to quickly use **NULL Implementer** without delving into complex configurations, you can run the following command in CMD to use the default configuration (`--browser`: `firefox`, `--bingcookie`: `empty`, `--lang`: `English`, and `--gptemail`: `project.someone@hotmail.com`):
    ```bash
    null-implementer config
    ```
    ![Config Default](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/config_default.png)

- If you prefer to use **NULL Implementer** with your own custom configuration (make sure you understand it and know what you’re doing), simply pass the corresponding arguments:
    ```bash
    null-implementer config --browser [your_browser_type] --bingcookie [your_bing_cookie] --lang [your_language] --gptemail [your_email_gpt_account]
    ```
    ![Config Detail](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/config_detail.png)
- Note: You need to fully configure the **NULL Implementer** before using it to perform any tasks. You can either run the command using the default configuration quickly or configure it fully according to your own preferences.

## How to Use

### `research` Option
- If you simply have a question or an inquiry that needs answering, open the Windows CMD and enter the following command to request the AI to generate text that addresses it. The text-generating AI will utilize its extensive knowledge base combined with real-time internet data access to assist you:
    ```bash
    null-implementer research --prompt "questions_you_need_answered"
    ```
    ![Simple Research](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/simple_research_1.png)
[Click here to view the demo video for this section.](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/simple_research_1.mp4)

- You can provide a text file (.txt, .docx, .pdf, ...) or source code (.html, .js, .py, ...) by specifying its path on your local machine or its cloud link using `--resource` after the `research` option. Then, request the AI to address a question related to the provided resource as follows:
    ```bash
    null-implementer research --resource [your_path_pdf] [your_path_docx] ... --prompt "questions_you_need_answered"
    ```
    ![Resource Research](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/resource_research_1.png)

    [Click here to view the demo video for this section.](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/resource_research_1.mp4)

- You can also provide a cloud resource, such as a website or a cloud link, as long as it is accessible through a browser. Then, request the AI to address a question related to that cloud resource as follows:
    ```bash
    null-implementer research --resource [your_url_1] [your_url_2] ... --prompt "questions_you_need_answered"
    ```
    ![Web Research](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/web_research_1.png)

    [Click here to view the demo video for this section.](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/web_research_1.mp4)

- For a general case that can apply to the previously mentioned scenarios, when your question is quite complex and cannot be directly expressed in a single CMD line, you can enter the question into a text file (.txt) (e.g., `question.txt`) and then execute the following command:
    ```bash
    null-implementer research --resource [your_url_1] [your_url_2] ... --prompt "your_path_question_txt"
    ```
    ![Question File](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/question_file_1.png)

    [Click here to view the demo video for this section.](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/question_file_1.mp4)
### `imager` Option
- You can provide an idea for the image you want to create and let **NULL Implementer**'s AI image generator handle the rest:
    ```bash
    null_implementer imager --prompt "your_image_idea"
    ```
    ![Imager Demo](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/imager_demo.png)
    [Click here to watch the demo video for this feature.](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/imager_demo.mp4)
### `gptunlocker` Option

- You have a regular ChatGPT account and you want to access the Plus features, but your financial situation doesn't allow it. Provide **NULL Implementer** with your ChatGPT account email address and let it unlock the Plus features for you by executing the following command:
    ```bash
    null-implementer gptunlocker --email "your_email_gpt_account"
    ```
    ![GPT Plus Unlocker](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/gptunlocker_demo.png)
    [Click here to view the demo video for this section.](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/gptunlocker_demo.mp4)

- You can omit the `--email` parameter, in which case **NULL Implementer** will use the default value configured in the `config` option. Execute the following command:
    ```bash
    null-implementer gptunlocker 
    ```
    ![GPT Plus Unlocker](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/gptunlocker_demo_1.png)
    [Click here to view the demo video for this section.](https://nullcommand1.github.io/NULLCommand1/NULLImplementer-DemoResources/gptunlocker_demo_1.mp4)