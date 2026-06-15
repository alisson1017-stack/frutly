import subprocess
import re


dic_meses = {'Janeiro':{'0001':{'vendas':111}, '0002':{'vendas':222}, '0003':{'vendas':333}, '0004':{'vendas':444}},
             'Fevereiro':{'0001':{'vendas':111}, '0002':{'vendas':222}, '0003':{'vendas':333}, '0004':{'vendas':444}},
             'Março':{'0001':{'vendas':0}, '0002':{'vendas':0}, '0003':{'vendas':0}, '0004':{'vendas':0}}}

dic_frutas = {'0001':{'nome':'Banana', 'id':'0001', 'valor':111.1, 'margem':0.1},
              '0002':{'nome':'Maçã', 'id':'0002', 'valor':222.2, 'margem':0.2},
              '0003':{'nome':'Morango', 'id':'0003', 'valor':333.3, 'margem':0.3},
              '0004':{'nome':'Laranja', 'id':'0004', 'valor':44, 'margem':0.4}}

select_mes = []
select_fruta = []

def main():
    exibir_menu_principal()
    select_menu_principal()

def exibir_menu_principal():
    exibir_titulo()
    exibir_subtitulo('Menu Principal')

    print('\n1. Listar frutas')
    print('2. Listar Meses')
    print('3. Editar frutas')
    print('4. Editar meses')
    print('5. Comparar')
    print('6. Sair\n')

def select_menu_principal():
    try:
        selecao = int(input('\nSelecione uma opção: '))
        match selecao:
            case 1:
                listar_frutas()
            case 2:
                listar_meses()
            case 3:
                editar_frutas()
            case 4:
                editar_meses()
            case 5:
                comparar()
            case 6:
                print('\nVocê selecionou: 6. Sair')
            case _:
                limpar_tela()
                print('\nOpção inválida.')
                exibir_menu_principal()
                select_menu_principal()
    except:
        limpar_tela()
        print('\nOpção inválida.')
        voltar_pro_menu()

def limpar_tela():
    subprocess.run('cls', shell=True)

def exibir_titulo():
    limpar_tela()
    print(f'''
    {'-'*28}
            🅵 🆁 🆄 🆃 🅻 🆈
    {'-'*28}
    ''')

def exibir_subtitulo(texto):
    print(f'''          {texto}
    {'-' * 28}\n''')

def voltar_pro_menu():
    input('\nPressione "Enter" para voltar ao menu principal\n')
    return main()


def listar_frutas():
    exibir_lista_frutas()
    voltar_pro_menu()

def print_header_fruta():
    print(f'''
{'nome'.ljust(15)} | {'ID'.ljust(8)} | {'Valor'.ljust(8)} | Margem de lucro
{'-' * 60}''')

def exibir_lista_frutas():
    exibir_titulo()
    exibir_subtitulo('Lista de Frutas')

    print_header_fruta()
    
    for fruta in dic_frutas:
        margem = float(query_info_fruta(fruta, 'margem')) * 100
        print(f'{exibir_info_fruta(fruta,'nome', 15)} | {exibir_info_fruta(fruta,'id', 8)} | {exibir_info_fruta(fruta,'valor', 8)} | {int(margem)}%')

def query_info_fruta(id_fruta, campo):
    return f'{dic_frutas[f'{id_fruta}'][f'{campo}']}'

def exibir_info_fruta(id_fruta, campo, espacamento):
    info = query_info_fruta(f'{id_fruta}',f'{campo}')
    return str(info).ljust(espacamento)


def listar_meses():
    exibir_menu_listar_meses()
    select_menu_listar_meses()
    voltar_pro_menu()

def exibir_menu_listar_meses():
    exibir_titulo()
    exibir_titulo()
    select_mes.clear()
    exibir_subtitulo('Listar Meses')
    i = 0
    for mes in dic_meses:
        i += 1
        select_mes.append(mes)
        print(f'{i}. {mes}')
    print(f'\n{i + 1}. Voltar\n')

