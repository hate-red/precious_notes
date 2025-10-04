from faster_whisper import WhisperModel
from razdel import sentenize

model_size = "medium"

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")

# or run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, _ = model.transcribe("audio.wav", beam_size=5)
text = ''.join(segment.text for segment in segments)
sentences = [sentence.text for sentence in sentenize(text)]

with open('transcription.txt', 'w') as file:
    for sentence in sentences:
        file.write(sentence)
        file.write('\n')
