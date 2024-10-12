import os
from dotenv import load_dotenv
from functools import lru_cache


class Setting:
    load_dotenv()

    app_name: str = os.getenv("APP_NAME")
    app_description: str = os.getenv("APP_DESCRIPTION")
    app_version: str = os.getenv("APP_VERSION")

@lru_cache
def get_setting():
    try:
        return Setting()
    except Exception as e:
        print("Setting {}".format(e))
