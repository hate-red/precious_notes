from faster_whisper import WhisperModel
from razdel import sentenize


def transcribe(audio: str, model_size: str = 'base'):
    """
    Makes transcription from audio to text
    """
    model = WhisperModel(model_size, device='cpu', compute_type='int8')
    segments, _ = model.transcribe(audio, beam_size=5)
    text = ''.join(segment.text for segment in segments)

    return text


if __name__ == '__main__':
    lecture_text = transcribe('audio.mp3')
    sentences = [sentence.text for sentence in sentenize(lecture_text)]

    with open('transcription.txt', 'w') as file:
        for sentence in sentences:
            file.write(sentence + '\n')
