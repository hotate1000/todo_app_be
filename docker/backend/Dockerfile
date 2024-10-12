FROM python:3.11.0

ARG root_path=/src

WORKDIR $root_path

# Pythonのキャッシュファイルが指定のディレクトに保存
ENV PYTHONPYCACHEPREFIX=/var/cache/python
# root_path内のPythonモジュールをインポート可能になる
ENV PYTHONPATH=$root_path
# Python の標準出力および標準エラー出力をバッファリングせずに直接出力するように設定
ENV PYTHONUNBUFFRED=1

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN pip install --upgrade pip
# setuptoolsパッケージを最新バージョンにアップグレード。setuptoolsはPythonのパッケージのビルドやインストールに必要なツール
RUN pip install --upgrade setuptools