def select_menu_listar_meses():
    try:
        selecao = int(input('Selecione uma opção: '))
        if selecao == (len(select_mes) + 1):
            return main()
        elif selecao <= len(select_mes):
            index = selecao - 1
            mes_selecionado = select_mes[index]
            return exibir_mes_selecionado(mes_selecionado)
        else:
            print('\n-> Opção inválida <-')
            input('\n\nAperte "Enter" para tentar de novo.')
            return listar_meses()
    except:
        print('\n-> Opção inválida <-')
        input('\n\nAperte "Enter" para tentar de novo.')
        return listar_meses()

def exibir_mes_selecionado(mes):
    exibir_titulo()
    exibir_subtitulo(f'   {mes.upper()}')
    print(f'''\n{'Fruta'.ljust(15)} | Qnt. vendida
{'-' * 60}''')
    quantidade = 0
    entrada = 0
    for id in dic_meses[mes]:
        print(f'{(dic_frutas[id]['nome']).ljust(15)} | {dic_meses[mes][id]['vendas']}')

        quantidade += dic_meses[mes][id]['vendas']
        entrada += float(query_info_fruta(id, 'valor')) * int(dic_meses[mes][id]['vendas'])

    print(f'Frutas vendidas: {quantidade:,}   Entrada total: R${entrada:,.2f}')
    input('\nAperte "Enter" para voltar.')
    return listar_meses()

def query_info_mes(mes, campo):
    return f'{dic_meses[f'{mes}'][f'{campo}']}'


def editar_frutas():
    exibir_menu_editar_frutas()
    select_menu_editar_frutas()

def exibir_menu_editar_frutas():
    # select_fruta.clear()
    exibir_titulo()
    exibir_subtitulo('Editar frutas')

    print('''
1. Adicionar fruta
2. Remover fruta
3. Editar fruta
\n4. Voltar''')

    return select_menu_editar_frutas()
    
def select_menu_editar_frutas():
    try:
        selecao = int(input('\nSelecione uma opção: '))
        match selecao:
            case 1:
                return adicionar_fruta()
            case 2:
                remover_fruta()
            case 3:
                editar_info_fruta()
            case 4:
                return main()
            case _:
                print('\nOpção inválida.')
                input('\nPressione "Enter" para tentar novamente.')
                return main()
    except:
        print('\nOpção inválida.')
        input('\nPressione "Enter" para tentar novamente.')
        return editar_frutas()


def adicionar_fruta():
    '''Essa função recebe como inputs:
    1: nome na fruta, 2. valor da fruta, 3. margem da fruta
    
    Depois disso ela:
    1. Cria um ID único (ID da última fruta + 1)
    2. Adiciona a nova fruta e suas informações ao dic_frutas e dic_meses
    3. Confirma a criação da nova fruta e mostra suas informações.'''

    exibir_titulo()
    exibir_subtitulo('Adicionar nova fruta')

    fruta = input('\nDigite o nome da fruta: ')
    if fruta == '':
        input('\nCampo obrigatório! Aperte "Enter" para tentar novamente.')
        return adicionar_fruta()
    else:
        valor = get_valor_fruta()
        margem = get_margem_fruta()

        id_ultima_fruta = int(next(reversed(dic_frutas))) 
        id_fruta = f'{(id_ultima_fruta + 1):04d}'
        dic_frutas[id_fruta] = {'nome': fruta, 'id': id_fruta, 'valor': valor, 'margem': margem}

        for mes in dic_meses:
            dic_meses[mes][id_fruta] ={'vendas':0}
        print(f'\nA fruta {fruta} foi adicionada com sucesso!')
        print(f'''
{'nome'.ljust(15)} | {'ID'.ljust(8)} | {'Valor'.ljust(8)} | Margem de lucro
{'-' * 60}''')
        
        margem = float(query_info_fruta(id_fruta, 'margem')) * 100
        print(f'{exibir_info_fruta(id_fruta,'nome', 15)} | {exibir_info_fruta(id_fruta,'id', 8)} | {exibir_info_fruta(id_fruta,'valor', 8)} | {int(margem)}%')
        input('\nAperte "Enter" para continuar.')
        return editar_frutas()
    
def get_valor_fruta():
    try:
        valor = float(input('\nDigite o valor da fruta: '))
        return valor
    except:
        input('\nValor inválido! Aperte "Enter" para tentar novamente.')
        return get_valor_fruta()

    
