try:
    import google.generativeai as genai
except ImportError:
    raise ImportError("Pacote 'google-generativeai' não encontrado. Instale com: pip install google-generativeai")

import os
from dotenv import load_dotenv

load_dotenv()

def configure_gemini():
    """Configura a API Gemini com a chave da API"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("A chave da API Gemini não foi encontrada na variável de ambiente GEMINI_API_KEY.")
    
    genai.configure(api_key=api_key)

def generate_summary(text, prompt="Gere um resumo conciso do texto a seguir:"):
    """Gera um resumo do texto usando a API Gemini."""
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')  # Alterado para modelo mais estável
        response = model.generate_content(prompt + "\n" + text)
        return response.text
    except Exception as e:
        print(f"Erro ao gerar o resumo: {e}")
        return None