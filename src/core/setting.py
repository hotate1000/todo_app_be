import os
from dotenv import load_dotenv
from functools import lru_cache


class Setting:
    load_dotenv()

    app_name: str = os.getenv("APP_NAME")
    app_description: str = os.getenv("APP_DESCRIPTION")
    app_version: str = os.getenv("APP_VERSION")

    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_host: str = os.getenv("DB_HOST")
    db_name: str = os.getenv("DB_NAME")
    db_port: str = os.getenv("DB_PORT")


# @lru_cacheについて関数の結果をメモリに保存するデコレータ。
# 関数が同じ引数で何度も呼び出された際に、計算結果を再利用してパフォーマンスを向上させる。
# 計算コストが高い関数や、頻繁に同じ結果を返す関数で効果的。
@lru_cache
def get_setting():
    try:
        return Setting()
    except Exception as e:
        print("Setting {}".format(e))
