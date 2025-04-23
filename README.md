# 🔮 Tradutor de Pergaminhos Arcanos - YouTube Transcript Summarizer

## ✨ Sobre o Projeto

Um aplicativo mágico que transforma vídeos do YouTube em pergaminhos decifrados, usando a inteligência arcana do Gemini para extrair a sabedoria essencial de qualquer conteúdo em vídeo.

**Tecnologias Utilizadas:**
- 🐍 Python 3.10+
- 🔮 Streamlit (interface mágica)
- 💎 Google Generative AI (Gemini)
- 📜 YouTube Transcript API
- 🧙‍♂️ Pytube (extração de metadados)

## 🏰 Estilo Místico

O projeto foi consagrado com:
- Temática medieval de magia e alquimia
- Cores arcanas (roxos profundos e dourados)
- Ícones místicos (cristais, pergaminhos, poções)
- Linguagem temática (rituais, invocações, feitiços)
- Efeitos visuais de grimório antigo

## 🧙‍♂️ Como Invocar o Aplicativo

### Pré-requisitos
- Python 3.10 ou superior
- Conta no Google Cloud com API do Gemini ativada
- Chave API do Gemini (armazenada no arquivo `.env`)

## Você pode colocar a URL do video desejado como esse exemplo
```
video_url = st.text_input(
        "Insira o Link do Pergaminho Visual:",
        "https://www.youtube.com/watch?v=TX9qSaGXFyg",
        help="O pergaminho deve ser um URL válido do YouTube"
    )
```



### Passos do Ritual

1. **Clonar o Grimório:**
   git clone https://github.com/seu-usuario/tradutor-pergaminhos.git
   entre no diretório

2. **Entrar no Grimório:**
   Coloque no terminal
   cd Tradutor-de-Pergaminhos-Arcanos
   python -m venv venv
  .venv/bin/activate         # Linux/Mac
  .venv\Scripts\activate     # Windows

3. **Instalar requisitos:**
   pip install -r requirements.txt

4. **Configurar a Chave de Invocação:**
   Crie um arquivo .env na raiz do projeto com:
   GEMINI_API_KEY=sua_chave_secreta_aqui

5.**Invocar o Espírito do Conhecimento:**
    streamlit run src/main.py
---

⚠️ Maldições Conhecidas (Problemas Comuns)

"Os espíritos se recusam a responder": Verifique sua chave API do Gemini

"Pergaminho protegido por feitiços": O vídeo pode não ter legendas

"Círculo de invocação incompleto": Certifique-se de todos os pacotes estão instalados
