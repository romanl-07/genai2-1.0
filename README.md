# Chatbot Project with Generative AI

This is the README file for the Educational Chatbot Project with Generative AI (Sponsored by Infosys).

## Project Information

- **Username:** ed_chat_bot
- **Password:** EdGenAI24%  
  This password is required for installing anything on this computer.

- **Project Directory:** `/Users/ed_chat_bot/chatbot_project`
- **Command to Navigate to Project Directory:**

    cd /Users/ed_chat_bot/chatbot_project
     or
    cd ~/chatbot_project

- **Opening the Project in VSCode** : I've downloaded the VSCode Integrated Development Environment (IDE) for you to use. To open your project directory in VSCode, follow these steps:

    1. **Open Terminal**
    2. **Navigate to the Project Directory:**
    cd ~/chatbot_project
    3. **Open the directory in VSCode**
    code .
-----------------------------------------------------------------------------------------------------------
## Activating the Virtual Environment

To ensure that the dependencies (libraries) for this project are managed properly, it's recommended to use a virtual environment. 

### What is a Virtual Environment?

A virtual environment is an isolated environment that allows you to manage dependencies for your project separately from other projects. When you create a virtual environment, it creates a unique directory containing all the necessary executables to use the packages that a Python project would need. This isolation ensures that your project’s dependencies do not interfere with other projects and vice versa.

### Why is it Important?

1. **Dependency Management:** Different projects may require different versions of the same library. Virtual environments allow you to manage these dependencies without conflicts.
2. **Isolation:** By isolating project dependencies, you ensure that changes in one project do not affect others, preventing unexpected issues.
3. **Reproducibility:** Using a virtual environment makes it easier to reproduce the project setup on different machines, as all dependencies are contained within the environment.

### Activating the Pre-Created Virtual Environment

A virtual environment has already been created for you in the project directory ~/chatbot_project. Follow these steps to activate it:

#### Step 1: Navigate to the Project Directory

First, navigate to your project directory:

    cd ~/chatbot_project

#### Step 2: To activate the virtual environment, use the following command:

    source venv/bin/activate

#### Step 3: Once the virtual environment is activated, your command shell prompt will change to show the name of the environment. For example, it will look something like this:

    (venv) ed_chat_bot@ed-chat-bots-MacBook-Air chatbot_project %

#### Step 4: When you're done working, you can deactivate the virtual environment by running: (not necessary)

    deactivate

- **Note**: you must install your required libraries for the project into the venv (pip3 install [library name] when the venv is activated)

-----------------------------------------------------------------------------------------------------------
## Installing Required Libraries
    To manage and install libraries in Python, we use a package manager called `pip`. Below are the commands to install the necessary libraries for this project.

**Streamlit is a library that allows you to create web applications for data science and machine learning projects with simple Python scripts.**
    pip3 install streamlit
**Langchain is a library that simplifies the process of interacting with large language models (LLMs) by providing a user-friendly interface and tools.**
    pip3 install langchain
**Google Generative AI is a library that enables you to access advanced language models like Gemini Pro from Google Cloud.**
    pip3 install google-generativeai
**Python Dotenv is a library that helps you manage environment variables by loading them from a .env file, which is useful for keeping sensitive information like API keys secure.**
    pip3 install python-dotenv
**You may need additional libraries as you progress in this project**

-----------------------------------------------------------------------------------------------------------

## Other Notes

    - Since this computer is only being used for this project, I did not set up a virtual environment. However, using a virtual environment is best practice in Python development. If you want any support setting up and using a virtual environment, contact Shaune at ReadyCT.
    - Let Shaune know if you need help setting up Github

## Using Environmental Variables and the .env file

    Environmental variables are a way to store configuration settings and sensitive information like API keys and passwords outside of your code. This practice enhances security and flexibility, making it easier to manage and deploy applications.

### Why Not Hard Code Credentials?

Hard coding credentials (e.g., API keys, passwords) directly in your code can lead to several security risks:
- **Exposure:** If your code is shared or uploaded to a public repository, your credentials can be exposed to unauthorized users.
- **Maintenance:** Updating credentials requires changing the code, which can be error-prone and inconvenient.
- **Security:** Hard coded credentials are vulnerable to accidental leaks and can compromise the security of your application.

### Using Environmental Variables with Python Dotenv

    The `python-dotenv` library allows you to manage environmental variables in a `.env` file and load them into your Python application.

### For example:
- **Below would be the environmental varialbe in your .evn file** 
    GEMINI_PRO_API_KEY=your_api_key_here

- **And this is how you would call it in your python file (.py)**
    gemini_pro_api_key = os.getenv('GEMINI_PRO_API_KEY')

    - see the .env file and example.py file for more info

