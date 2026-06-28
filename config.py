import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Token del bot de Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# API Key de Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Modelo de Gemini
GEMINI_MODEL = "gemini-2.5-flash"

# Base de datos
DATABASE_NAME = "data/memory.db"
