from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp

async def process_request(question: str):
    # LLM 모델 경로
    model_path = "G:/llama/llama.cpp/models/llama-2-70b-chat.Q5_K_M.gguf"

    # 템플릿 설정
    template = """Input code: {question}
    
    Explanation: Please explain the purpose and functionality of the given code."""
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # 콜백 설정
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

    # LLM 초기화
    llm = LlamaCpp(
        model_path=model_path,
        input={"temperature": 0.1, "max_length": 2000, "top_p": 0.1},
        n_ctx=3584,
        n_batch=521,
        callback_manager=callback_manager,
        verbose=True,
    )

    # LLMChain 초기화
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    # 입력 prompt
    prompt = question

    # LLMChain 실행 및 응답 반환
    response = llm_chain.run(prompt)
    return response
