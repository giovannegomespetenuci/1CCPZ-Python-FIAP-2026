def conta_emails(dominios):
    d = dict()
    for item in dominios:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d

def append_items(nome, dominio):
    nomes.append(nome)
    dominios.append(dominio)
    return

listaemails = (
    "gustavo.pires@hotmail.com.br",
    "carla.oliveira@fiap.com.br",
    "rafael.cardoso@alura.com.br",
    "jessica.coelho@gmail.com.br",
    "bruno.santos@fiap.com.br",
    "helena.dantas@hotmail.com.br",
    "mariana.souza@alura.com.br",
    "fabio.correia@gmail.com.br",
    "isabela.ramos@fiap.com.br",
    "caio.andrade@hotmail.com.br",
    "vinicius.machado@alura.com.br",
    "adriana.melo@gmail.com.br",
    "daniel.costa@fiap.com.br",
    "sabrina.mendes@alura.com.br",
    "leonardo.siqueira@gmail.com.br",
)
dominios = list()
nomes = list()

for emails in listaemails:
    separados = emails.split("@")
    nome, dominio = separados
    append_items(nome, dominio)

print("Quantidade de emails por domínio:")
for k, v in conta_emails(dominios).items():
    print(f"{k}: {v}")

print()
tuplanomes = tuple(nomes)
print(f"Lista de usuários:{tuplanomes}")
print()
tuplanomesinvertida = tuplanomes[::-1]
print(f"Lista de usuários invertida:{tuplanomesinvertida}")