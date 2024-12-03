# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # O executor passa a URL do servidor, o ID da tarefa que está sendo executada,
    # o token de acesso e os parâmetros que essa tarefa recebe (quando aplicável).
    maestro = BotMaestroSDK.from_sys_args()

    # Obtenha o BotExecution com detalhes da tarefa, incluindo parâmetros
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    bot.headless = False

    bot.browser = Browser.CHROME
    bot.driver_path = bot.get_resource_abspath("chromedriver.exe")
    bot.browse("https://www.google.com.br")

    # Implement here your logic...
    
    if not bot.find( label="pesquisa", matching=0.97, waiting_time=10000):
        not_found("pesquisa") 

    bot.paste("Cotação Dólar")
    bot.enter()
    
    # valor_cotacao = bot.find_element('.SwHCTb', By.CSS_SELECTOR)
    print(bot.find_element('.SwHCTb', By.CSS_SELECTOR).text)

    # DFlfde SwHCTb

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
