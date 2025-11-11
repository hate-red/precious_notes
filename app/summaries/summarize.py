from ollama import chat


def summarize(text: str):
    """
    Makes request to LLM (gemma3) to process text
    """
    initial_prompt = 'Summarize the following text by outlining key ideas. ' \
                     'Do not write your opinion, ' \
                     'only use what was provided in the text \n\n'
    model_response = chat(
        model='gemma3', 
        messages=[{
            'role': 'user',
            'content': initial_prompt + text,
        }],
    )
    content = model_response['message']['content']

    return content
