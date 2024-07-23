# Plataforma de Cursos Online (Em desenvolvimento)
Projeto de plataforma de cursos em Python orientado a objetos.

## Descrição do projeto
Este projeto visa desenvolver uma plataforma de cursos online utilizando Python e orientação a objetos. A plataforma permite que os usuários se inscrevam em cursos, assistam às aulas e acompanhem seu progresso. O projeto é construído utilizando boas práticas de desenvolvimento de software e ferramentas modernas como Poetry e Docker.

## Estrutura do projeto
A estrutura de diretórios do projeto é organizada da seguinte forma:

```
cursos_online/
├── cursos_online/
│ ├── __init__.py
│ ├── __main__.py
│ ├── pagina_inicial.py
│ └── funcionalidades_auxiliares/
│     ├── __init__.py
│     ├── gerenciador_entidades.py      
│ └── pages/ 
│     ├── __init__.py
│     ├── busca.py
│     ├── cadastro.py
│     ├── login.py
│     ├── matricula.py
│     ├── menu_administrador.py
│     ├── menu_aluno.py
│     ├── menu_professor.py
│ └── usuarios/
│     ├── __init__.py
│     ├── administrador.py
│     ├── aluno.py
│     ├── professor.py
│     ├── matricula.py 
│     ├── usuario.py 
│ └── cursos/
│     ├── __init__.py
│     ├── curso.py
│     ├── aula.py
├── pyproject.toml
├── README.md
└── docker-compose.yml
```

- `cursos_online/`: Contém o código fonte do projeto.
- `pages/`: Contém os arquivos de páginas da aplicação com streamlit.
- `usuarios/`: Contém as classes de usuários da aplicação.
- `cursos/`: Contém as classes de cursos da aplicação.
- `funcionalidades_auxiliares/`: Contém as classes de gerenciamento de entidades.
- `pyproject.toml`: Arquivo de configuração do Poetry.
- `README.md`: Documentação do projeto.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose.

## Guia de Instalação
### Instalando dependências com Poetry
Poetry é uma ferramenta de gerenciamento de dependências e ambientes virtuais para projetos Python. Para instalar o Poetry, siga as instruções no site oficial [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).

Depois de instalar o Poetry, execute os seguintes comandos para configurar o ambiente virtual e instalar as dependências do projeto:
```bash
# Instalar as dependências do projeto
poetry install

# Abrir o ambiente virtual
poetry shell
```

## Guia de Execução
### Executando o projeto
Para executar o projeto, certifique-se de estar no diretório cursos_online e execute o seguinte comando:
```bash
python3 -B -m cursos_online
```

## Executando o banco de dados com Docker e Docker Compose (Recomendado)
Para facilitar a configuração do banco de dados, utilizamos o Docker e o Docker Compose. Docker é uma plataforma para desenvolver, enviar e executar aplicações em containers, enquanto Docker Compose é uma ferramenta para definir e gerenciar aplicações multi-container.

### Criar uma rede Docker
Primeiro, crie uma rede Docker que possibilita a comunicação entre os containers e a máquina host dentro da sua rede local:

```bash
docker network create -d ipvlan \
  --subnet=192.168.0.0/24 \
  --gateway=192.168.0.1 \
  -o parent=wlp2s0 \
  my_ipvlan_wifi_network
```
Levantar o container do banco de dados
No diretório do projeto (/cursos_online), execute:
```bash
docker-compose up -d
```

Acessar o container do banco de dados
```bash
docker exec -it bd-cursos-online mysql -u root -p
```
*Senha:* `root`


Configurando MySQL na própria máquina
Caso prefira configurar o MySQL localmente, siga os passos abaixo:

Instale o MySQL:
```bash
sudo apt install mysql-server
```
Entre na conta root e crie a base de dados:
```bash
mysql -u root -p
create database cursos_online;
```

## Equipe de Desenvolvimento
Nome: João Pedro Ramos de Oliveira

E-mail: joaoprdo2.aluno@unimpampa.edu.br




