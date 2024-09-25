

# Plataforma de Cursos Online (Em desenvolvimento)
Projeto de plataforma de cursos em Python orientado a objetos, este projeto ainda não esta funcional na parte de programção. Mas o ambiente de desentolvimento esta pronto para ser utilizado, usando devcontinares e docker, fiz as configuraçoes necessarias para que com poucos comandos o ambiente de desenvolvimento esteja pronto para ser utilizado. Estou me dedicando para aplicar as praticas de DevOps que venho estudando.

## Todo
  - [ ] Refatorar código
  - [ ] Adicionar funcionalidades
  - [ ] Adicionar Documentação da arquitetura
  - [ ] Adicionar Documentação de como contribuir
  - [ ] Adicionar Pipeline de CI/CD
  - [ ] Adicionar auteticação com streamlit
  - [ ] Adicionar autenticação https://github.com/GauriSP10/streamlit_login_auth_ui (Projeto base)
  - [ ] Adicionar diagrama de bloco
  - [ ] Adicionar .env para definir variaveis de ambiente de desenvolvimento e homologação
  - [ ] Adicionar testes
  - [ ] Adicionar pasta somente de da arquivos docker
  - [ ] Adcionar documentação das tecnologias utilizadas no docker compose (DNS, volumes, Networks, include, etc)
  - [ ] Atualizar documentação sobre os testes de unidade com pipeline
  - [ ] Arrumar pipeline de deploy com docker 


## Descrição do projeto
Este projeto visa desenvolver uma plataforma de cursos online utilizando Python e orientação a objetos. A plataforma permite que os usuários se inscrevam em cursos, assistam às aulas e acompanhem seu progresso. O projeto é construído utilizando boas práticas de desenvolvimento de software e ferramentas modernas como Poetry e Docker e desenvolvido usando devcontainers.

