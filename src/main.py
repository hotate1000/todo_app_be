import uvicorn
from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from core.router import router
from core.setting import get_setting


setting = get_setting()


def middleware() -> List[Middleware]:
    middlewares = [
        Middleware(
            # CORS（Cross-Origin Resource Sharing）を設定するためのミドルウェア
            # - allow_origins=['*']: すべてのオリジンからのリクエストを許可。
            # - allow_credentials=True: 認証情報（クッキーやHTTP認証ヘッダー）の共有を許可。
            # - allow_methods=['*']: すべてのHTTPメソッド（GET, POST, PUT, DELETEなど）を許可。
            # - allow_headers=['*']: すべてのリクエストヘッダーを許可。
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
    ]
    return middlewares


def init_app():
    # auto_error=Falseにより、認証エラー時に自動的にエラーを発生させない設定
    bearer_scheme = HTTPBearer(auto_error=False)
    app = FastAPI(
        # FastAPI アプリケーションのタイトルを設定。
        title=setting.app_name,
        # アプリケーションの説明を設定。
        description=setting.app_description,
        # アプリケーションのバージョンを設定。
        version=setting.app_version,
        # 上記で定義した `middleware()` 関数を呼び出し、ミドルウェアを設定。
        middleware=middleware(),
        # Swagger UI の設定で、APIのHTTPメソッドでソート(GET、POST、PUT、DELETE等)するように設定。
        swagger_ui_parameters={
            "operationsSorter": "method"
        }
    )

    # アプリケーションにルーターを含める。
    # ルーター全体にbearer_schemeを依存関係として追加し、リクエスト時に認証を処理。
    app.include_router(router, dependencies=[Depends(bearer_scheme)])

    return app


app = init_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=80,
        reload=True
    )
