#Definição de variáveis associadas às listas que serão recebidas pela função 
primeiraLista = []
segundaLista = []

#Definição da função encarregada de formar as duas listas ao receber continuamente os digitos fornecidos
#pelos inputs do usuário até o mesmo finalizar o processo ao teclar 'f'. Após isso, inicia uma verificação
#averiguando se o valor não está em alguma das duas listas, e, em caso afirmativo, adiciona o digito à
#"listaFinal", que é a que será de fato retornada ao usuário
def ReceberListas(pListaInicial, sListaInicial):
    listaFinal = []
    for aux in range (1, 3):
        if aux == 1:
            lista = pListaInicial
        else:
            lista = sListaInicial
        while True: 
            digito = input("Insira os números da lista correspondente.\nAperte 'f' para completar a lista.")
            if digito == 'f':
                break 
            if digito.isdigit():
                digito = int(digito)
                lista.append(digito)
            else:
                print("Insira um valor válido para a inclusão na lista.")
    # Verifica se o valor não está em pListaInicial ou não está em sListaInicial ou já está em listaFinal
    for valor in pListaInicial + sListaInicial:
        if valor not in pListaInicial or valor not in sListaInicial or valor in listaFinal:
            listaFinal.append(valor)
            
    return listaFinal 

print(ReceberListas(primeiraLista, segundaLista)) 
        