# cursos_online
Projeto de plataforma de cursos em python orientado a objetos
## Como usar o poetry para executar o projeto
Instale o poetry atraves do seguinte link [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

Com o poetry instalado faça:
- Para instalar o ambeinte virtual com as dependencias do projeto
```bash
poetry install
```
- Para abrir o ambiente virtual
```bash
poetry shell
```

## Como executar o projeto
- Executar o projeto (deve estar no diretorio cursos_online)
```bash
python3 -B -m cursos_online
```

## Configurando Mysql
- instale o Mysql
```bash
sudo apt install mysql-server
```
- Entre na conta root e crie a database
```bash
mysql -u root -p
create database cursos_online
```
*AGORA O BANCO DE DADOS ESTA PRONTO PRA SER EXECUTADO NA APLICAÇÃO*

## Como levantar o banco de dadpos com docker + doker compose 
Para instanciar e levantar o nosso container docker pela primeira vez:
```bash
docker-compose up -d
```
verificar se esta ativo
```bash
docker-compose ps
```
Comando para entrar no container do banco de dados:
docker exec -it bd-cursos-online mysql -u root -p

`senha: root`
