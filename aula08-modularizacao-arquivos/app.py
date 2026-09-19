from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    stage = input("Etapa de vendas: ")

    # validações dos dados
    # necessário modelar os dados (lead) como um dicionário
    # modelar = model.py
    print(model_lead(name, email, stage))

    # de acordo com os dados modelados (lead como dict)
    # precisamos enviar esse dados do lead para o leads.json
    # control irá nos ajudar nisso

    control.create_lead(model_lead(name, email, stage))
    print("Lead adicionado")

def list_leads():
    leads = control.read_leads
    print(leads)

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar Lead")
        print("[2] Listar Leads")
        print("[0] Sair do programa")
    
        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("saindoooooooooooooooooooooooo")
            break
        else:
            print("chapou")

if __name__ == "__main__":
    main()