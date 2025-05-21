"""This file contains some useful functions and data."""

from openai import OpenAI, OpenAIError
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def get_gpt_response(prompt: str, client: OpenAI) -> str:
    """
    Function, that gives two arguments:
    Prompt - User question/statement.
    Client - OpenAI client.

    Function uses ChatGPT API for answering to user prompt.
    Return GPT answer.

    :param prompt:
    :param client:
    :return str:
    """
    tries = 5
    while tries:
        try:
            completion = client.chat.completions.create(
                model='gpt-4o',
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
            break
        except OpenAIError:
            tries -= 1
            continue

    if not tries:
        return 'В данный момент наш ассистент находится на техническом перерыве. Обратитесь в наш центр.'
    return completion.choices[0].message.content


def get_embedding(text, client):
    """
    Function creates embedding based on given text and returns it.
    """
    embedding = client.embeddings.create(
      model="text-embedding-ada-002",
      input=text,
      encoding_format="float"
    )
    return embedding.data[0].embedding


def search_with_embeddings(query, texts, client):
    """
    Function searches the most relevant text based on cosine similarity of embeddings.
    """
    # Get embedding for query.
    query_embedding = get_embedding(query, client)
    print(query_embedding)

    # Get embeddings for every given text.
    text_embeddings = [get_embedding(text, client) for text in texts]

    # Calculate cosine similarity.
    similarities = cosine_similarity([query_embedding], text_embeddings)[0]

    # Find the best index of texts with maximum similarity.
    best_match_index = np.argmax(similarities)
    return texts[best_match_index], similarities[best_match_index]


# Usage example:

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
