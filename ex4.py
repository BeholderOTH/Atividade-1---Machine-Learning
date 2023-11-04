#Recebe elementos fornecidos pelo usuário com um único input 
entrada = input("Insira os nomes seguidos das idades das pessoas e os separe com um ; para preencher a lista.")
#Separa o "input" recebido em vários elementos de uma lista de acordo com a separação deles por ";" dentro do fornecido
tuplaFormada = entrada.split(';')
#Estabelece a tuplaFinal, que efetua diversos papéis de uma só vez, apagando espaços em branco antes e depois
#dos elementos presentes e depois define a tupla ao fornecer os dados em relação ao seu tamanho e quantidade
#de elementos, o que define por meio de um laço de repetição "for" e a int de tuplaFormada que se baseia em
#"aux" para iterar sob os elementos e determinar seus números/tamanhos
tuplaFinal = [(tuplaFormada[aux].strip(), int(tuplaFormada[aux+1])) for aux in range(0, len(tuplaFormada), 2)]

#Definição de função associada à ordenação de lista requisitada no enunciado, recebendo uma lista e 
#devolvendo outra "ordenada" por meio de uma simples função "sorted" 
def ordenarLista(tuplaAlvo):
    tuplaOrd = tuple(sorted(tuplaAlvo))
    return tuplaOrd

#Imprime a lista organizada em ordem alfabética através da função "ordenarLista" pré-definida
print("Lista organizada em ordem alfabética:", ordenarLista(tuplaFinal))