import streamlit as st
import requests

import streamlit as st
import requests
import os

def send_tweet_to_backend(tweet_text):
    url = st.secrets["MAKE_URL"]
    payload = {'tweet': tweet_text}
    try:
        response = requests.post(url, json=payload, timeout=10)  # Adjust timeout as needed
        response.raise_for_status()  # Raise exception for 4xx or 5xx status codes
        return response.json()
    except requests.Timeout:
        return {"error": "Timeout occurred while waiting for response from the backend."}
    except requests.RequestException as e:
        return {"error": f"Error occurred: {str(e)}"}
    except ValueError:
        return {"error": "Empty or invalid response from the backend."}

# Rest of the code remains the same...

def display_response(response):
    if "error" in response:
        st.error(f"Enter valid twitter string \n error: {response}")
        return

    score = response['score']
    status = response['status']
    question = response['Question']

    st.write(f"Search complete:")
    # st.write(f"Status: {status}")
    # st.write(f"Question: {question_answer}")
    if status == 'found':
        st.write("Question posted 👉:", question)
    elif status == 'irrelevent':
        st.write("No relevant question found.")
    else:
        st.write("Invalid status")

def main():
    st.title("Tweet Analyzer")

    tweet_input = st.text_area("Enter the tweet:")
    if st.button("Submit"):
        if tweet_input:
            with st.spinner("Analyzing tweet..."):
                response = send_tweet_to_backend(tweet_input)
            display_response(response)

if __name__ == "__main__":
    main()
