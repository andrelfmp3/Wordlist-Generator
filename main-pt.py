print(" __      __          _ _ _    _          ")
print(" \ \    / /__ _ _ __| | (_)__| |_        ")
print("  \ \/\/ / _ \ '_/ _` | | (_-<  _|       ")
print("   \_/\_/\___/_| \__,_|_|_/__/\__|       ")
print("  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ ")
print(" | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|")
print("  \___\___|_||_\___|_| \__,_|\__\___/_|         > Desenvolvido por: github.com/andrelfmp3")
print("")                                    
print("IMPORTANTE: Se não souber responder, apenas aperte ENTER")
print("Se a resposta for sim, digite Y ou aperte ENTER")
print("Sempre use números em sua forma numérica (ex: 11, e não onze)")

# funções ----------------------------------------
wordlistContador = 0
listaWordlist = []

def contador_input(prompt):
    global wordlistContador
    resposta = input(prompt)
    if resposta != "":
        wordlistContador += 1
    return resposta

def salvarNoWordlist(valor, arquivo):
    if valor not in [None, ""]:
        arquivo.write((valor) + "\n")
        listaWordlist.append(valor)
        
def trocaLetraNumero(palavra):
    # dicionário de substituições
    mapa_substituicao = {
        'a': '4', 'A': '4',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        'o': '0', 'O': '0',
        's': '5', 'S': '5',
    }

    resultado = ""
    for char in palavra:
        if char in mapa_substituicao:
            resultado += mapa_substituicao[char]  # troca a letra
        else:
            resultado += char  # mantém igual
    return resultado

# dados ----------------------------------------
nome = contador_input("Nome: ")
apelido = contador_input("Apelido: ")
nick = contador_input("Principal Nick (@): ")
anoNiver = contador_input("Ano que nasceu (número): ")
mesNiver = contador_input("Mês que nasceu (número): ")
diaNiver = contador_input("Dia que nasceu (número): ")
nomePai = contador_input("Nome do pai: ")
nomeMae = contador_input("Nome da mãe: ")
nomeTrabalho = contador_input("Local de trabalho: ")
CidadeNasceu = contador_input("Cidade que nasceu: ")
CidadeAtual = contador_input("Cidade atual: ")
Cargo = contador_input("Cargo: ")

conjuge = {}
if input("Possui cônjuge? (Y/n) ").lower() in ["y", ""]:
    conjuge["nome"] = contador_input("Nome do cônjuge: ")
    conjuge["apelido"] = contador_input("Apelido do cônjuge: ")
    conjuge["nick"] = contador_input("Principal nick (@) do cônjuge: ")
    conjuge["anoNiver"] = contador_input("Ano que o cônjuge nasceu: ")
    conjuge["mesNiver"] = contador_input("Mês que o cônjuge nasceu: ")
    conjuge["diaNiver"] = contador_input("Dia que o cônjuge nasceu: ")
    conjuge["trabalho"] = contador_input("Local de trabalho do cônjuge: ")
    conjuge["cargo"] = contador_input("Cargo do cônjuge: ")
    conjuge["anoNamoro"] = contador_input("Ano que começaram a namorar: ")
    conjuge["mesNamoro"] = contador_input("Mês que começaram a namorar: ")
    conjuge["diaNamoro"] = contador_input("Dia que começaram a namorar: ")

casamento = {}
if input("São casados? (Y/n) ").lower() in ["y", ""]:
    casamento["nome"] = contador_input("Nome: ")
    casamento["apelido"] = contador_input("Apelido: ")
    casamento["nick"] = contador_input("Principal Nick (@): ")
    casamento["anoNiver"] = contador_input("Ano que nasceu (número): ")
    casamento["mesNiver"] = contador_input("Mês que nasceu (número): ")
    casamento["diaNiver"] = contador_input("Dia que nasceu (número): ")
    casamento["nomePai"] = contador_input("Nome do pai: ")
    casamento["nomeMae"] = contador_input("Nome da mãe: ")
    casamento["nomeTrabalho"] = contador_input("Local de trabalho: ")
    casamento["cidadeNasceu"] = contador_input("Cidade que nasceu: ")
    casamento["cidadeAtual"] = contador_input("Cidade atual: ")
    casamento["cargo"] = contador_input("Cargo: ")

