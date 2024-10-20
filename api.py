from fastapi import FastAPI, HTTPException
# from llamacpp import process_request
from ollama import process_request
app = FastAPI()

# # FastAPI에서 POST 요청 처리를 위한 endpoint 설정
# @app.post("/api/verification")
# async def call_llama(data: dict):
#     # POST 요청에서 question 데이터를 받아옴
#     question = data.get("question")
#     print(question)
#     if not question:
#         raise HTTPException(status_code=400, detail="Question data not provided")

#     # POST 요청을 llamacpp 모듈의 함수로 전달하여 처리
#     response = await process_request(question)
#     return {"response": response}

# FastAPI에서 POST 요청 처리를 위한 endpoint 설정
@app.post("/api/verification")
async def call_llama(data: dict):
    # POST 요청에서 question 데이터를 받아옴
    question = data.get("question")
    print(question)
    if not question:
        raise HTTPException(status_code=400, detail="Question data not provided")

    # POST 요청을 llamacpp 모듈의 함수로 전달하여 처리
    response = await process_request (question)
    return {"response":response}
