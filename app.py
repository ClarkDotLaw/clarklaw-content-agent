import streamlit as st
import openai
import os

st.set_page_config(page_title="CLARK.LAW AI Content Agent", layout="centered")
st.title("CLARK.LAW AI Content Agent")
st.caption("Solutions for Growing Businesses")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Example.svg/512px-Example.svg.png", width=100)

openai.api_key = os.getenv("OPENAI_API_KEY")

content_type = st.selectbox("What would you like to generate?", ["Blog Article", "Social Media Post", "Newsletter"])
topic = st.selectbox("Choose a topic:", [
    "Med Spa Compliance", "Trademark Law", "IV Hydration Clinics",
    "Artificial Intelligence & Law", "Contract Basics",
    "Mergers & Acquisitions", "Legal Issues in Professional Disc Golf"
])

if st.button("Generate Draft"):
    with st.spinner("Generating content..."):
        try:
            prompt = f"Write a {content_type.lower()} about {topic} in the style of a modern business law firm focused on strategic, plain-English, data-driven advice. Use a professional, confident, and approachable tone. End with a call to action."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1000
            )
            output = response.choices[0].message['content']
            st.markdown("### Generated Content")
            st.text_area("Edit the draft below:", value=output, height=400)
        except Exception as e:
            st.error(f"An error occurred: {e}")
