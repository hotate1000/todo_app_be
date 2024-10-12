# docker

## ネットワークを作成する

```bash
docker network create -d bridge db_network
docker network create -d bridge sys-db-app-sql-net
```

## コンテナ内に入る

```bash
docker-compose exec app bash
docker-compose exec db bash
```

# mysql

## pythonでテーブル管理

### alembicの利用

```bash
# 初期化
alembic init alembic
# マイグレーションファイル作成
alembic revision --autogenerate -m "Create Init Tables"
# マイグレーションのダウングレード
alembic downgrade base
# マイグレーションの再実行
alembic upgrade head
```

## SQL

```sql
SHOW CREATE TABLE table_name;
DESC table_name;
ALTER TABLE user MODIFY COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
ALTER TABLE company MODIFY COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
```
