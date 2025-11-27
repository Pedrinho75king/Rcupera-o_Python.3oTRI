itens = []

while True:
    item = input("Digite um item (ou 'fim' para encerrar): ")

    if item.lower() == "fim":
        break

    itens.append(item)

print("Lista de compras:")
for item in itens:
    print("-", item)