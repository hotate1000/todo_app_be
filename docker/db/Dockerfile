# ベースイメージとして MySQL 8.0 の Debian ベースのイメージを使用する
FROM mysql:8.0-debian

# パッケージマネージャを更新し、必要なパッケージ（日本語ロケール）をインストールする
RUN apt-get update && \
    apt-get install -y locales && \
    rm -rf /var/lib/apt/lists/*

# 日本語ロケールの設定ファイルを生成し、ja_JP.UTF-8 ロケールを生成する
RUN echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen ja_JP.UTF-8 && \
    update-locale LANG=ja_JP.UTF-8

# 日本語ロケールを使うように環境変数を設定する
ENV LANG=ja_JP.UTF-8
ENV LANGUAGE=ja_JP:ja
ENV LC_ALL=ja_JP.UTF-8
