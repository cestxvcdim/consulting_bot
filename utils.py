"""
This file contains some useful functions and data.
"""

from openai import OpenAI, OpenAIError
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# all links that use in the project
URLS = {
    'kc_base': 'https://xn--80adxqo3a.xn--p1ai/state/G_%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B/E_%D0%9D%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE-%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%B1%D0%B0%D0%B7%D0%B0',
    'consulting_appointment': 'https://xn--80adxqo3a.xn--p1ai/#segment_30',
    'portal': 'https://xn--80aidamjr3akke.xn--p1ai/',
    'yandex_form': 'https://forms.yandex.ru/u/672e5bb584227c79f8f9cc95/',
    'feedback_to_consultant': 'https://xn--80adxqo3a.xn--p1ai/review'
}

# all callback data that handle in the project after pressing buttons
CB_DATA = {
    'allowance': 'Пособие для родителей',
    'article1': 'Агрессивный ребенок',
    'article2': 'Давай дружить',
    'article3': 'Дети и гаджеты',
    'article4': 'Дизграфия',
    'article5': 'Как воспитать в ребенке здоровую уверенность',
    'article6': 'Как помочь подростку',
    'article7': 'Мой ребенок готов к школе',
    'article8': 'Причины самоповреждающего поведения',
    'article9': 'Ребенок остро реагирует на критику',
    'article10': 'Роль отца в воспитании девочки',
    'article11': 'Что такое психосоматика'
}

def get_gpt_response(prompt: str, client: OpenAI) -> str:
    '''
    Function, that gives two arguments:
    Prompt - User question/statement.
    Client - OpenAI client.

    Function uses ChatGPT API for answering to user prompt.
    Return GPT answer.

    :param prompt:
    :param client:
    :return str:
    '''
    is_answered = False
    while not is_answered:
        try:
            completion = client.chat.completions.create(
                model='gpt-4o-mini',
                max_tokens=500,
                temperature=0.9,
                messages=[
                    {"role": "system", "content": "Ты - консультант по оказанию психолого – педагогической, методической и консультативной помощи родителям (законным представителям) детей, а так же гражданам, желающим принять на воспитание в свои семьи детей, оставшихся без попечения родителей."},
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            is_answered = True
        except OpenAIError:
            continue
    return completion.choices[0].message.content


def get_embedding(text, client):
    '''
    Function creates embedding based on given text and return it.
    '''
    embedding = client.embeddings.create(
      model="text-embedding-ada-002",
      input=text,
      encoding_format="float"
    )
    return embedding.data[0].embedding


def search_with_embeddings(query, texts, client):
    '''
    Function searches the most relevant text based on cosine similarity of embeddings.
    '''
    # get embedding for query
    query_embedding = get_embedding(query, client)
    print(query_embedding)

    # get embeddings for every given text.
    text_embeddings = [get_embedding(text, client) for text in texts]

    # calculate cosine similarity
    similarities = cosine_similarity([query_embedding], text_embeddings)[0]

    # Find the best index of texts with maximum similarity.
    best_match_index = np.argmax(similarities)
    return texts[best_match_index], similarities[best_match_index]


# Usage example

# if __name__ == "__main__":
#     texts = [
#         "Машинное обучение — это область искусственного интеллекта.",
#         "Программирование на Python становится все популярнее.",
#         "GPT-3 — это мощная языковая модель для обработки текста."
#     ]
#
#     query = "Что такое GPT-3?"
#     best_text, similarity = search_with_embeddings(query, texts, client)
#     print(f"Наиболее релевантный текст: {best_text}")
#     print(f"Сходство: {similarity}")