def get_margem_fruta():
    try:
        margem = float(input('\nDigite a margem de lucro da fruta em números decimais(0.1 = 10%): '))
        if 1 > margem > 0:
            return margem
        else:
            input('\n   ~ A margem deve ser in número entre 0 e 1!\nAperte "Enter" para tentar novamente.')
            return get_margem_fruta()

    except:
        input('\nValor inválido! Aperte "Enter" para tentar novamente.')
        return get_margem_fruta()

def remover_fruta():
    exibir_menu_remover_fruta()
    select_menu_remover_fruta()
    

def exibir_menu_remover_fruta():
    exibir_titulo()
    exibir_subtitulo('Remover Fruta')
    print('''
1. Buscar fruta por nome
2. Buscar fruta por ID
3. Listar todas as frutas
\n4. Voltar
''')

def select_menu_remover_fruta():
    try:
        selecao = int(input('\nSelecione uma opção: '))
        match selecao:
            case 1:
                return buscar_fruta_por_nome()
            case 2:
                return buscar_fruta_por_id()
            case 3:
                exibir_lista_frutas()
                input('\nAperte "Enter" para voltar.')
                return remover_fruta()
            case 4:
                return editar_frutas()
            case _:
                print('\nOpção inválida.')
                input('\nPressione "Enter" para tentar novamente.')
                return remover_fruta()
    except:
        print('\nOpção inválida.')
        input('\nPressione "Enter" para tentar novamente.')
        return remover_fruta()

def buscar_fruta_por_nome():
    exibir_titulo()
    exibir_subtitulo('Remover fruta')
    try:
        busca = input('\nDigite o nome da fruta: ')
        for frutas in dic_frutas:
            if busca == dic_frutas[frutas]['nome']:
                # print(f'Fruta encontrada! {frutas}')
                fruta = frutas
                break
        confirmacao = input(f'''\nDeseja remover a fruta {dic_frutas[fruta]['nome']}?

1.Confirmar
2.Cancelar
                            
: ''')
        match confirmacao:
            case '1':
                del dic_frutas[fruta]
                input('\nFruta removida com sucesso.\nPressione "Enter" para continuar')
                return remover_fruta()
            case '2':
                return remover_fruta()
    except:
        input('\n   ~Fruta não encontrada!\n    Pressione "Enter" para voltar.')
        return remover_fruta()

def buscar_fruta_por_id():
    exibir_titulo()
    exibir_subtitulo('Remover fruta')
    try:
        busca = input('\nDigite o ID da fruta: ')
        for frutas in dic_frutas:
            if busca == dic_frutas[frutas]['id']:
                # print(f'Fruta encontrada! {frutas}')
                fruta = frutas
                break
        confirmacao = input(f'''\nDeseja remover a fruta {dic_frutas[fruta]['nome']}?

1.Confirmar
2.Cancelar
                            
: ''')
        match confirmacao:
            case '1':
                del dic_frutas[fruta]
                input('\nFruta removida com sucesso.\nPressione "Enter" para continuar')
                return remover_fruta()
            case '2':
                return remover_fruta()
    except:
        input('\n   ~Fruta não encontrada!\n    Pressione "Enter" para voltar.')
        return remover_fruta()


def editar_info_fruta():
    exibir_menu_editar_info_fruta()
    select_menu_editar_info_fruta()
    
def exibir_menu_editar_info_fruta():
    exibir_titulo()
    exibir_subtitulo('Editar Fruta')
    print('''\nEscolha fruta que deseja editar

1. Escolher fruta por nome
2. Escolher fruta por ID
3. Listar todas as frutas
\n4. Voltar  
''')

def select_menu_editar_info_fruta():
    try:
        escolha = input('\nEscolha uma opção: ')
        match escolha:
            case '1':
                return editar_fruta_por_nome()
            case '2':
                return editar_fruta_por_id()
            case '3':
                exibir_lista_frutas()
                input('\nAperte "Enter" para voltar.')
                return editar_info_fruta()
            case '4':
                return editar_info_fruta()
            case _:
                print('funcao()')
                input('\nOpção Inválida. Pressione "Enter" para tentar novamente.')
                return editar_info_fruta()
    except:
        input('\nOpção Inválida. Pressione "Enter" para tentar novamente.')
        return editar_info_fruta()

