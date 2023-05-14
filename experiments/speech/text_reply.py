from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from huggingface_hub import login
from transformers.tools import HfAgent
import keyboard
from question_audio_input import ask_ques
from question_audio_to_text import ques_speech_to_text
from speak_reply import run_speak_reply
login(token="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")
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")

with open('run_config.txt','r') as f:
    agent.run_prompt_template = f.read()

HUGGING_FACE_API_KEY = "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"
hf_embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

print("Starting check for activation...")
while True:
    if keyboard.is_pressed("w"):
        ask_ques()
        question = ques_speech_to_text()
        my_loader = DirectoryLoader('./saved_text', glob='**/*.txt')
        docs = my_loader.load()
        text_split = RecursiveCharacterTextSplitter(chunk_size = 200, chunk_overlap = 20)
        text = text_split.split_documents(docs)
        vectorstore = FAISS.from_documents(text, hf_embeddings)

        documents = vectorstore.similarity_search(question,k=2)
        documents = ' '.join([document.page_content for document in documents])
        print("documents:",documents)

        summary = agent.run("Summarize the text. You have been provided text in the variable `text`.",text=documents,remote=True)
        run_speak_reply(summary)
