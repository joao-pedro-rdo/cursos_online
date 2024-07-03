from cursos_online.funcionalidades_auxiliares import *

from cursos_online.usuarios import *
from cursos_online.cursos import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker


def main():
    # Definicao da intancia do faker para a lingua BR
    faker_instance = Faker(locale="pt_BR")

    # Criando as instancias
    print("\n\n")
    print("==== Criando Instâncias ====")
    for _ in range(2):
        Administrador(
            email=faker_instance.email(),
            senha=faker_instance.password(),
            nome=faker_instance.name(),
            cpf=faker_instance.cpf(),
        )
    for _ in range(2):
        Aluno(
            email=faker_instance.email(),
            senha=faker_instance.password(),
            nome=faker_instance.name(),
            cpf=faker_instance.cpf(),
        )
    for _ in range(2):
        Professor(
            email=faker_instance.email(),
            senha=faker_instance.password(),
            nome=faker_instance.name(),
            cpf=faker_instance.cpf(),
        )

    curso_teste = Curso(nome="Nome do Curso", descricao=faker_instance.text())
    print("Sou CURSO ==", curso_teste.nome)

    print("\n\n")
    print("==== Listando Instâncias Criadas ====")
    classes_a_serem_listadas = [Administrador, Aluno, Professor, Curso]
    for classe in classes_a_serem_listadas:
        for instancia in classe.all():
            print(instancia)

    # Checking if the user wants to remove the created instances
    print("\n\n")
    remove_instances = input("Remover instâncias? [S/N]")

    # Remove as instancias da database
    if remove_instances.lower() == "s":
        print("==== Deletando Instâncias ====")
        classes_a_serem_deletadas = [Administrador, Aluno, Professor, Curso]
        for classe in classes_a_serem_deletadas:
            for instancia in classe.all():
                classe.delete(id=instancia.id)


if __name__ == "__main__":
    # Defining the database connection (please note that the database URL is hardcoded for brevity, which is not recommended)
    GerenciadorEntidades.engine = create_engine("mysql+pymysql://root:root@localhost/cursos_online")
    GerenciadorEntidades.base.metadata.create_all(GerenciadorEntidades.engine)
    GerenciadorEntidades.session_maker = sessionmaker(bind=GerenciadorEntidades.engine)
    GerenciadorEntidades.session = GerenciadorEntidades.session_maker()

    # Running the main function
    main()