def editar_fruta_por_nome():
    exibir_titulo()
    exibir_subtitulo('Editar fruta')
    try:
        busca = input('\nDigite o nome da fruta: ')
        for frutas in dic_frutas:
            if busca == dic_frutas[frutas]['nome']:
                fruta = frutas
                break
        confirmacao = input(f'''\nDeseja editar a fruta {dic_frutas[fruta]['nome']}?

1.Confirmar
2.Cancelar
                            
: ''')
        match confirmacao:
            case '1':
                return editar_a_fruta(fruta)
            case '2':
                return editar_info_fruta()
    except:
        input('\n   ~Fruta não encontrada!\n    Pressione "Enter" para voltar.')
        return editar_info_fruta()

def editar_a_fruta(fruta):
    exibir_titulo()
    exibir_subtitulo(f'Editando {dic_frutas[fruta]['nome']}')
    escolha = input('''Escolha a informação que deseja editar:
1. Nome da fruta
2. Valor da fruta
3. Margem de lucro da fruta
4. Cancelar
''')
    match escolha:
        case '1':
            return mudar_nome_fruta(fruta)
        case '2':
            return mudar_valor_fruta(fruta)
        case '3':
            return mudar_margem_fruta(fruta)
        case '4':
            return editar_info_fruta()
        case _:
            input('\nOpção inválida. Aperte "Enter" para tentar novamente.')
            return editar_a_fruta(fruta)

def mudar_nome_fruta(fruta):
    exibir_titulo()
    exibir_subtitulo(f'Editando {dic_frutas[fruta]['nome']}')
    nome = input(f'Digite o novo nome da fruta {dic_frutas[fruta]['nome']}: ')
    dic_frutas[fruta]['nome'] = nome
    
    print('\nAlteração realizada com sucesso!')
    print_header_fruta()
    margem = float(query_info_fruta(fruta, 'margem')) * 100
    print(f'{exibir_info_fruta(fruta,'nome', 15)} | {exibir_info_fruta(fruta,'id', 8)} | {exibir_info_fruta(fruta,'valor', 8)} | {int(margem)}%')
    input('\nPressione "Enter" para continuar.')
    return editar_frutas()

def get_valor_fruta_edicao():
        valor = (input('\nDigite o novo valor da fruta ou "x" para cancelar: '))
        if valor == 'x':
            return None
        else:
            try:
                valor = float(valor)
                return valor
            except:
                input('\nValor inválido! Aperte "Enter" para tentar novamente.')
                return get_valor_fruta()

def mudar_valor_fruta(fruta):
    exibir_titulo()
    exibir_subtitulo(f'Editando {dic_frutas[fruta]['nome']}')

    valor = get_valor_fruta_edicao()
    if valor == None:
        return editar_a_fruta(fruta)
    
    dic_frutas[fruta]['valor'] = valor
    
    print('\nAlteração realizada com sucesso!')
    print_header_fruta()
    margem = float(query_info_fruta(fruta, 'margem')) * 100
    print(f'{exibir_info_fruta(fruta,'nome', 15)} | {exibir_info_fruta(fruta,'id', 8)} | {exibir_info_fruta(fruta,'valor', 8)} | {int(margem)}%')
    input('\nPressione "Enter" para continuar.')
    return editar_frutas()

def get_margem_fruta_edicao():
    margem = (input('\nDigite o novo valor da fruta ou "x" para cancelar: '))
    if margem == 'x':
        return None
    else:
        try:
            margem = float(margem)
            if 1 > margem > 0:
                return margem
            else:
                input('\n   ~ A margem deve ser in número entre 0 e 1!\nAperte "Enter" para tentar novamente.')
                return get_margem_fruta()
        except:
            input('\nValor inválido! Aperte "Enter" para tentar novamente.')
            return get_margem_fruta()

def mudar_margem_fruta(fruta):
    margem = get_margem_fruta()
    if margem == None:
        return editar_a_fruta(fruta)
    
    dic_frutas[fruta]['margem'] = margem
    
    print('\nAlteração realizada com sucesso!')
    print_header_fruta()
    margem = float(query_info_fruta(fruta, 'margem')) * 100
    print(f'{exibir_info_fruta(fruta,'nome', 15)} | {exibir_info_fruta(fruta,'id', 8)} | {exibir_info_fruta(fruta,'valor', 8)} | {int(margem)}%')
    input('\nPressione "Enter" para continuar.')
    return editar_frutas()

