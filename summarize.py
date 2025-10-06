from ollama import chat


def summarize(text: str, prompt: str = ''):
    """
    Makes request to LLM (gemma3) to process text
    """
    model_response = chat(model='gemma3', messages=[{
        'role': 'user',
        'content': prompt,
    }])
    content = model_response['message']['content']

    return content


if __name__ == '__main__':
    initial_prompt = """
        You are my efficient AI lecture analysis assistant.
        The following text is a transcription of a lecture.
        Based on that transcription make a very short summary,
        poining out main topics and arguments (if there was any).
    """

    with open('transcription.txt') as file:
        lecture_text = file.read()

    prompt = f'{initial_prompt}\nLecture transcription:\n{lecture_text}'
    response = summarize(lecture_text, prompt)

    with open('model_response.md', 'w') as file:
        file.write(response)