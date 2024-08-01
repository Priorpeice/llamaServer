# LlamaServer

## 💡 프로젝트 소개

- Cps 프로젝트에 LLM Server 파트입니다.
- llama2라는 meta에서 제공한 open ai 모델을 사용했습니다.
- BackEnd : https://github.com/Priorpeice/cps
- FrontEnd : https://github.com/Priorpeice/tscps

## ⚙️ 프로젝트 개발 환경

- 프로그래밍 언어: Python
- 개발도구: Visual Studio Code
- 프레임워크: FastAPI, LlangChain

## 📚 기능

- 코드 분석 기능
    - 원래는 Fine-Tuning을 통해서 값을 직접 학습시킬예정이었습니다.
    
    하지만 데이터 셋 찾기, 올바른 코드의 정의 , 하드웨어적 문제로 우선 잠정 연기되었습니다.
    
    - 우선 사용자 코드를 분석해달라는 요청을 기본 prompt로 설정하였습니다.
    
    그리고 타 생성형 모델과 다르게 항상 같고 정형화된 값을 얻고자 top_p, temperature 값을 모두 0.1이라는 수치로 두어서 서비스를 제공합니다. 
    
    - FastAPI를 이용하여 간단한 라우팅만을 제공하여 코드를 분석하는 기능만을 수행하는 서버입니다.