def editar_fruta_por_id():
    exibir_titulo()
    exibir_subtitulo('Editar fruta')
    try:
        fruta = input('\nDigite o ID da fruta: ') 
        confirmacao = input(f'''\nDeseja editar a fruta {dic_frutas[fruta]['nome']}?

1.Confirmar
2.Cancelar
                            
: ''')
        match confirmacao:
            case '1':
                return editar_a_fruta(fruta)
            case '2':
                return editar_frutas()
    except:
        input('\n   ~Fruta não encontrada!\n    Pressione "Enter" para voltar.')
        return editar_info_fruta()


def editar_meses():
    exibir_titulo()
    exibir_subtitulo('Editar mês')
    
    print('\nEscolha um mês para editar:\n')
    i = 1
    selecao_meses = {}
    print(f'\n1. Adicionar mês\n')
    
    for mes in dic_meses:
        i += 1
        selecao_meses[i] = mes
        print(f'{i}. {mes}')
    print(f'\n{i + 1}. Voltar')
    try:
        escolha = int(input('\nDigite o número do mês escolhido: '))
        if escolha in selecao_meses:
            mes = selecao_meses[escolha]
            # print(f'-monitoramento- mês: {mes}') <- MONITORAMENTO
            return select_menu_editar_meses(mes)
        elif escolha == 1:
            return adicionar_mes()
        elif escolha == i + 1:
            return main() 
        else:
            ('    ~ Opção inválida.\nAperte "Enter" para tentar novamente.')
            return editar_meses()
    except:
        input('    ~ Opção inválida.\nAperte "Enter" para tentar novamente.')
        return editar_meses()

def adicionar_mes():
    exibir_titulo()
    exibir_subtitulo('Adicionar mês')
    novo_mes = input('\nDigite o nome do mês a ser adicionado, ou "x" para cancelar: ')
    if novo_mes == 'x':
        return editar_meses()
    elif novo_mes in dic_meses:
        input(f'\n  ~ O mês {novo_mes} já existe!\nPressione "Enter" para tentar novamente.')
        return adicionar_mes()
    elif not novo_mes:
        input(f'\nNome em branco, pressione "Enter" para tentar novamente.')
        return adicionar_mes()
    else:
        return confirma_adicionar_mes(novo_mes)

def confirma_adicionar_mes(mes):
    exibir_titulo()
    exibir_subtitulo('Adicionar mês')
    try:
        escolha = input(f'''\nTem certeza de que quer adicionar o mês {mes}?
\n1. Sim
2. Cancelar

 : ''')
        match escolha:
            case '1':
                dic_meses[mes] = {}
                for fruta in dic_frutas:
                    dic_meses[mes][fruta] = {}
                    dic_meses[mes][fruta]['vendas'] = 0
                # print(f'\nmonitoramento:\n{dic_meses[mes]}') <-MONITORAMENTO
                print(f'\nO mês {mes} foi adicionado com sucesso!')
                input(f'\nAperte "Enter para voltar.')
                return editar_meses()
            case '2':
                return adicionar_mes()
            case _:
                print('\n   ~ Opção inválida!')
                input('\nPressione "Enter" para tentar novamente.')
                return confirma_adicionar_mes(mes)
    except:
        input('\n   ~ Opção inválida.\nPressione "Enter" para tentar novamente.')
        return confirma_adicionar_mes(mes)

def select_menu_editar_meses(mes):
    exibir_titulo()
    exibir_subtitulo(f'Editando {mes}')
    try:
        selecao = input(f'''
    1. Remover {mes}
    2. Alterar nome
    3. Editar número de vendas

    4. Cancelar
\n    Selecione uma opção: ''')
        match selecao:
            case '1':
                return remover_mes(mes)
            case '2':
                return alterar_nome_mes(mes)
            case '3':
                return editar_vendas_mes(mes)
            case '4':
                return editar_meses()
            case _:
                input('\n   ~ Opção inválida!\nAperte "Enter" para tentar novamente.')
                return select_menu_editar_meses(mes)
    except:
        input('\n   ~ Opção inválida!\nAperte "Enter" para tentar novamente.')
        return select_menu_editar_meses(mes)

