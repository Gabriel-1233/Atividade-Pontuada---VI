import os
from dataclasses import dataclass
os.system("cls || clear")

# Função para limpar a tela
def limpa_tela():
    os.system("cls || clear")

# Dataclass para armazenar informações das pessoas
@dataclass
class Pessoas:
    sexo: str
    idade: int
    salario: float

# Lista para armazenar os dados das pessoas
lista_pessoas = []
QUANTIDADE_PESSOAS = 2  # Defina a quantidade de pessoas que você deseja adicionar

# Verdadeiro começo do código
print("""
Código || Descrição
1 - Adicionar habitante
2 - Exibir dados
""")
opcao = int(input("Digite a opção de sua escolha: "))
match opcao:
    case 1:
        limpa_tela()
        print("=== Recolhendo seus dados ===")
        
        for _ in range(QUANTIDADE_PESSOAS):
            habitantes = Pessoas(
                sexo=input("Digite seu sexo (M=masculino, F=feminino): "),
                idade=int(input("Digite sua idade: ")),
                salario=float(input("Digite seu salário: "))
            )
            lista_pessoas.append(habitantes)

            # Gravar os dados no arquivo
            nome_do_arquivo = "carteira_de_clientes.txt"
            with open(nome_do_arquivo, "a") as arquivo:
                arquivo.write(f"{habitantes.sexo},{habitantes.idade},{habitantes.salario}\n")

    case 2:
        limpa_tela()

        if not lista_pessoas:
            print("Nenhum habitante cadastrado.")
        else:
            total_pessoas = len(lista_pessoas)
            maior_idade = max(habitante.idade for habitante in lista_pessoas)
            menor_idade = min(habitante.idade for habitante in lista_pessoas)
            total_salario = sum(habitante.salario for habitante in lista_pessoas)
            media_salario = total_salario / total_pessoas

            # Contar quantas mulheres têm salário a partir de R$ 5.000
            quantidade_mulheres = sum(1 for habitante in lista_pessoas if habitante.sexo == 'F' and habitante.salario >= 5000)

            print(f"O total de habitantes: {total_pessoas}")
            print(f"O habitante mais velho tem: {maior_idade} anos")
            print(f"O habitante mais novo tem: {menor_idade} anos")
            print(f"A média do salário por habitante: R$ {media_salario:.2f}")
            print(f"Quantidade de mulheres com salário a partir de R$ 5.000: {quantidade_mulheres}")
