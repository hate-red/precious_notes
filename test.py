import whisper
from razdel import sentenize


model = whisper.load_model('medium')

transcribed = model.transcribe('audio.wav', language='ru')
sentences = [sentence.text for sentence in sentenize(transcribed['text'])]

with open('transcription2.txt', 'w') as file:
    for sentence in sentences:
        file.write(sentence)
        file.write('\n')
