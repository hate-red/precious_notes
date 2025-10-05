from faster_whisper import WhisperModel
from ollama import chat
from razdel import sentenize


def transcribe_audio(audio: str, model_size: str = 'base'):
    """
    Transcription process
    """
    model = WhisperModel(model_size, device='cpu', compute_type='int8')
    segments, _ = model.transcribe(audio, beam_size=5)
    text = ''.join(segment.text for segment in segments)

    return text


lecture_text = transcribe_audio('audio.mp3')
sentences = [sentence.text for sentence in sentenize(lecture_text)]

with open('transcription.txt', 'w') as file:
    for sentence in sentences:
        file.write(sentence + '\n')


def process_text(text: str, prompt: str = ''):
    """
    This function make request to LLM (gemma3)
    to process text
    """
    model_response = chat(model='gemma3', messages=[{
        'role': 'user',
        'content': prompt,
    }])
    content = model_response['message']['content']

    return content


initial_prompt = """
    You are my efficient AI lecture analysis assistant.
    The following text is a transcription of a lecture.
    Based on that transcription make a very short summary,
    poining out main topics and arguments (if there was any).
"""

with open('transcription.txt') as file:
    lecture_text = file.read()

prompt = f'{initial_prompt}\nLecture transcription:\n{lecture_text}'
response = process_text(lecture_text, prompt)

with open('model_response.md', 'w') as file:
    file.write(response)
