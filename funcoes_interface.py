def separacao(*texto, sep='─', tam=50, comp=True):
    if comp:
        print(sep * tam)
        for i, frase in enumerate(texto):
            if i == 0:
                print(frase.center(tam).upper())
            else:
                print(frase.center(tam))
        print(sep * tam)
    else:
        for i, frase in enumerate(texto):
            if i == 0:
                print(frase.center(tam).upper())
            else:
                print(frase.center(tam))
        print(sep * tam)


def cabecalho():
    separacao('pesquisador de mangás')


def rodape():
    separacao('programa encerrado!', 'Obrigado por utilizar o pesquisador de mangás!')
    

def opcoes_conta():
    separacao('opções de conta', 'O que gostaria de fazer? ')
    print('''    [ 1 ] → Fazer login
    [ 2 ] → Criar nova conta
    [ 3 ] → Redefinir minha senha
    [ 4 ] → Mudar avatar
    [ 5 ] → Voltar para tela inicial
    [ 6 ] → Encerrar o Programa
    [999] → EXCLUIR MINHA CONTA PERMANENTEMENTE
    ''')
    escolha = int(input('Digite o número da opção escolhida: '))

    while True:
    

def inicial():
    separacao('Bem vindo ao leitor de mangás')
    separacao('O que você gostaria de fazer?', sep='·', comp=False)
    print('''    [1] → Fazer login\n
    [2] → Criar uma nova conta\n
    [3] → Ver todas as opções da conta\n
    [4] → Encerrar Programa''') 
    print('·' * 50)
    escolha = int(input('Digite a opção desejada: '))

    while escolha not in range(1, 5):
        print('ERRO! Opção inválida!')
        escolha = int(input('Digite novamente a opção desejada: '))

    if escolha == 1:
        pass
    elif escolha == 2:
        from funcoes_banco import registro
        separacao('criar uma nova conta')
        reg = registro()
        if reg == True:
            separacao('Conta cadastrada com sucesso!', sep = '*')
            inicial()
        else:
            print('Ouve algum erro, tente novamente!')
    elif escolha == 3:
        pass
    else:
        rodape()

    
if __name__ == '__main__':
   opcoes_conta()
