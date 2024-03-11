from g4f import Provider, models
from langchain.llms.base import LLM
from data_loader.data_reader import df
from langchain_g4f import G4FLLM
from data_cleaner.text_cleaner import TextPreprocessor
import pandas as pd


# from sqlalchemy.orm import sessionmaker
# from create_table import Person, engine, Search_output


def main():
    # Предобработка текста
    preprocessor = TextPreprocessor()
    cleaned_text = preprocessor.clean_text(df)

    # Провайдеры для LLM
    providers_to_try = [Provider.Theb, Provider.GeminiProChat, Provider.Aichat, Provider.You,
                        Provider.Liaobots, Provider.Bing, Provider.Koala, Provider.Pi, Provider.FreeChatgpt]

    # Имя и день рождения абитуриента
    name = 'Азиз Антеев'
    bithday = '09.08.1996'

    # Инициализация модели LLM
    llm: LLM = G4FLLM(
        model=models.gpt_35_turbo,
        provider=providers_to_try,
    )

    # Генерация характеристик абитуриента
    res = llm(f"Напиши характеристику об абитуриенте {name} по основной информации из текста,"
              f" {bithday} года рождения, собирающемся поступить в вуз: [{cleaned_text}]")

    vk_data = pd.read_excel('../data/NR_vk_id.xlsx').iloc[0, :]
    res_data = llm(f"Обобщи и объедини информацию о человеке, ссылки при анализе не используй. Данные из социальной"
                   f" сети[{vk_data}] и данные из поисковой выдачи [{res}]")
    output_predisposition = llm(f'По имеющейся информации определи предрасположен человек к техническому или '
                                f'гумманитарному направлению, для выбора направления обучения. Данные: {res_data}')

    print(output_predisposition)

    # Добавление новой записи в базу данных
    # new_person = Person(name=name)
    # session.add(new_person)
    # session.add(Search_output(text=res))
    # session.commit()
    #
    # Закрытие сессии
    # session.close()


if __name__ == "__main__":
    main()
