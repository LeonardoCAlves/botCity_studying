from botcity.web import WebBot, Browser, By
from botcity.maestro import *
import pandas


# Disable errors if we are not connected to Maestro
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
        import pandas as pd
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

    
    
    

    bot.wait(10000)
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
