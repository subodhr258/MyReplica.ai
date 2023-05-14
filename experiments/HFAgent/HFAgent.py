from huggingface_hub import login
from transformers.tools import HfAgent
from PIL import Image
login(token="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")
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")

print(agent.run_prompt_template)
with open('run_config.txt','r') as f:
    agent.run_prompt_template = f.read()
# image = Image.open('image.png')
# image = agent.run("Draw me an image of a boat. You have been provided with an `image` if necessary.",image=image,remote=True)
# image.save("image.png","PNG")
# image = agent.run("Now transform that image to replace the boat with an elephant. You have been provided with an `image` if necessary.",image=image,remote=True)
# image.save("image.png","PNG")

# caption = agent.run("Now caption that image. You have been provided with an `image` if necessary.",image=image,remote=True)
# print("Caption:",caption)

with open("saved_text.txt","r") as f:
    text = f.read()

# agent.run("Answer this question why is Universal basic income controversial. You have been provided text in the variable `text`.",text=text,remote=True)
summary = agent.run("Summarize the text. You have been provided text in the variable `text`.",text=text,remote=True)
print(summary)



