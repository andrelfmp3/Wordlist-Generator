print("IMPORTANTE: Se não souber responder, apenas aperte ENTER")
print("Se a resposta for sim, digite Y ou aperte ENTER")
print("Sempre use números em sua forma numérica (ex: 11, e não onze)")

wordlistContador = 0

# Função de input que incrementa contador
def contador_input(prompt):
    global wordlistContador
    resposta = input(prompt)
    if resposta != "":
        wordlistContador += 1
    return resposta

# Função para salvar valores no wordlist
def salvar_no_wordlist(valor, arquivo):
    if valor not in [None, ""]:
        arquivo.write((valor) + "\n")

# -------------------- DADOS --------------------
# Dados pessoais
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

# Cônjuge
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

# Casamento
casados = input("São casados? (Y/n) ").lower()
if casados in ["y", ""]:
    nomeCasamento = contador_input("Nome: ")
    apelidoCasamento = contador_input("Apelido: ")
    nickCasamento = contador_input("Principal Nick (@): ")
    anoNiverCasamento = contador_input("Ano que nasceu (número): ")
    mesNiverCasamento = contador_input("Mês que nasceu (número): ")
    diaNiverCasamento = contador_input("Dia que nasceu (número): ")
    nomePaiCasamento = contador_input("Nome do pai: ")
    nomeMaeCasamento = contador_input("Nome da mãe: ")
    nomeTrabalhoCasamento = contador_input("Local de trabalho: ")
    cidadeNasceuCasamento = contador_input("Cidade que nasceu: ")
    cidadeAtualCasamento = contador_input("Cidade atual: ")
    cargoCasamento = contador_input("Cargo: ")

# Filhos
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

# Pets
pets = []
if input("Teve algum pet? (y/N) ").lower() in ["y"]:
    qntd = int(contador_input("Quantidade de pets: "))
    for i in range(qntd):
        pet = {}
        pet["nome"] = contador_input(f"Nome do pet {i+1}: ")
        pet["anoNiver"] = contador_input(f"Ano que nasceu (número) do pet {i+1}: ")
        pet["mesNiver"] = contador_input(f"Mês que nasceu (número) do pet {i+1}: ")
        pet["diaNiver"] = contador_input(f"Dia que nasceu (número) do pet {i+1}: ")
        pet["apelido"] = contador_input(f"Espécie do pet {i+1}: ")
        pet["raca"] = contador_input(f"Raça do pet {i+1}: ")
        pets.append(pet)

# Carros
carros = []
if input("Teve algum carro? (y/N) ").lower() in ["y"]:
    qntd = int(contador_input("Quantidade de carros: "))
    for i in range(qntd):
        carro = {}
        carro["placa"] = contador_input(f"Placa do carro {i+1}: ")
        carros.append(carro)

# Palavras relevantes
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

# Configurações adicionais
print(f"\nQuantidade de palavras registradas: {wordlistContador}")
qtdPalavras = contador_input(f"Quantas palavras você quer no wordlist? Sugestão: {wordlistContador}: ")
if qtdPalavras == "":
    qtdPalavras = wordlistContador
else:
    qtdPalavras = int(qtdPalavras)

with open("wordlist.txt", "w", encoding="utf-8") as arquivo:
    # Dados pessoais
    salvar_no_wordlist(nome, arquivo)
    salvar_no_wordlist(apelido, arquivo)
    salvar_no_wordlist(nick, arquivo)
    salvar_no_wordlist(anoNiver, arquivo)
    salvar_no_wordlist(mesNiver, arquivo)
    salvar_no_wordlist(diaNiver, arquivo)
    salvar_no_wordlist(nomePai, arquivo)
    salvar_no_wordlist(nomeMae, arquivo)
    salvar_no_wordlist(nomeTrabalho, arquivo)
    salvar_no_wordlist(CidadeNasceu, arquivo)
    salvar_no_wordlist(CidadeAtual, arquivo)
    salvar_no_wordlist(Cargo, arquivo)
