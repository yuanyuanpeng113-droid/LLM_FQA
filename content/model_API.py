import openai
from openai import OpenAI
import socket
import time
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
# sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))

def model_run(model_name, prompt):
    time_total = 0
    while True:
        try:
            response = model_api_call(model_name, prompt)
            break
        except Exception as e:
            time.sleep(20)
            time_total = time_total + 1
            if time_total>5:
                break
    return response

def model_api_call(model_name, prompt):
    if model_name == "Yi-1.5-9B-Chat-16K":
        # print('==============================')
        # print(prompt)
        API_KEY="sk-bwucfycjdlgarxjrohvbmmcjdlnmwsidycnwfrnkmdrpenzz",
        API_BASE="https://api.siliconflow.cn/v1",
        # API_BASE = "https://api.lingyiwanwu.com/v1"
        # API_KEY = "f1715743f62343fea132f873111a3c44"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        
        completion = client.chat.completions.create(
            model = "01-ai/Yi-1.5-9B-Chat-16K",
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
        # print('==============================')
        # print(response)
    elif model_name == "gemma-2-9b-it":   
        openai = OpenAI(
            api_key="8KddykfDkJPkHwUZ0lekxXEYMcJ2lVtM",
            base_url="https://api.deepinfra.com/v1/openai",
            )
        chat_completion = openai.chat.completions.create(
            model="google/gemma-2-9b-it",
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}],
            )
        response = chat_completion.choices[0].message.content
    elif model_name == "WizardLM-2-7B":   
        openai = OpenAI(
            api_key="8KddykfDkJPkHwUZ0lekxXEYMcJ2lVtM",
            base_url="https://api.deepinfra.com/v1/openai",
            )
        chat_completion = openai.chat.completions.create(
            model="microsoft/WizardLM-2-7B",
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}],
            )
        response = chat_completion.choices[0].message.content
    elif model_name == "Meta-Llama-3.1-8B-Instruct":   
        openai = OpenAI(
            # api_key="sk-bwucfycjdlgarxjrohvbmmcjdlnmwsidycnwfrnkmdrpenzz",
            # base_url="https://api.siliconflow.cn/v1",
            api_key="8KddykfDkJPkHwUZ0lekxXEYMcJ2lVtM",
            base_url="https://api.deepinfra.com/v1/openai",
            )
        chat_completion = openai.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct",
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}],
            )
        response = chat_completion.choices[0].message.content
    elif model_name == "deepseek-chat":
        API_BASE = "https://api.deepseek.com"
        API_KEY = "sk-825702af768b42fbbb8dfcccc1216e18"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
    elif model_name == "Qwen/Qwen2-7B-Instruct":
        API_BASE = "https://api.siliconflow.cn/v1"
        API_KEY = "sk-wlyagmcadnehxxofddguvwtfngphbigvbshaufpwsysiihrj"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
    elif model_name == "Qwen/Qwen2-1.5B-Instruct":
        API_BASE = "https://api.siliconflow.cn/v1"
        API_KEY = "sk-wlyagmcadnehxxofddguvwtfngphbigvbshaufpwsysiihrj"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
    elif model_name == "Qwen/Qwen1.5-7B-Chat":
        API_BASE = "https://api.siliconflow.cn/v1"
        API_KEY = "sk-wlyagmcadnehxxofddguvwtfngphbigvbshaufpwsysiihrj"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
    elif model_name == "gpt-3.5-turbo":
        API_BASE = "https://zmgpt.cc/v1"
        API_KEY = "sk-ulbb89vmBvK9MLf30b82B3973f9b45C0A3F00b82E7886eE1"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
        
    elif model_name == "gpt-4o-mini":
        API_BASE = "https://zmgpt.cc/v1"
        API_KEY = "sk-ulbb89vmBvK9MLf30b82B3973f9b45C0A3F00b82E7886eE1"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
        
    elif model_name == "THUDM/glm-4-9b-chat":
        API_BASE = "https://api.siliconflow.cn/v1"
        API_KEY = "sk-wlyagmcadnehxxofddguvwtfngphbigvbshaufpwsysiihrj"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
    elif model_name == "THUDM/chatglm3-6b":
        API_BASE = "https://api.siliconflow.cn/v1"
        API_KEY = "sk-wlyagmcadnehxxofddguvwtfngphbigvbshaufpwsysiihrj"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
    elif model_name == "Pro/google/gemma-2-9b-it":
        API_BASE = "https://api.siliconflow.cn/v1"
        API_KEY = "sk-wlyagmcadnehxxofddguvwtfngphbigvbshaufpwsysiihrj"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content
    # Assume openai>=1.0.0
    elif model_name == "meta-llama/Meta-Llama-3-8B-Instruct":
        # Create an OpenAI client with your deepinfra token and endpoint
        openai = OpenAI(
            api_key="8KddykfDkJPkHwUZ0lekxXEYMcJ2lVtM",
            base_url="https://api.deepinfra.com/v1/openai",
        )
        completion = openai.chat.completions.create(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": "Hello"}],
        )
        response = completion.choices[0].message.content
        # Assume openai>=1.0.0
# Create an OpenAI client with your deepinfra token and endpoint
    elif model_name == "openchat/openchat-3.6-8b":
        openai = OpenAI(
            api_key="8KddykfDkJPkHwUZ0lekxXEYMcJ2lVtM",
            base_url="https://api.deepinfra.com/v1/openai",
        )

        completion = openai.chat.completions.create(
            model="openchat/openchat-3.6-8b",
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": "Hello"}],
        )
        response = completion.choices[0].message.content

    elif model_name == "llama3-70b-8192":
        API_BASE = "https://api.agicto.cn/v1"
        API_KEY = "sk-ItWYrqpit7PISgmRQFWYj31vgpcFBuP7XfOnOvGOaHitiraE"
        client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE
        )
        completion = client.chat.completions.create(
            model = model_name,
            temperature = 0.1,
            top_p=0.95,
            messages=[{"role": "user", "content": prompt}]
        )
        # print('--------------------')
        # print(completion)
        response = completion.choices[0].message.content

    else:
        print("error!!!")
        return
    return response

if __name__=='__main__':
    model_name = "THUDM/chatglm3-6b"
    # model_name = "deepseek-chat"
    prompt = "你好"
    response = model_run(model_name, prompt)
    print('--------------------')
    print(response)
    