## Índice
- [Estrutura do projeto](#estrutura-do-projeto)
- [Guia de execução com docker](#guia-de-execução)
  - [Requisitos](#requisitos)
  - [Acessando o ambiente de desenvolvimento com Devcontainers](#acessando-o-ambiente-de-desenvolvimento-com-devcontainers)
  - [Guia de execução Local](#guia-de-execução-local)
    - [Instalando dependências com Poetry](#instalando-dependências-com-poetry)
    - [Executando o banco de dados com Docker e Docker Compose (Recomendado)](#executando-o-banco-de-dados-com-docker-e-docker-compose-recomendado)
    - [Executando o projeto](#executando-o-projeto)
    - [Configurando banco de dados localmente](#configurando-banco-de-dados-localmente)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Equipe de Desenvolvimento](#equipe-de-desenvolvimento)



## Guia de execução
A execução do projeto foi planejada para ser realizada usando Docker, para facilitar o processo.

### Requisitos:
- Ambiente de desenvolvimento com Devcontainers:
  - Docker
  - Docker Compose
  - Visual Studio Code
    - [Devcontainers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

- Execução do ambiente de homologação local:
  - Docker 
  - Docker Compose

### Acessando o ambiente de desenvolvimento com Devcontainers:
1. Clone o repositório:
```bash
git clone https://github.com/joao-pedro-rdo/cursos_online.git
```
2. Abra o Visual Studio Code e acesse a pasta do projeto.
3. Quando abrir o projeto no Visual Studio Code, uma notificação será exibida perguntando se você deseja reabrir o projeto em um Devcontainer. Clique em `Reopen in Container`.
- Caso a notificação não seja exibida, pressione `ctrl+shift+p`  e selecione a opção `Reopen in Container`.
4. Aguarde o ambiente de desenvolvimento ser configurado. Isso pode levar alguns minutos.
5. Quando o ambiente de desenvolvimento estiver pronto, você verá uma notificação informando que o Devcontainer foi configurado com sucesso.
6. Apos a configuração do ambiente de desenvolvimento, o portry ira instalar as dependencias do projeto e o banco de dados ja deverá estar configurado e pronto para ser utilizado.
7. Execute o projeto no terminal do Vs Code com o comando:
```bash
python3 -B -m cursos_online
```

### Executando ambiente de homologação com Docker
Para executar o ambiente de homologação com Docker, siga os passos abaixo:
```bash
docker compose up -d
```


<details>
  <summary>Guia de execução Local</summary>

## Guia de Execução local

### Instalando dependências com Poetry
Poetry é uma ferramenta de gerenciamento de dependências e ambientes virtuais para projetos Python. Para instalar o Poetry, siga as instruções no site oficial [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).

Depois de instalar o Poetry, execute os seguintes comandos para configurar o ambiente virtual e instalar as dependências do projeto:
```bash
# Instalar as dependências do projeto
poetry install

# Abrir o ambiente virtual
poetry shell
```
## Executando o banco de dados com Docker e Docker Compose (Recomendado)
Para facilitar a configuração do banco de dados, utilizamos o Docker e o Docker Compose. Docker é uma plataforma para desenvolver, enviar e executar aplicações em containers, enquanto Docker Compose é uma ferramenta para definir e gerenciar aplicações multi-container.

Levantar o container do banco de dados
No diretório do projeto (`/cursos_online`), execute:
```bash
docker compose -f compose.db.yml up -d
```

### Executando o projeto
Para executar o projeto, certifique-se de estar no diretório cursos_online e o banco de dados online e e execute o seguinte comando:
```bash
python3 -B -m cursos_online
```
Caso deseje acessar o banco de dados no container para realizar consultas , siga os passos abaixo:

```bash
docker exec -it bd-cursos-online mysql -u root -p
```
*Senha:* `root`
- pode trocar o nome do container pelo id do container que pode ser obtido com o comando `docker container ls`


## Configurando banco de dados localmente 
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
</details>

## Estrutura do projeto
A estrutura de diretórios do projeto é organizada da seguinte forma:

```
cursos_online
├── Dockerfile
├── LICENSE
├── README.md
├── compose.db.yml
├── compose.yml
├── cursos_online
│   ├── __init__.py
│   ├── __main__.py
│   ├── cursos
│   │   ├── __init__.py
│   │   ├── aula.py
│   │   └── curso.py
│   ├── funcionalidades_auxiliares
│   │   ├── __init__.py
│   │   └── gerenciador_entidades.py
│   ├── pages
│   │   ├── __init__.py
│   │   ├── busca.py
│   │   ├── cadastro.py
│   │   ├── login.py
│   │   ├── matricula.py
│   │   ├── menus_administrador.py
│   │   ├── menus_aluno.py
│   │   └── menus_professor.py
│   ├── pagina_inicial.py
│   ├── sonar-project.properties
│   └── usuarios
│       ├── __init__.py
│       ├── administrador.py
│       ├── aluno.py
│       ├── matricula.py
│       ├── professor.py
│       └── usuario.py
├── poetry.lock
├── pyproject.toml
└── requirements.txt

```

- `cursos_online/`: Contém o código fonte do projeto.
- `pages/`: Contém os arquivos de páginas da aplicação com streamlit.
- `usuarios/`: Contém as classes de usuários da aplicação.
- `cursos/`: Contém as classes de cursos da aplicação.
- `funcionalidades_auxiliares/`: Contém as classes de gerenciamento de entidades.
- `pyproject.toml`: Arquivo de configuração do Poetry.
- `README.md`: Documentação do projeto.
- `compose.yml`: Arquivo de configuração do Docker Compose para ambiente de homologação.
- `compose.db.yml`: Arquivo de configuração do banco de dados mysql para ambiente de homologação e desenvolvimento.
- `Dockerfile`: Arquivo para criação da imagem Docker do ambiente de homologação.
- `requirements.txt`: Arquivo de dependências do projeto exportado do poetry para uso com pip e Dockerfile.
- `.devcontainers/`: Contém os arquivos de configuração do ambiente de desenvolvimento com Devcontainers.

## Equipe de Desenvolvimento
Nome: João Pedro Ramos de Oliveira

E-mail: joaoprdo2.aluno@unimpampa.edu.br




