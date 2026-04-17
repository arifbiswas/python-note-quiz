from gtts import gTTS
import io


def TTV(text) :
    speech = gTTS(text,lang="en",slow=False)
    
    audio_buffer = io.BytesIO()
    
    speech.write_to_fp(audio_buffer)

    return audio_buffer

