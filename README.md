Repositório:
- https://github.com/marcelmenezes/mssqlc


Caso já possua container MSSQL rodando, stopar antes:
```
docker stop sql_server_container
docker rm sql_server_container
```


MSSQL
```
docker-compose up -d
```



Python
```
pip install -r requirements.txt
python create.py
```


C#
```
cd c_sharp_demo
dotnet build
dotnet run


Exemplos de comandos sql:
create database db1
use db1
create table tb1(id int)
insert tb1(id) values (1), (2)
select * from tb1

```