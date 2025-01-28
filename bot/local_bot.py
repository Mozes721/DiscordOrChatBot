import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.bart_llm import BartLLM

class LocalBot:
    def __init__(self) -> None:
        self.initialize_session_state()
        self.bart_llm = BartLLM()
        st.title("Simple chat")

    def initialize_session_state(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def classify_query(self, query: str) -> str:
        """
        Classify the user's query and return the category.
        """
        category = self.bart_llm.classify_query(query)
        return f"Query classified as: {category}"

    def display_chat_history(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def get_user_input(self):
        return st.chat_input("What is up?")

    def run(self):
        self.display_chat_history()

        if prompt := self.get_user_input():
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Classify the query and generate a response
            response = self.classify_query(prompt)
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    bot = LocalBot()
    bot.run()