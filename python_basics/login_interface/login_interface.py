import PySimpleGUI as sg
import pandas as pd

# Caminho para o arquivo CSV que contém os dados de login
csv_file = 'sample_users.csv'  # Nome do arquivo CSV com dados de usuários e senhas

# Carregar os dados do arquivo CSV em um DataFrame do pandas
df = pd.read_csv(csv_file)

# Definir o tema e o layout da interface gráfica
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text("Senha"), sg.Input(key='senha', password_char="*")],
    [sg.Checkbox("Salvar o login?")],
    [sg.Button("Entrar")]
]

# Criar uma janela com o título 'Tela de Login' e o layout definido
janela = sg.Window('Tela de Login', layout)

# Loop principal da interface gráfica para monitorar eventos
while True:
    eventos, valores = janela.read()  # Ler eventos e valores da interface
    if eventos == sg.WIN_CLOSED:  # Se a janela for fechada, sair do loop
        break
    if eventos == "Entrar":  # Se o botão 'Entrar' for clicado
        usuario = valores["usuario"]  # Obter o valor do campo 'Usuário'
        senha = valores['senha']      # Obter o valor do campo 'Senha'
        
        # Verificar se o usuário e a senha fornecidos correspondem a algum registro no DataFrame
        if (df['Nome'] == usuario).any() and (df['Senha'] == senha).any():
            sg.popup(f"Bem-vindo, {usuario}!")  # Mostrar uma mensagem de boas-vindas
            janela.close()  # Fechar a janela após login bem-sucedido
            break  # Sair do loop para encerrar o programa
        else:
            sg.popup("Usuário ou senha incorretos. Tente novamente.")  # Mostrar mensagem de erro

# Fechar a janela quando o loop terminar
janela.close()
