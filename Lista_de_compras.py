from os import path
import sys


class Txt:

    def __init__(self, arquivo: str, item: str, quantidade: float) -> None:
        """Recebe todas as informacoes para criacao do arquivo txt"""
        self.__arquivo = arquivo
        self.__item = item                 # item sempre armazer formatando com title
        self.__quantidade = quantidade

    @property
    def g_arquivo(self):
        return self.__arquivo

    @property
    def g_item(self):
        return self.__item

    @property
    def g_quantidade(self):
        return self.__quantidade

    @g_arquivo.setter
    def g_arquivo(self, arquivo: str):
        self.__arquivo = arquivo

    @g_item.setter
    def g_item(self, item: str):
        self.__item = item

    @g_quantidade.setter
    def g_quantidade(self, quantidade: float):
        self.__quantidade = quantidade


class Manipula_Txt(Txt):
    """Realiza toda as manipulacoes e verificacoes necessarias no arquivo txt. Todo metodo usa o valor atual da
    classe para funcinamento, por isso antes da execucao de cada metodo redefinam o Txt.g_item e Txt.g_quantidade."""

    @staticmethod
    def verifica_exit_arq_entrada() -> None:
        """Verifica se o arquivo txt existe. Tratar .txt no final. Criar o arquivo. Possibilita digitar o path."""
        if ".txt" not in Txt.g_arquivo:
            Txt.g_arquivo = str(Txt.g_arquivo) + ".txt"
        elif path.exists(Txt.g_arquivo):
            return True
        else:
            return False

    @staticmethod
    def cria_arquivo():
        """Realiza a criacao do arquivo txt"""
        try:
            with open(Txt.g_arquivo, 'w', encoding='utf-8'):
                pass
        except Exception as error:
            print(error)

    @staticmethod
    def verifica_item():
        """Verifica se o item sendo passado na classe TXT existe no arquivo txt"""
        with open(Txt.g_arquivo, 'r+', encoding='utf-8') as arq:
            lista = arq.readlines()
            for i in lista:
                if Txt.g_item in i:
                    return True
            return False

    @staticmethod
    def add_item():
        """"Adiconar o item atualmente informado na classe TXT no arquivo txt"""
        with open(Txt.g_arquivo, 'a', encoding='utf-8') as arq:
            arq.write(f'{Txt.g_item};{Txt.g_quantidade}\n')

    @staticmethod
    def atualiza_item():
        """Verfica a existencia do item na lista e atualiza a quantidade do item"""
        arquivo = open(Txt.g_arquivo, 'r', encoding='utf-8').readlines()
        with open(Txt.g_arquivo, 'w', encoding='utf-8') as arq:    # Da para juntar com a funcao remover, só criar # um parametro para remover ou atualizar
            for i in arquivo:
                if Txt.g_item in i:
                    arq.write(f'{Txt.g_item};{Txt.g_quantidade}\n')
                else:
                    arq.write(i)

    @staticmethod
    def remover_item():
        """Remove o item informado atualmente da lista"""
        arquivo = open(Txt.g_arquivo, 'r', encoding='utf-8').readlines()
        with open(Txt.g_arquivo, 'w', encoding='utf-8') as arq:
            for i in arquivo:
                if Txt.g_item in i:
                    pass
                else:
                    arq.write(i)
        return print(f'Item "{Txt.g_item}" removido.')

    @staticmethod
    def gerar_relatorio():

        conteudo = open(Txt.g_arquivo, 'r', encoding='utf-8').readlines()
        print('========================================================='
              '\n|Nº           DESCRICAO            QUANTIDADE           |')
        for i in conteudo:
            parte = i.split(";")
            print(f'|{conteudo.index(i)+1}             {parte[0]}{" "*(21-len(parte[0]))}{parte[1].rstrip()}'
                  f'                  |')

        print('=========================================================')


def inicia_txt() -> None:
    """Realiza a procura do arquivo txt ou realiza sua criação."""
    # Aqui será interessnte realizar alguma decoração... vou pensar em algo mais tarde
    Txt.g_arquivo = input('Digite o caminho da lista de compras, onde o arquivo está salvo ou onde quer que seja '
                          'salvo: ')
    while True:
        if Manipula_Txt.verifica_exit_arq_entrada() is True:
            break
        else:
            print('\nArquivo não encontrado.')
            print(f'obs: Caso informe somente o nome do arquivo "arquivo.txt" ele deverá estar em {sys.path[0]}')
            menu = input('\nMenu: [1] Criar um novo arquivo txt, [2] Digite novamnete o caminho do arquivo txt: ')
            if menu == '1':
                Manipula_Txt.verifica_exit_arq_entrada()
                Manipula_Txt.cria_arquivo()
            else:
                Txt.g_arquivo = input('Digite o caminho do arquivo txt: ')


def add_at_txt():
    menu = input('\n[1] Adicionar novo item, [2] Atualizar item: ')

    Txt.g_item = input('Digite a descrição do produto: ').title()
    Txt.g_quantidade = input('Digite a quantidade: ')

    if menu == '1':
        if Manipula_Txt.verifica_item() is False:
            Manipula_Txt.add_item()
            return None
        else:
            return print('Item existente, favor utilizar a opcao 2.')
    elif menu == '2':
        if Manipula_Txt.verifica_item() is True:
            Manipula_Txt.atualiza_item()
            return None
        else:
            return print('Item inexistente, favor utilizar a opcao 1.')
    else:
        print('Menu inexistente. Selecione novamente')


def remover_item():
    Txt.g_item = input('Digite a descrição do produto: ').title()
    Manipula_Txt.remover_item()
    return None


def main() -> None:
    inicia_txt()

    while True:

        menu = input('\nDigite [1] Para adicionar/atualizar um item a lista, [2] Remover um item da lista, [3] Gerar '
                     'relaório e [4] Encerrar o programa: ')

        if menu == '1':
            add_at_txt()
        elif menu == '2':
            remover_item()
        elif menu == '3':
            Manipula_Txt.gerar_relatorio()
        else:
            print('Obrigado! Programa finalizado')
            break

main()