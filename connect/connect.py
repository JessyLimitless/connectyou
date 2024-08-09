import openai
import streamlit as st

# Streamlit 페이지 설정
st.set_page_config(page_title="OPEN AI")
st.title('OPEN AI')
st.markdown("<p style='font-size: 20px; font-weight: bold; font-family: Arial, sans-serif;'>챗봇은 누구나 만들 수 있습니다. 😊</p>", unsafe_allow_html=True)

# API 키 입력 필드
api_key = st.text_input("OpenAI API 키를 입력하세요:", type="password")

def generate_response(input_text, api_key):  # LLM이 답변 생성
    openai.api_key = api_key  # API 키 설정

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 모델명
        messages=[{"role": "user", "content": input_text}],  # 메시지 생성
        temperature=0.99  # 창의성 설정
    )
    
    return response['choices'][0]['message']['content']  # 응답 반환

if api_key:
    # 환영 인사
    st.markdown("<p style='font-size: 20px; font-weight: bold; font-family: Arial, sans-serif;'>환영합니다! 이제 질문을 입력할 수 있습니다.</p>", unsafe_allow_html=True)
    
    # Streamlit 폼 사용
    with st.form('Question'):
        text = st.text_area('질문 입력:', '')  # 첫 페이지가 실행될 때 보여줄 질문
        submitted = st.form_submit_button('보내기')
        if submitted:
            response = generate_response(text, api_key)  # 폼 제출 시 응답 생성
            st.info(response)  # 응답 출력
else:
    st.warning("OpenAI API 키를 입력해주세요.")
