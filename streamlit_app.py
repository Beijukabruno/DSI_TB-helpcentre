import streamlit as st
import requests

API_URL = "http://localhost:8001"  # Update if running elsewhere

st.set_page_config(page_title="TB Help Centre Chatbot", layout="centered")
st.title("TB Help Centre Chatbot")

# Chat Section
st.header("Chat with the Bot")
user_input = st.text_input("Type your question:")
if st.button("Send"):
    if user_input:
        try:
            response = requests.post(f"{API_URL}/chat", json={"query": user_input})
            if response.status_code == 200:
                data = response.json()
                answer = data.get("answer", "No answer returned.")
                st.success(answer)
                sources = data.get("sources", [])
                if sources:
                    st.markdown("**Sources:**")
                    for src in sources:
                        header = src.get("header", "")
                        url = src.get("source_url", "")
                        if header and url:
                            st.markdown(f"- [{header}]({url})")
                        elif url:
                            st.markdown(f"- [Source Link]({url})")
                else:
                    st.info("No sources provided.")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")

# Rating Section
st.header("Rate Your Experience")
rating = st.slider("How would you rate your experience?", 1, 5, 3)
if st.button("Submit Rating"):
    try:
        response = requests.post(f"{API_URL}/rate", json={"rating": rating})
        if response.status_code == 200:
            st.success("Thank you for your feedback!")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")

# (Optional) Add more sections for search, etc., as needed.
