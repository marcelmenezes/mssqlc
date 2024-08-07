
docker pull mcr.microsoft.com/mssql/server:2022-latest


docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=YourStrongPassw0rd" -p 1433:1433 --name sql_server_container -d mcr.microsoft.com/mssql/server:2022-latest


docker-compose up -d