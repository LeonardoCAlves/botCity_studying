from botcity.core import DesktopBot
from botcity.maestro import *
import json

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    try:
        with open(r'dados\produtos.json', 'r', encoding='utf-8') as file:
            produtos = json.load(file)
    except FileNotFoundError as e:
        print(e)

    bot = DesktopBot()

    path_fakturama = r"C:\Program Files\Fakturama2\Fakturama.exe"
    bot.execute(path_fakturama)

    for produto in produtos:
        if not bot.find( "novo_produto", matching=0.97, waiting_time=10000):
            not_found("novo_produto")
        bot.click()
      
        if not bot.find( "id", matching=0.97, waiting_time=10000):
            not_found("id")
        bot.click_relative(130, 9)

        bot.type_keys(str(produto["id"]))
        
        bot.tab()
        bot.type_keys(str(produto['nome']))

        bot.tab()        
        bot.type_keys(str(produto['categoria']))
        
        bot.tab()
        bot.type_keys(str(produto['gtin']))
        
        bot.tab()
        bot.type_keys(str(produto['fornecedor']))
        
        bot.tab()
        bot.type_keys(str(produto['descricao']))
        
        bot.tab()
        bot.control_a()
        bot.type_keys(str(produto['preco']))
        
        bot.tab()
        bot.control_a()      
        bot.type_keys(str(produto['preco_custo']))

        bot.tab()
        bot.control_a()
        bot.type_keys(str(produto['subsidio']))

        bot.tab()

        bot.tab()
        bot.control_a()
        bot.type_keys(str(produto['estoque']))     
        
        if not bot.find( "btn_salvar", matching=0.97, waiting_time=10000):
            not_found("btn_salvar")
        bot.click()
        
        bot.control_w()
        
    bot.alt_f4()
        
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()










