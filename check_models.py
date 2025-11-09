import google.generativeai as genai
from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

print("\n --- Checking available models --- \n")
# models = genai.list_models()
# for model in models:
#     print(f"Model ID: {model.id}, Name: {model.name}")

for model in genai.list_models():
    print(f"ModName: {model.name}")