#Definição da variável "listaInicial" que fornecerá a lista pré-estabelecida especificada no enunciado
listaInicial = [2, 3, 5, 6, 9, 12]

#Definição da função que atenderá ao requisitado no enunciado. Começa estabelecendo os valores das variáveis
#que acabam por não serem muito relevantes por serem rapidamente alterados ao passarem pelo laço de repetição "for"
#que compara o valor de "aux", sendo ele a iteração do elementos em lista, e analisando se é maior que "maiorNum",
#em caso afirmativo substituindo o seu valor por "aux" enquanto segundoMaiorNum, antes dessa linha, altera 
#seu valor para "maiorNum" que ainda não estaria "atualizado" para o maior número encontrado por essa linha 
#só vir depois, encontrando assim o segundo maior número 
def EncontrarSegMaiorValor(lista):
    maiorNum = lista[0]
    segundoMaiorNum = 0
    for aux in lista: 
        if aux > maiorNum: 
            segundoMaiorNum = maiorNum 
            maiorNum = aux
    return segundoMaiorNum 
    
print(EncontrarSegMaiorValor(listaInicial))
        