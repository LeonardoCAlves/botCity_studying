from botcity.web import WebBot, Browser, By
from botcity.maestro import *
import pandas as pd

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False

    bot.browser = Browser.CHROME

    try:
        bot.driver_path = bot.get_resource_abspath('chromedriver.exe')
    except Exception:
        from webdriver_manager.chrome import ChromeDriverManager
        import os
        import shutil

        shutil.move(
            ChromeDriverManager().install(), 
            os.path.join(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)
                    ), 'resources'
                ), "chromedriver.exe"
            )
        )
        bot.driver_path = bot.get_resource_abspath('chromedriver.exe')

    bot.browse("https://www.casasbahia.com.br/")

    if bot.find( "pesquisa", matching=0.97, waiting_time=1000):
       bot.click()

    bot.paste("smartphone samsung")
    bot.enter()
 
    try:
        bot.find_element(selector='select__select', by=By.CLASS_NAME).click()
        bot.find_elements(selector='option', by=By.TAG_NAME)[-1].click()

        titulos = bot.find_elements(
            selector='product-card__title', by=By.CLASS_NAME
        )

        precos_promo = bot.find_elements(
            selector='product-card__highlight-price', by=By.CLASS_NAME
        )

        tipos_pg_promo = bot.find_elements(
            selector='product-card__highlight-price-description', by=By.CLASS_NAME
        )

        dados = []

        for titulo, preco_promo, tipo_pg_promo in zip(titulos, precos_promo, tipos_pg_promo):
            dados.append({
                'titulo': titulo.text.split(',')[0],
                'preco_pix': preco_promo.text,
                'tipo_pg_promo': tipo_pg_promo.text
            }) 
        
        df = pd.DataFrame(dados)
        df.index = df.index + 1
        df.to_csv(
            'smartphone_casasBahia_maisVendidos.csv',
            encoding='utf-8',
            index_label="Posição",
            sep=';'
        )

    except Exception as e:
        print(f'Erro: {e}')


    bot.wait(3000)
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



