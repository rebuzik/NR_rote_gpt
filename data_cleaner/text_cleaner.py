import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')


class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.punctuation = set(string.punctuation)

    def clean_text(self, text):
        # Удаление символов пунктуации
        text = text.lower()
        text = ''.join([char for char in text if char not in self.punctuation])

        # Токенизация текста
        tokens = word_tokenize(text)

        # Удаление стоп-слов
        tokens = [word for word in tokens if word not in self.stop_words]

        # Удаление чисел и специальных символов
        tokens = [word for word in tokens if word.isalpha()]

        # Лемматизация (приведение слов к их базовой форме)
        lemmatizer = nltk.stem.WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]

        # Объединение токенов в строку
        clean_text = ' '.join(tokens)

        return clean_text


# # Пример использования
# text = "This is an example sentence, with some numbers like 123 and punctuation!"
# preprocessor = TextPreprocessor()
# cleaned_text = preprocessor.clean_text(text)
# print("Cleaned text:", cleaned_text)
