import requests
import json

async def process_request(question: str):
    url = "http://localhost:11434/api/generate"
    prompt=question + "Please explain the purpose and functionality of the given code in korean."
    data = {
        "model": "llama3",
        "prompt": prompt
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print('Success')
    else:
        print("Error:", response.status_code, response.text)
        # 개별 JSON 객체로 분할
    json_objects = response.content.decode().strip().split("\n")

    # 각 JSON 객체를 Python 사전으로 변환
    data = [json.loads(obj) for obj in json_objects]
    res_text = ''
    # 변환된 데이터 출력
    for item in data:
        res_text += item['response']
    print(res_text)
    return res_text

        
