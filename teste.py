print("IMPORTANTE: Se não souber responder, apenas aperte ENTER")

nome = input("Nome: ")
apelido = input("Apelido: ")
nick = input("Principal Nick (@): ")
anoNiver = input("Ano que nasceu (número): ")
mesNiver = input("Mês que nasceu (número): ")
diaNiver = input("Dia que nasceu (número): ")
nomePai = input("Nome do pai: ")
nomeMãe = input("Nome da mãe: ")
nomeTrabalho = input("Local de trabalho: ")
CidadeNasceu = input("Cidade que nasceu: ")
CidadeAtual = input("Cidade atual: ")
Cargo = input("Cargo:")

temp = input("Possui conjuge? (Y/n)")
if temp == "Y" or temp == "y" or temp == None:
    nomeConjuge = input("Qual o nome do conjuge?: ")
    apelidoConjuge = input("Qual o apelido do conjuge?: ")
    nickConjuge = input("Principal nick (@) conjuge")
    anoConjuge = input("Ano que o conjuge nasceu: ")
    mesConjuge = input("Mês que o conjuge nasceu: ")
    diaConjuge = input("Dia que o conjuge nasceu: ")
    trabalhoConjuge = input("Local de trabalho do conjuge: ")
    cargoConjuge = input("Cargo do conjuge:")
    anoConjugeNamoro = input("Ano que começaram a namorar: ")
    mesConjugeNamoro = input("Mes que começaram a namorar: ")
    diaConjugeNamoro = input("Dia que começaram a namorar: ")
    
temp2 = input("Casados? (Y/n)")
if temp2 == "Y" or temp2 == "y" or temp2 == None:
    print("Teste")
    
temp3 = input("Possuem filhos? (Y/n)")
if temp3 == "Y" or temp3 == "y" or temp3 == None:
    qntd = input("Quantidade de filhos: ")
    for i in range(qntd):
        nomeFilho = input("Nome do filho {i}")
        NickFilho = input("Principal nick (@) do filho {i}")
        anoNiverFilho = input("Ano que nasceu (número) o filho {i}: ")
        mesNiverFilho = input("Mês que nasceu (número) o filho {i}: ")
        diaNiverFilho = input("Dia que nasceu (número) o filho {i}: ")
        apelidoFilho = input("Apelido do filho {i}")
        
temp4 = input("Teve algum pet? (Y/n)")
if temp4 == "Y" or temp4 == "y" or temp4 == None:
    qntd = input("Quantidade de pets: ")
    for i in range(qntd):
        nomePet = input("Nome do pet {i}")
        anoNiverPet = input("Ano que nasceu (número) o filho {i}: ")
        mesNiverPet = input("Mês que nasceu (número) o filho {i}: ")
        diaNiverPet = input("Dia que nasceu (número) o filho {i}: ")
        apelidoPet = input("Especie do pet {i}")
        racaPet = input("Raça do pet:")
        
temp5 = input("Teve algum carro (Y/n)")
if temp5 == "Y" or temp5 == "y" or temp5 == None:
    qntd = input("Quantidade de carros: ")
    for i in range(qntd):
        nomePet = input("Placa do carro {i}")

print("Outras palavras que podem ser relevantes: (Pressione enter para sair)")
while (True):
    update = 1
    palavra1 = input("Palavra {update}: ")
    update = update + 1
    if (palavra1 == None):
        break
    

qtdPalavras = input("Teste")
numRandom = input("Teste")
substituirLetrasNumeros = input("Teste")
caracteresEspeciais = input("Teste")