def remover_mes(mes):
    try:
        exibir_titulo()
        exibir_subtitulo(f'Remover {mes}')
        escolha = input(f'Tem certeza de que quer remover o mês {mes}?\n\n1. Sim\n2.Cancelar\n: ')
        match escolha:
            case '1':
                del dic_meses[mes]
                print(f'\nO mês {mes} foi removido com sucesso.')
                input('\nPressione "Enter" para voltar.')
                return editar_meses()
            case '2':
                return select_menu_editar_meses(mes)
            case _:
                input('\nOpção inválida. Pressione "Enter" para tentar novamente') 
                return remover_mes(mes)
    except:
        input('\nOpção inválida. Pressione "Enter" para tentar novamente') 
        return remover_mes(mes)

def alterar_nome_mes(mes):
    nome = input(f'\nEscreva o novo nome do mês {mes}: ')
    escolha = input(f'Mudar o mês "{mes}" para "{nome}"?\n\n1. Sim\n2.Cancelar\n: ')
    match escolha:
        case '1':
            dic_meses[nome] = dic_meses.pop(mes)
            # print(f'\nmonitoramento:\n{dic_meses}') # <- monitoramento
            print(f'\nMês renomeado com sucesso.')
            input('\nPressione "Enter" para voltar.')
            return editar_meses()
        case '2':
            return editar_meses()
        case _:
            input('\nOpção inválida. Pressione "Enter" para tentar novamente') 
            return alterar_nome_mes(mes)

def editar_vendas_mes(mes):
    exibir_titulo()
    exibir_subtitulo(f'Vendas de {mes}')
    i = 1
    selecao = {}
    for fruta in dic_frutas:
        selecao[i] = fruta
        print(f'{i}. {dic_frutas[fruta]['nome']}')
        i += 1
    try:
        escolha = int(input('\nDigite o número da fruta que deseja alterar: '))
        fruta = selecao[escolha]
        if escolha in selecao:
            print(f'\nNúmero de vendas da fruta {dic_frutas[fruta]['nome']}: {dic_meses[mes][fruta]['vendas']}:')
            novo_valor = input('\nDigite o novo valor, ou "x" para cancelar: ')
            if novo_valor == 'x':
                return select_menu_editar_meses(mes)
            elif 0 < int(novo_valor):
                dic_meses[mes][fruta]['vendas'] = novo_valor
                print('\nValor atualizado com sucesso!')
                input('\nPressione "Enter" para voltar.')
                return select_menu_editar_meses(mes)
            else:
                print('\n   ~ Opção inválida!')
                input('Pressione "Enter para tentar novamente.')
                return editar_vendas_mes(mes)
                
        
    except:
        print('\n   ~ Opção inválida!')
        input('Pressione "Enter para tentar novamente.')
        return editar_vendas_mes(mes)

def comparar():
    exibir_titulo()
    exibir_subtitulo('Comparar')
    print('''
1. Comparar frutas
2. Comparar meses

3. Voltar
''')
    escolha = input('\nEscolha uma opção: ')
    match escolha:
        case '1':
            return comparar_frutas()
        case '2':
            input('\nEm desenvolvimento.')
            return main()
            # return comparar_meses()
        case '3':
            return main()
        case _:
            print('\n   ~ Opção Inválida!')
            input('\nPressione "Enter" para tentar novamente.')
            return comparar()
    print('\nEm desenvolvimento.')
    input('\nAperte "Enter" para continuar.')
    return main()


def escolha_fruta_b(fruta_a):
    fruta_b = input('\nDigite o nome da segunda fruta, ou "x" para cancelar: ')
    if fruta_b == 'x':
        return comparar()
    else:
        for fruta in dic_frutas:
            if fruta_b == dic_frutas[fruta]['nome']:
                return fruta
            else:
                continue
        print('\n   ~ Fruta não encontrada.')
        input('\nPressione "Enter" para tentar novamente.')
        exibir_titulo()
        exibir_subtitulo('Comparar frutas')
        print(f'\n  - {fruta_a}')
        return(escolha_fruta_b(fruta_a))

