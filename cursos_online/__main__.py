from .usuarios import *
# from usuarios.administrador import Administrador 

# from usuarios.entity_manager import EntityManager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from random import choice #? OQUE ESSA PORRA FAZ ???

def main():
    # Definicao da intancia do faker para a lingua BR
    faker_instance = Faker(locale="pt_BR")

    #Criando as instancias
    print("\n\n")
    print("==== Criando Instâncias ====")
    
    # #! TESTE QUE FUNCIONA 
    # print("EU SOU O ADM =======")
    # hop = Administrador(email=faker_instance.email(), senha=faker_instance.password(), nome=faker_instance.name(), data_nascimento=faker_instance.date_this_year(), cpf=faker_instance.cpf())
    # print(hop.nome)
    # print(hop.email)
    # print(hop.senha)
    # # print(hop.data_nascimento)
    # print(hop.cpf)

    for _ in range(2):
        Administrador(email=faker_instance.email(), senha=faker_instance.password(), nome=faker_instance.name(), data_nascimento=faker_instance.date_this_year(), cpf=faker_instance.cpf())
    for _ in range(2):
        Aluno(email=faker_instance.email(), senha=faker_instance.password(), nome=faker_instance.name(), data_nascimento=faker_instance.date_this_year(), cpf=faker_instance.cpf())
    for _ in range(2):
        Professor(email=faker_instance.email(), senha=faker_instance.password(), nome=faker_instance.name(), data_nascimento=faker_instance.date_this_year(), cpf=faker_instance.cpf())



 
    print("\n\n")
    print("==== Listando Instâncias Criadas ====")
    
    for user in User.all():
        print(f"{user.id}: {user.nome} ({user.email})") # TODO: MOSTRAR O RESTO DOS DADOS 
    print("\n\n")


    '''
    random_user = choice(User.all())
    update_instance = input(f"Atualizar instância {random_user}? [S/N]")

    # If the user wants to update the instance, the name and email will be updated with random data
    if update_instance.lower() == "s":
        print("==== Atualizando Instância ====")

        print(f"[ANTES] {random_user}. Nome: {random_user.name}, Email: {random_user.email}")

        User.update(id=random_user.id, new_attributes={"name": faker_instance.name(), "email": faker_instance.email()})

        print(f"[DEPOIS] {random_user}. Nome: {random_user.name}, Email: {random_user.email}")
        print("\n\n")

    # Checking if the user wants to remove the created instances
    remove_instances = input("Remover instâncias? [S/N]")

    # If the user wants to remove the instances, all instances will be deleted from the database
    if remove_instances.lower() == "s":
        print("==== Deletando Instâncias ====")
        for user in User.all():
            user.delete(id=user.id)
'''

if __name__ == "__main__":
    # Defining the database connection (please note that the database URL is hardcoded for brevity, which is not recommended)
    EntityManager.engine = create_engine("mysql+pymysql://root:root@localhost/teste")
    EntityManager.base.metadata.create_all(EntityManager.engine)
    EntityManager.session_maker = sessionmaker(bind=EntityManager.engine)
    EntityManager.session = EntityManager.session_maker()

    # Running the main function
    main()

