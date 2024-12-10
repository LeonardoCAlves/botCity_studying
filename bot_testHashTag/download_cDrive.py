import os
import shutil
from webdriver_manager.chrome import ChromeDriverManager

shutil.move(
    ChromeDriverManager().install(), 
    os.path.join(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)
            ), 'resources'
        ), "chromedriver.exe"
    )
)