def comparar_frutas():
    exibir_titulo()
    exibir_subtitulo('Comparar frutas')
    fruta_a = input('\nDigite o nome da primeira fruta, ou "x" para cancelar: ')
    fruta_encontrada = False
    if fruta_a == 'x':
        return comparar()
    else:
        for fruta in dic_frutas:
            if fruta_a == dic_frutas[fruta]['nome']:
                exibir_titulo()
                exibir_subtitulo('Comparar frutas')
                print(f'\n  - {fruta_a}')
                id_fruta_a = fruta
                fruta_encontrada = True
                break
            else:
                continue
    if fruta_encontrada:
        id_fruta_b = escolha_fruta_b(fruta_a)
        try:
            exibir_resultado_comparacao(id_fruta_a, id_fruta_b)
            input('\nAperte "Enter".')
            return comparar()
        except:
            print('\n   ~Ocorreu um erro')
            input('\nAperte "Enter".')
            return comparar_frutas()
    else:
        print('\n   ~ Fruta não encontrada.')
        input('\nPressione "Enter" para tentar novamente.')
        return comparar_frutas()

def exibir_resultado_comparacao(fruta_a, fruta_b):
    print(f'''
{dic_frutas[fruta_a]['nome']}:\n
{'mês'.ljust(10)} | {'vendas'.ljust(8)} | {'bruto'.ljust(10)} | líquido
{'-' * 60}''')
    margem_a = float(query_info_fruta(fruta_a, 'margem'))
    bruto_soma_a = 0
    liquido_soma_a = 0
    vendas_soma_a = 0
    for mes in dic_meses:
        vendas = int(dic_meses[mes][fruta_a]['vendas'])
        vendas_soma_a += vendas
        # print(f'\nmonitoramento: vendas = {vendas_soma_a}')
        valor = float(dic_frutas[fruta_a]['valor'])
        
        bruto = int(vendas * valor)
        bruto_soma_a += bruto 
        # print(f'\nmonitoramento: bruto = {bruto_soma_a}')
        bruto_str = f'{bruto:,.2f}'
        
        liquido = int(bruto * margem_a)
        liquido_soma_a += liquido
        # print(f'\nmonitoramento: liquido = {liquido_soma_a}')
        print(f'{mes.ljust(10)} | {str(vendas).ljust(8)} | R${bruto_str.ljust(12)} | R${liquido:,.2f}')
    print(f'Vendas totais: {vendas_soma_a:,} | Valor bruto total: {bruto_soma_a:,.2f} | Valor liquido total: {liquido_soma_a:,.2f}')
    
    print(f'''
{dic_frutas[fruta_b]['nome']}:\n
{'mês'.ljust(10)} | {'vendas'.ljust(8)} | {'bruto'.ljust(10)} | líquido
{'-' * 60}''')
    margem_b = float(query_info_fruta(fruta_b, 'margem'))
    bruto_soma_b = 0
    liquido_soma_b = 0
    vendas_soma_b = 0
    for mes in dic_meses:
        vendas = int(dic_meses[mes][fruta_b]['vendas'])
        vendas_soma_b += vendas
        # print(f'\nmonitoramento: vendas = {vendas_soma_a}')
        valor = float(dic_frutas[fruta_b]['valor'])
        
        bruto = int(vendas * valor)
        bruto_soma_b += bruto 
        # print(f'\nmonitoramento: bruto = {bruto_soma_a}')
        bruto_str = f'{bruto:,.2f}'
        
        liquido = int(bruto * margem_b)
        liquido_soma_b += liquido
        # print(f'\nmonitoramento: liquido = {liquido_soma_a}')
        print(f'{mes.ljust(10)} | {str(vendas).ljust(8)} | R${bruto_str.ljust(12)} | R${liquido:,.2f}')
    print(f'Vendas totais: {vendas_soma_b:,} | Valor bruto total: {bruto_soma_b:,.2f} | Valor liquido total: {liquido_soma_b:,.2f}')
    input(f'Aperte "Enter".')
    return comparar_frutas()


if __name__ == '__main__':
    main()
