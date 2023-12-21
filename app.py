import streamlit as st
import openai
import os
import Together
import Anyscale

os.environ[ "OPENAI_BASE_URL"] ='https://api.endpoints.anyscale.com/v1'
# Set your OpenAI API key here
os.environ[ "together_api_key"] = "2332ed28db876b7f1a700baa5a257464381df06b99e8213b4dade9a00091caa1"
os.environ["ANYSCALE_API_KEY"] = "esecret_w2d6mtjlb4wpq4cyw3wsn8pi9e"


# Function to interact with the GPT-3.5-turbo model with tunable parameters
def generate_response(prompt, temperature=0.7, max_tokens=256, top_p=0.9, n=2, stop=None, frequency_penalty=0.9, presence_penalty=0.9, chat_history=None):
    if chat_history is None:
        chat_history = []

    messages = [
        {"role": "system", "content": "Discuss, describe and fully elaborate each point with examples as if you were a human Ugandan  University Professor helping university students pass exams. Be professional and factual. Answer based on context of question asked. Use simple english. Give more than 10 points. Fully explain and elaborate each point with an example.  Where possible give references or quotations. Examples should be relevant to uganda. Use essays with introduction, body and conclusion. Rewrite all content and answers like a human being. rephrase all content. Change the syntax and vocabulary. Recheck and verify your answers to eliminate errors, and give the most correct answer."},
        {"role": "user", "content": prompt},
    ]
    messages.extend(chat_history)
    
    client = openai.OpenAI()
    response = openai.ChatCompletion.create(
        model=""mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        n=n,
        stop=stop,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    return response['choices'][0]['message']['content']

# Streamlit app header and title
 # tattooed geek logo
logo1 = 'https://miro.medium.com/v2/resize:fit:180/1*ypRBA86IBBbZbti76vm4Hg.png'
# Streamlit app header and title
st.set_page_config(page_title="Personal ChatGPT bot | By Anish Singh Walia", page_icon=logo1 , layout="wide")


st.write("# Ai Lecturer :sunglasses: ")
st.write("Made with love")
st.write("Welcome to your personal Ai Assistant Lecturer app! Type your message below:")


# Sidebar with social profiles and model parameters
#st.sidebar.markdown("# Follow me on my Social Profiles")
#st.sidebar.markdown(
#    """<a href="https://github.com/anishsingh20" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="60px"></a>
#    <a href="https://www.linkedin.com/in/anish-singh-walia-924529103/" target="_blank"><img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="LinkedIn" width="60px"></a>
#    <a href="https://medium.com/@anishsinghwalia" target="_blank"><img src="https://cdn1.iconfinder.com/data/icons/social-media-circle-7/512/Circled_Medium_svg5-512.png" alt="Medium" width="60px"></a>
#    <a href="https://instagram.com/cali_br20" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/2048px-Instagram_logo_2016.svg.png" alt="Instagram" width="60px"></a>
#    """,
#    unsafe_allow_html=True,
#)

# HTML sidebar to fine-tune model's parameters to customize the bot's responses.
st.sidebar.markdown("# Model Parameters")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
max_tokens = st.sidebar.number_input("Max Tokens", 50, 500, 256, step=50)
top_p = st.sidebar.slider("Top P", 0.1, 1.0, 0.9, 0.1)
n = st.sidebar.number_input("N", 1, 5, 2, step=1)
stop = st.sidebar.text_input("Stop", "")
frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 1.0, 0.9, 0.1)
presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 1.0, 0.9, 0.1)

# Main app where user enters prompt and gets the response
user_input = st.text_area("You:", "", key="user_input")
generate_button = st.button("Generate Response")


# Chat history
messages = []
if user_input.strip() != "":
    messages.append({"role": "user", "content": user_input})
    response = generate_response(user_input, temperature, max_tokens, top_p, n, stop, frequency_penalty, presence_penalty)
    messages.append({"role": "assistant", "content": response})

st.subheader("Chat History")
for message in messages:
    if message["role"] == "user":
        st.text_area("You:", value=message["content"], height=50, max_chars=200, key="user_history", disabled=True)
    else:
        st.text_area("Jarvis:", value=message["content"], height=500, key="chatbot_history")

# Additional styling to make the app visually appealing
st.markdown(
    """
    <style>
        body {
            font-family: Montserrat, sans-serif;
        }
        .stTextInput>div>div>textarea {
            background-color: #f0f0f0;
            color: #000;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        .stTextArea>div>textarea {
            resize: none;
        }
        .st-subheader {
            margin-top: 20px;
            font-size: 16px;
        }
        .stTextArea>div>div>textarea {
            height: 100px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
