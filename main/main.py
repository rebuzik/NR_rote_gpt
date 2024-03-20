from g4f import Provider, models
from langchain.llms.base import LLM
from data_loader.data_reader import name, birthday, search_engines, eyes_of_god, vk_group, process_data
from langchain_g4f import G4FLLM
from data_cleaner.text_cleaner import TextPreprocessor
import pandas as pd


# from sqlalchemy.orm import sessionmaker
# from create_table import Person, engine, Search_output
file_path = '../data/data.json'

def main():
    # Предобработка текста
    # preprocessor = TextPreprocessor()
    # cleaned_text = preprocessor.clean_text(search_engines)
    process_data(file_path, 1)
    # Провайдеры для LLM
    providers_to_try = [Provider.Theb, Provider.GeminiProChat, Provider.Aichat, Provider.You,
                        Provider.Liaobots, Provider.Bing, Provider.Koala, Provider.Pi, Provider.FreeChatgpt]

    # Инициализация модели LLM
    llm: LLM = G4FLLM(
        model=models.gpt_35_turbo,
        provider=providers_to_try,
    )

    # Генерация характеристик абитуриента
    res = llm(f"Напиши справку о человеке {name} {birthday} года рождения по основной информации из текста , по пунктам "
              f"(фамилия, имя, отчество, дата рождения, наименование учебного заведения, текущая деятельность, Семейное положение, Знание языков программирования, "
              f"Знание программных продуктов, Спортивные разряды, Дополнительные сведения и так далее). В тексте имеются упоминания о других людях, исключи их в ответе. "
              f"Данные для анализа: [{search_engines}]")

    print("Предрасположенности по поиску:", res)

    res_data = llm(f"Раздели данный список категорий на две группы в соответствии с их тематикой: технические (включая такие области как  программирование, безопасность, дизайн и графика, военное дело, медицина, машиностроение, нефтегаз, горнодобывающие и прочие технические направления) и гуманитарные "
                   f"(включая историю, творчество, туризм и путешествия, кино, активный отдых, литературу и другие смежные области):  {vk_group}") #
    print("Группы вк", res_data)

    # output_predisposition = llm(f'По имеющейся информации определи предрасположен человек к технической или '
    #                             f'гумманитарной науке при выборе программы поступления, опиши кратко обоснование выбора. Личные данные: {res}, направления интересов в социальных сетях, при выборе направления не учитывай тематики отдыха и музыки: {res_data}')
    # output_predisposition = llm(f'Используя имеющиеся данные, определите склонность человека к гуманитарным или техническим наукам. Учитывайте факторы, такие как предыдущий образовательный и профессиональный опыт, интересы, а также выполненные работы или проекты. Опиши кратко обоснование выбора. данные: {res}, направления интересов в социальных сетях, при выборе направления не учитывай тематики отдыха и музыки: {res_data}')
    output_predisposition = llm(f'На основе имеющихся данных, предположи склонность человека к гуманитарной или технической области. Для анализа используй интересы человека. Пример ожидаемого ответа ("Вы гуманитарий", либо "Вы технарь"). Данные для анализа: {res}, {res_data}')

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
