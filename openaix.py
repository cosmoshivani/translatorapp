import os
import openai
import config

openai.api_key = config.api_key


def getLanguageTranslation(prompt, language):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Translate this into {}\n{}".format(language, prompt),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response


prompt = 'What is the time'
language = 'French'
answer = getLanguageTranslation(prompt, language)

print(answer)
