from botcity.web import WebBot, Browser, By
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    maestro = BotMaestroSDK.from_sys_args()

    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    bot.headless = False

    bot.browser = Browser.CHROME

    bot.driver_path = bot.get_resource_abspath('chromedriver.exe')

    bot.browse("https://dlp.hashtagtreinamentos.com/python/intensivao/login?ps=incompany")
 
    bot.wait(30000)
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













