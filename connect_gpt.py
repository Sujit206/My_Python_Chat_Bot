
import streamlit as st
from google import genai

api_keys = "AIzaSyCse6MvPeXMlTAGLmt7C3JCJAHmqqNh3wc"

def query(user_query):


    my_ai = genai.Client(api_key= api_keys)

    response = my_ai.models.generate_content(model="gemini-3-flash-preview", contents= user_query)

    return response.text

st.title("Python Chat Bot")

if 'message' not in st.session_state:
    st.session_state.message = []

for i in st.session_state.message:
    with st.chat_message(i["role"]):
        st.markdown(i["msg"])


user_input = st.chat_input("Enter your query!")

if user_input:
    st.session_state.message.append({
        "role" : "user",
        "msg" : user_input
    })
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("thinking.."):
            result = query(user_input)
            st.markdown(result)

    st.session_state.message.append({
        "role" : "assistant",
        "msg" : result
    })