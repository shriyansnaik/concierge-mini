import streamlit as st
from intent import IntentClassifier
from extract import Extractor
from web_search import Internet
from follow_up import FollowUpQuestionGenerator

from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
llm = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)
classifier = IntentClassifier(llm)
extractor = Extractor(llm)
web_browser = Internet(llm)
generate_follow_up = FollowUpQuestionGenerator(llm)

st.set_page_config(page_title="Concierge Mini", page_icon="🤖")
st.title("🤖 Concierge Mini")

def pretty_json(data):
    return json.dumps(data, indent=2, ensure_ascii=False)

def process_query(query):
    intent = classifier(query)
    if intent["intent"] == "other":
        res = web_browser(query)
    else:
        res, missing_required_fields = extractor(query, intent["intent"])
        res.update(intent)
        if missing_required_fields:
            follow_up_questions = generate_follow_up(query, missing_required_fields)
            res['follow_up_questions'] = follow_up_questions
    return res

example_queries = [
    "book me a cab to swiggy office banglore from banglore airport. i need an SUV",
    "my moms birthday is coming up. i want to buy her a watch",
    "i want to visit brazil this summer",
    "Need a sunset-view table for two tonight; gluten-free menu a must",
    "i want to update my aadhar address"
]

if "user_query" not in st.session_state:
    st.session_state.user_query = ""
if "last_processed_query" not in st.session_state:
    st.session_state.last_processed_query = ""

with st.sidebar:
    st.markdown("#### Example Queries")
    for idx, example in enumerate(example_queries):
        if st.button(example, key=f"example_{idx}"):
            st.session_state.user_query = example

user_query = st.text_input("Ask me anything...", value=st.session_state.user_query, key="main_query_input")

if user_query and (user_query != st.session_state.last_processed_query):
    response = process_query(user_query)
    st.markdown("**Response:**")
    st.code(pretty_json(response), language="json")
    st.session_state.last_processed_query = user_query