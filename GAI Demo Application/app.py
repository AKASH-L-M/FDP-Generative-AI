# python -m venv .test (Only once to create new)
# Press Shift + Control + P to open the Command Palette and click on the Python: Select Interpreter.
# .test\Scripts\activate.ps1

# Deactivate the virtual environment using the command:deactivate

"""
# Run in terminal

.test\Scripts\activate.ps1
python -m pip install gradio
python -m pip install torch torchvision
python app.py

"""
from transformers import pipeline
import gradio as gr

# Define the text generation pipeline
pipe = pipeline("text-generation", model="openai-community/gpt2")

# Function to generate text based on user input
def generate_text(input_text):
    generated_text = pipe(input_text, max_length=50, do_sample=True, temperature=0.7)
    return generated_text[0]['generated_text']

# Create Gradio interface
iface = gr.Interface(fn=generate_text, inputs="text", outputs="text", title="Text Generation",
                     description="Enter a text prompt and see AI's response.")
iface.launch(share=True)


