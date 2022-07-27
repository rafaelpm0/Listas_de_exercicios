from os import path
import sys


class Txt:

    def __init__(self, arquivo: str, item: int, quantidade: float) -> None:
        self.__arquivo = arquivo
        self.__item = item
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
    def g_arquivo(self, arquivo):
        self.__arquivo = arquivo

    @g_item.setter
    def g_item(self, item):
        self.__item = item

    @g_quantidade.setter
    def g_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def __add__(self, other):
        return self.__arquivo + other


class Manipula_Txt(Txt):

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
        try:
            with open(Txt.g_arquivo, 'w', encoding='utf-8') as arquivo:
                pass
        except Exception as error:
            print(error)


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
    menu = input('\n[1] Adicionar novo item, [2] Atualizar item: , [3] Voltar o menu: ')
    if menu == '1':
        desc = input('Digite a descrição do produto: ').upper()
        quant = input('Digite a quantidade: ')
        with open(Txt.g_arquivo, 'a+', encoding='utf-8') as arq:   # erro no loop, tem de ver oque faz quando a lista está zerada, pois fiz percorrer todo o caminho, mas não tem oque ler
            lista = arq.readlines()
            if len(lista) != 0:
                for i in lista:
                    if desc not in i.split(';')[0]:
                        arq.write(f'{desc};{quant}')
                    else:
                        return print('Item existente, fazer utiliza a opcao 2.')
            else:
                arq.write(f'{desc};{quant}')


def main() -> None:
    inicia_txt()

    menu = input('\nDigite [1] Para adicionar/atualizar um item a lista, [2] Remover um item da lista, [3] Gerar '
                 'relaório e [4] Encerrar o programa: ')

    while True:
        if menu == '1':
            add_at_txt()
        if menu == '2':
            pass
        if menu == '3':
            pass
        else:
            print('Comando invalido. Programa finalizado')
            break


main()
