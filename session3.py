import os
import requests
import matplotlib.pyplot as pyplot
from dotenv import load_dotenv

print("hugging face project hands on session in workshop")
load_dotenv()
access_token=os.getenv("Access_Token")
API_URL="https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers={"Autherisation": f"Bearer {access_token}" }
def query(payload):
    response=requests.post(API_URL,headers=headers,json=payload)
    return response.content                         