# 設定

## コンテナ起動

```
> docker-compose up -d

> docker-compose ps
      Name                     Command               State                 Ports
----------------------------------------------------------------------------------------------
ai_analysis_db_1    docker-entrypoint.sh mysqld      Up      0.0.0.0:3306->3306/tcp, 33060/tcp
ai_analysis_web_1   python3 app/manage.py runs ...   Up      0.0.0.0:8000->8000/tcp
```

## DB 作成

```
> docker-compose exec db setup

Done
```

## マイグレーション

```
> docker-compose exec web python3 manage.py migrate
```

# 実行

以下のURLにアクセスします。

```
http://localhost:8000/
```

