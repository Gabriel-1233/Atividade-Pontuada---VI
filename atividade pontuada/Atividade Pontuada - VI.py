import os
from dataclasses import dataclass
os.system("cls || clear")

#função
def limpa_tela():
    os.system("cls || clear")
    
#dataclass
@dataclass
class Pessoas:
    sexo:str
    idade:int
    salario:float

#lista e constante.
lista_pessoas=[] 
QUANTIDADE_PESSOAS=2 

#verdadeiro começo do código.
print("""
Código || Descerição
1-Adicionar habitante
2-Exibir dados
  """)
opcao=int(input("Digite a opção de sua escolha:"))
match(opcao):
    case 1:
        limpa_tela()
        print("===Recolhendo seus dados===")
        habitantes=Pessoas(
            sexo=input("Digite seu sexo(M=masculino,F=feminino):"),
            idade=int(input("Digite sua idade:")),
            salario=float(input("Digite seu salario:"))
        )
        lista_pessoas.append(habitantes)
#nome do arquivo e seu processamento.
        nome_do_arquivo="carteira_de_clientes.txt"
        with open(nome_do_arquivo, "a") as arquivos_alunos:
            for aluno in lista_pessoas:
                arquivos_alunos.write(f"{habitantes.sexo},{aluno.idade},{habitantes.salario}\n")
#fechar arquivo, para desligar a utilização do poder de computação.
                arquivos_alunos.close()
    case 2:
        limpa_tela()
        total_pessoas=QUANTIDADE_PESSOAS
        salario_pessoal=len(habitantes.salario for habitantes in lista_pessoas)
        maior_idade=max(habitantes.idade for habitantes in lista_pessoas)
        menor_idade=min(habitantes.idade for habitantes in lista_pessoas)
        salario=sum(habitantes.salrio for habitantes in lista_pessoas )
        media_salario=salario/total_pessoas

        print(f"O total de habitantes:{total_pessoas}")
        print(f"O seu salario:{salario_pessoal}")
        print(f"O habitante mais velho:{maior_idade}")
        print(f"O habitante mais novo:{menor_idade}")
        print(f"A media do salario por habitante:{media_salario}")
