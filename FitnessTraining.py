import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

st.title("Fitness Training App")
st.header("Enter Your Fitness Details")
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
goals = st.text_input("What are your fitness goals?")
fitness_level = st.selectbox("What is your current fitness level?", ["Beginner", "Intermediate", "Advanced"])
duration = st.slider("Duration of the training plan (in weeks)", 4, 8, 12)
generate_button = st.button("Generate plan")
concatenated_content=""

if not openai_api_key.startswith('sk-'):
   st.warning('Please enter your OpenAI API key!', icon='⚠')
if generate_button and openai_api_key.startswith('sk-'):
   if goals and fitness_level and duration:
      llm=ChatOpenAI(api_key=openai_api_key,temperature=0.8,model_name="gpt-3.5-turbo")
      prompt = (f"I am a {fitness_level.lower()} looking to achieve {goals} in {duration} weeks. "
                   f"Can you provide me with a detailed weekly fitness training plan?")
      st.write(prompt)
      response = llm.stream(prompt)
      print(type(response))
      st.write(f"{response}")
   else:
      st.error("Please provide all the required information.")
