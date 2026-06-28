import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

genai.configure(api_key=GEMINI_API_KEY)

modelo = genai.GenerativeModel(GEMINI_MODEL)

def preguntar(texto):
    respuesta = modelo.generate_content(texto)
    return respuesta.text
