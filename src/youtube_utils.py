from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_title(video_url):
    """Extrai o título de um vídeo do YouTube."""
    try:
        yt = YouTube(video_url)
        return yt.title
    except Exception as e:
        print(f"Erro ao obter o título do vídeo: {e}")
        return None

def get_transcript(video_id):
    """Obtém a transcrição de um vídeo do YouTube."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([entry['text'] for entry in transcript])
    except Exception as e:
        print(f"Erro ao obter a transcrição: {e}")
        return None
  
def extract_video_id(url):
    """Extrai o ID do vídeo da URL do YouTube."""
    try:
        # Extrai o ID da URL (mais eficiente que instanciar o objeto YouTube)
        if 'youtube.com/watch?v=' in url:
            return url.split('v=')[1].split('&')[0]
        elif 'youtu.be/' in url:
            return url.split('youtu.be/')[1].split('?')[0]
        else:
            yt = YouTube(url)
            return yt.video_id
    except Exception as e:
        print(f"Erro ao extrair o ID do vídeo: {e}")
        return None