filhos = []
if input("Possuem filhos? (y/N) ").lower() in ["y"]:
    qntd = int(contador_input("Quantidade de filhos: "))
    for i in range(qntd):
        filho = {}
        filho["nome"] = contador_input(f"Nome do filho {i+1}: ")
        filho["nick"] = contador_input(f"Principal nick (@) do filho {i+1}: ")
        filho["anoNiver"] = contador_input(f"Ano que nasceu (número) do filho {i+1}: ")
        filho["mesNiver"] = contador_input(f"Mês que nasceu (número) do filho {i+1}: ")
        filho["diaNiver"] = contador_input(f"Dia que nasceu (número) do filho {i+1}: ")
        filho["apelido"] = contador_input(f"Apelido do filho {i+1}: ")
        filhos.append(filho)

pets = []
if input("Teve algum pet? (y/N) ").lower() in ["y"]:
    qntd = int(contador_input("Quantidade de pets: "))
    for i in range(qntd):
        pet = {}
        pet["nome"] = contador_input(f"Nome do pet {i+1}: ")
        pet["anoNiver"] = contador_input(f"Ano que nasceu (número) do pet {i+1}: ")
        pet["mesNiver"] = contador_input(f"Mês que nasceu (número) do pet {i+1}: ")
        pet["diaNiver"] = contador_input(f"Dia que nasceu (número) do pet {i+1}: ")
        pet["especie"] = contador_input(f"Espécie do pet {i+1}: ")
        pet["raca"] = contador_input(f"Raça do pet {i+1}: ")
        pets.append(pet)

carros = []
if input("Teve algum carro? (y/N) ").lower() in ["y"]:
    qntd = int(contador_input("Quantidade de carros: "))
    for i in range(qntd):
        carro = {}
        carro["placa"] = contador_input(f"Placa do carro {i+1}: ")
        carros.append(carro)

palavras_relevantes = []
update = 1
print("Outras palavras que podem ser relevantes: (Pressione Enter para sair)")
while True:
    palavra = input(f"Palavra {update}: ")
    if palavra == "":
        break
    palavras_relevantes.append(palavra)
    wordlistContador += 1
    update += 1

# Combinações adicionais --------------------------------
print(f"\nQuantidade de palavras registradas: {wordlistContador}")

concatena = input("Mais combinações: Concatenar números registrados ao finals das palavras registradas? Ex: palavra + 123, palavra123 (Y/n)").lower()
if concatena in ["y", ""]:
    concatena = True
trocaNumero = input("Mais combinações: Trocar letras por números? Ex: A -> 4, E -> 3, (Y/n) ").lower()
if trocaNumero in ["y", ""]:
    trocaNumero = True
# futura ideia: substituir letras por simbolos, mas sem sobreescrever numeros = A -> 4 ou A -> @?

# wordlist ----------------------------------------
with open("wordlist.txt", "w", encoding="utf-8") as arquivo:
    # Dados pessoais
    salvarNoWordlist(nome, arquivo)
    salvarNoWordlist(apelido, arquivo)
    salvarNoWordlist(nick, arquivo)
    salvarNoWordlist(anoNiver, arquivo)
    salvarNoWordlist(mesNiver, arquivo)
    salvarNoWordlist(diaNiver, arquivo)
    salvarNoWordlist(nomePai, arquivo)
    salvarNoWordlist(nomeMae, arquivo)
    salvarNoWordlist(nomeTrabalho, arquivo)
    salvarNoWordlist(CidadeNasceu, arquivo)
    salvarNoWordlist(CidadeAtual, arquivo)
    salvarNoWordlist(Cargo, arquivo)

    # Cônjuge
    for valor in conjuge.values():
        salvarNoWordlist(valor, arquivo)

    # Casamento
    for valor in casamento.values():
        salvarNoWordlist(valor, arquivo)

    # Filhos
    for filho in filhos:
        for valor in filho.values():
            salvarNoWordlist(valor, arquivo)

    # Pets
    for pet in pets:
        for valor in pet.values():
            salvarNoWordlist(valor, arquivo)

    # Carros
    for carro in carros:
        for valor in carro.values():
            salvarNoWordlist(valor, arquivo)

    # Palavras extras
    for palavra in palavras_relevantes:
        salvarNoWordlist(palavra, arquivo)
          
    if concatena:
        # concatena
        numerosNaWordlist = []
        for item in listaWordlist:
            if item.isnumeric():
                numerosNaWordlist.append(item)
        for palavra in listaWordlist:
            if not palavra.isnumeric():  # só combina palavras
                for numero in numerosNaWordlist:
                    combinacao = palavra + numero
                    salvarNoWordlist(combinacao, arquivo)
                    
    if trocaNumero:
        # troca letra e numero
        for palavra in listaWordlist:
            salvarNoWordlist(trocaLetraNumero(palavra), arquivo)