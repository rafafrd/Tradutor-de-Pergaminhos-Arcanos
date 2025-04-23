import sys
import os
import streamlit as st
import youtube_utils
import gemini_utils

# Configuração do tema místico
st.set_page_config(
    page_title="Tradutor de Pergaminhos Arcanos",
    page_icon="🔮",
    layout="wide"
)

# CORREÇÃO AQUI: Faltava um parêntese no os.path.join()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# CSS personalizado para o tema de magos
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap');
    
    .main {
        background-image: url('https://i.imgur.com/X6QX0yT.jpg');
        background-size: cover;
    }
    
    .stApp {
        background-color: rgba(10, 5, 30, 0.9);
        color: #e0d0b0;
        font-family: 'MedievalSharp', cursive;
    }
    
    .stTextInput>div>div>input {
        background-color: #1a0d2b;
        color: #e0d0b0;
        border: 1px solid #5a3a7a;
    }
    
    .stButton>button {
        background-color: #3a1d5d;
        color: #f0e0b0;
        border: 1px solid #7a5a9a;
        font-family: 'MedievalSharp', cursive;
        font-size: 1.1em;
        border-radius: 5px;
    }
    
    .stButton>button:hover {
        background-color: #5a3a7a;
        color: #ffedc2;
        border: 1px solid #9a7aba;
    }
    
    h1, h2, h3 {
        color: #d4af37 !important;
        text-shadow: 2px 2px 4px #000000;
    }
    
    .error {
        color: #ff6b6b !important;
        font-weight: bold;
    }
    
    .success {
        color: #a0e0a0 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Cabeçalho místico
    st.markdown("""
    <div style="text-align: center;">
        <h1>🔮 Tradutor de Pergaminhos Arcanos 🔮</h1>
        <p style="font-size: 1.2em;">Desvende os segredos dos pergaminhos de vídeo com o poder do Cristal de Gemini</p>
        <hr style="border-top: 1px solid #5a3a7a;">
    </div>
    """, unsafe_allow_html=True)

    # Input de URL estilizado
    video_url = st.text_input(
        "Insira o Link do Pergaminho Visual:",
        "https://www.youtube.com/watch?v=TX9qSaGXFyg",
        help="O pergaminho deve ser um URL válido do YouTube"
    )

    if video_url:
        try:
            # Processamento do vídeo com mensagens temáticas
            with st.spinner('Consultando os arquivos arcanos...'):
                video_id = youtube_utils.extract_video_id(video_url)
                video_title = youtube_utils.get_video_title(video_url)
                transcript = youtube_utils.get_transcript(video_id)

            if video_title:
                st.markdown(f"""
                <div style="background-color: rgba(58, 29, 93, 0.5); padding: 15px; border-radius: 10px; border-left: 5px solid #d4af37;">
                    <h3>📜 Título do Pergaminho: <span class="success">{video_title}</span></h3>
                </div>
                """, unsafe_allow_html=True)
            
            if transcript:
                with st.expander("📜 Conteúdo Decifrado do Pergaminho", expanded=False):
                    st.write(transcript)

                if st.button("🔮 Invocar Sabedoria de Gemini", key="summarize"):
                    try:
                        with st.spinner('Convocando os espíritos do conhecimento...'):
                            gemini_utils.configure_gemini()
                            summary = gemini_utils.generate_summary(transcript)
                        
                        if summary:
                            st.markdown("""
                            <div style="background-color: rgba(90, 58, 122, 0.5); padding: 15px; border-radius: 10px; margin-top: 20px; border-left: 5px solid #d4af37;">
                                <h3>✨ Sabedoria Revelada:</h3>
                            </div>
                            """, unsafe_allow_html=True)
                            st.write(summary)
                        else:
                            st.error("Os espíritos do conhecimento se recusaram a responder...", icon="⚠️")
                    except Exception as e:
                        st.error(f"O círculo de invocação falhou: {str(e)}", icon="❌")
            else:
                st.error("O pergaminho está protegido por feitiços antigos... não foi possível decifrar.", icon="🔒")

        except Exception as e:
            st.error(f"Uma maldição interferiu no ritual: {str(e)}", icon="☠️")

if __name__ == "__main__":
    main()