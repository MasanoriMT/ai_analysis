# 設定

## コンテナ起動

```
> docker-compose up -d

> docker-compose ps
    Name                   Command               State                 Ports              
------------------------------------------------------------------------------------------
db-container    docker-entrypoint.sh mysqld      Up      0.0.0.0:3306->3306/tcp, 33060/tcp
example.com     python3 manage.py runserve ...   Up      0.0.0.0:8001->80/tcp             
web-container   python3 manage.py runserve ...   Up      0.0.0.0:8000->8000/tcp   
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

```
> docker-compose restart
```

以下のURLにアクセスします。

```
http://localhost:8000/
```

