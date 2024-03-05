from g4f import Provider, models
from langchain.llms.base import LLM
from data_loader.data_reader import df
from langchain_g4f import G4FLLM

providers_to_try = [Provider.FreeChatgpt, Provider.Theb, Provider.GeminiProChat, Provider.Aichat, Provider.You,
                    Provider.Liaobots, Provider.Bing, Provider.Koala, Provider.Pi]  # Добавьте другие провайдеры здесь
name = 'Азиз Антеев'
bithday = '09.08.1996'
def main():
    llm: LLM = G4FLLM(
        model=models.gpt_35_turbo,
        provider=providers_to_try,
    )
    res = llm(f"Напиши характеристику по основной информации из текста об абитуриенте {name}, {bithday} года рождения, собирающемся поступить в вуз: [{df}]")
    print(res)





if __name__ == "__main__":
    main()
