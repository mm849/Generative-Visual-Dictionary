import openai
import gradio as gr
from dotenv import load_dotenv
load_dotenv()
import os

openai_api_key = os.environ['OPENAI_API_KEY']
openai.api_key = openai_api_key

messages=[
    {
        "role": "system",
        "content": "You are a English teacher. If you get an English word, return its meaning and list 3 example sentences which use the word."
    }
]

def chatbot(input):
    if input:
        messages.append({
            "role": "user",
            "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({
            "role": "assistant",
            "content": reply
            })
        return reply
    
inputs = gr.inputs.Textbox(lines=1, label="Put an English word")
outputs = gr.outputs.Textbox(label="Meaning & Example sentences")

gr.Interface(
    fn=chatbot, 
    inputs=inputs, 
    outputs=outputs, 
    title="Dictionary with example sentences",
    description="Ask anything you want",
    theme="compact"
    ).launch()