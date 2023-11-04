#Definição de variável inicial responsável por armazenar os valores que o usuário inserir
listaInicial = []

#Definição da função responsável por avaliar se um número é primo ou não ao verificar se é acima de 1 e se entre ele e 2 existem outros números que poderiam perfeitamente o dividir
def localizarPrimo(num):
    if num <= 1:
        return False 
    for aux in range(2, int(num)):
        if num%aux == 0: 
            return False 
    return True 
            
#Função responsável por inserir o digito específico, caso ele passe pela função "localizarPrimo", em uma nova lista "listaFinal"
def agruparPrimos(listaInicial):
    listaFinal = []
    for aux in listaInicial:
        if localizarPrimo(aux):
            listaFinal.append(aux)
    return listaFinal 

#Trecho responsável por permitir que o usuário insira quantos valores ele desejar na lista até "fechá-la"
while True: 
    digito = input("Digite um valor.\nInsira 'f' para finalizar a lista.")
    if digito == 'f':
        break 
    if digito.isdigit():
        digito = int(digito)
        listaInicial.append(digito)
    else:
        print("Insira um valor válido para a inclusão na lista.")
        
#Chamada da função responsável por agrupar os primos na lista inicial
primosEncontrados = agruparPrimos(listaInicial)
#Impressão dos primos encontrados 
print(primosEncontrados)