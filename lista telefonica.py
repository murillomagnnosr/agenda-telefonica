contacts = []

def add_contact():
    name = input("Digite o nome do contato: ")
    phone = input("Digite o número de telefone: ")
    contacts.append({"name": name, "phone": phone})
    print(f"Contato '{name}' adicionado com sucesso!\n")

def show_contacts():
    if len(contacts) == 0:
        print("Nenhum contato encontrado. A lista está vazia.\n")
        return

    print("---- Todos os Contatos ----")
    for i in range(len(contacts)):
        print(f"{i + 1}. Nome: {contacts[i]['name']} | Telefone: {contacts[i]['phone']}")
    print("---------------------------\n")

def search_contact():
    search_name = input("Digite o nome para pesquisar: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f"Contato encontrado! Nome: {contact['name']} | Telefone: {contact['phone']}\n")
            found = True
            break

    if not found:
        print(f"Nenhum contato com o nome '{search_name}' foi encontrado.\n")

def remove_contact():
    remove_name = input("Digite o nome do contato que deseja remover: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == remove_name.lower():
            contacts.remove(contact)
            print(f"Contato '{remove_name}' removido com sucesso!\n")
            found = True
            break

    if not found:
        print(f"Nenhum contato com o nome '{remove_name}' foi encontrado.\n")

def main():
    print("Bem-vindo ao App de Lista de Contatos!\n")

    while True:
        print("O que você deseja fazer?")
        print("1 - Adicionar um contato")
        print("2 - Mostrar todos os contatos")
        print("3 - Pesquisar por um contato")
        print("4 - Remover um contato")
        print("5 - Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            add_contact()
        elif option == "2":
            show_contacts()
        elif option == "3":
            search_contact()
        elif option == "4":
            remove_contact()
        elif option == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida, por favor tente novamente.\n")

main()