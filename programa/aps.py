from PySimpleGUI import PySimpleGUI as sg # A INTERFACE USADA 
import random # A BIBLIOTECA USADA PARA GERAR O 'EMBARALHAMENTO' DE CARACTERES PARA CRIPTOGRAFIA

class PassGen:
    def __init__(self):  #AQUI UMA CLASSE E UMA FUNÇÃO QUE DEFINE O INICIO DO CODIGO
        #Layout              
        sg.theme('Dark')
        layout = [ #AQUI DEFINE AS LINHAS DA INTERFACE. LABELS BOTÕES, ETC
            [sg.Text('Usuario'),sg.Input(key='usuario')],   
            [sg.Text('Senha  '),sg.Input(key='senha', password_char='*')],
            [sg.Button('Verificar Acesso')],
            [sg.Text('...', key='Verificar', size=(15,5))],
            [sg.Text('   Digite a Mensagem:')],
            [sg.Text(''),sg.Input(key='cript', size=(50,50))],
            [sg.Text('Mensagem Criptografada: ')],
            [sg.Text('',key='c', size=(50,5))],
            [sg.Text('Mensagem descriptografada: ')],
            [sg.Text('', key='d',size=(50,5))],
            [sg.Button('Criptografar'), sg.Button('Descriptografar')],
        ]#TERMINA AQUI A INTERFACE
        #Janela
        self.janela = sg.Window('Criptografador', layout) #AQUI CRIA UMA JANELA, A INTERFACE EM SI NÃO RODA SEM A CRIAÇÃO DA JANELA
        #Ler os eventos
    def Iniciar(self): #AQUI COMEÇA AS LINHAS DE CODIGOS
        while True:
            eventos, valores = self.janela.read() #AQUI DEFINE PARA QUE SE A JANELA FOR FECHADA LOGO O CODIGO ACABA
            if eventos == sg.WINDOW_CLOSED:
                break

            if eventos == 'Verificar Acesso': #O BOTÃO VERIFICAR ACESSO VAI VERIFICAR SE O LOGIN E SENHA VAI ESTAR IGUAL AO DA VARIAVEL
                if valores ['usuario'] == 'kaue' and valores ['senha'] == '123456':
                    acess = 'Acesso Liberado' # SE ESTIVER, O ACESSO É LIBERADO
                    self.janela['Verificar'].update(acess)
                else: # SE NÃO, O ACESSO É NEGADO
                    neg = 'Acesso Negado!'
                    self.janela['Verificar'].update(neg)
                    
             
            if eventos == 'Criptografar': #O BOTÃO CRIPTOGRAFAR SO VAI FUNCIONAR SE O ACESSO ESTIVER LIBERADO, E SE ALGO FOR DIGITADO
                cript = ('')              # NO CAMPO DE MENSAGEM, CASO CONTRARIO, ELE VAI REPRESENTAR QUE O ACESSO ESTÁ NEGADO TAMBÉM
                if valores ['usuario'] == 'kaue' and valores ['senha'] == '123456':
                    if  valores ['cript']  != cript:
                        new = self.gerar_criptografia()
                        print(new)
                        self.janela['c'].update(new)  
                else:
                    neg = 'Acesso Negado!'
                    self.janela['c'].update(neg)
                    
            elif eventos == 'Descriptografar': # O MESMO VALE PARA O BOTÃO DE DESCRIPTOGRAFIA
                cript = ('')
                if valores ['usuario'] == 'kaue' and valores ['senha'] == '123456':
                    if  valores ['cript']:
                        self.janela['d'].update((valores['cript'])) 
                else:
                    neg = 'Acesso Negado!'
                    self.janela['d'].update(neg)

            

    def gerar_criptografia(self): # AQUI DEFINE A CRIPTOGRAFIA
        cripto = "ABCDEFGHYJKLMNOPQRSTUVWXYZabcdef-=+-*/ghijklmnop$%&qrstuvwxyz1234567890!@*"
        char = random.choices(cripto, k=50)
        join = ''.join(char)
        print(join)
        return join 
gen = PassGen()
gen.Iniciar() 
#FIM
