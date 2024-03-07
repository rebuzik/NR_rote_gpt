from g4f import Provider, models
from langchain.llms.base import LLM
from data_loader.data_reader import df
from langchain_g4f import G4FLLM
from data_cleaner.text_cleaner import TextPreprocessor

from sqlalchemy.orm import sessionmaker
from create_table import Person, engine, Search_output

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

def main():
    # Предобработка текста
    preprocessor = TextPreprocessor()
    cleaned_text = preprocessor.clean_text(df)

    # Провайдеры для LLM
    providers_to_try = [Provider.FreeChatgpt, Provider.Theb, Provider.GeminiProChat, Provider.Aichat, Provider.You,
                        Provider.Liaobots, Provider.Bing, Provider.Koala, Provider.Pi]

    # Имя и день рождения абитуриента
    name = 'Азиз Антеев'
    bithday = '09.08.1996'

    # Инициализация модели LLM
    llm: LLM = G4FLLM(
        model=models.gpt_35_turbo,
        provider=providers_to_try,
    )

    # Генерация характеристики абитуриента
    res = llm(f"Напиши характеристику по основной информации из текста об абитуриенте {name},"
              f" {bithday} года рождения, собирающемся поступить в вуз: [{cleaned_text}]")
    print(res)

    # Добавление новой записи в базу данных
    new_person = Person(name=name)
    session.add(new_person)
    session.add(Search_output(text=res))
    session.commit()

    # Закрытие сессии
    session.close()

if __name__ == "__main__":
    main()