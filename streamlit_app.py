import streamlit as st

# 앱 제목 설정
st.title("가장 큰 수 찾기 앱")
st.write("세 개의 정수를 입력하면 가장 큰 수를 찾아줍니다.")

# 1. 기존의 input()을 streamlit의 number_input()으로 변경
# 기본값을 0으로 설정하고, 정수(int) 형태로 입력받도록 step=1을 설정했습니다.
num1 = st.number_input("첫 번째 숫자를 입력하세요", value=0, step=1)
num2 = st.number_input("두 번째 숫자를 입력하세요", value=0, step=1)
num3 = st.number_input("세 번째 숫자를 입력하세요", value=0, step=1)

# 계산 시작 버튼
if st.button("가장 큰 수 찾기"):
    # 2. 원본 조건문 논리 (그대로 유지)
    if num1 > num2:
        if num1 > num3:
            result = num1
        else:
            result = num3
    else:
        if num2 > num3:
            result = num2
        else:
            result = num3

    # 3. 기존의 print() 대신 streamlit의 success/write 기능을 사용해 화면에 출력
    st.success(f"가장 큰 수는 **{result}**입니다.")
