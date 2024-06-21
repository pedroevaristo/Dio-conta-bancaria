import main
from Model.receive_Options import Options_From_View

def main():
    
    option = input('''Seja bem-vindo ao The Bank 
    \n Selecione as opções abaixo ?
    \n  1- ver o extrato 2- depositar 3- sacar''')
    
    match option:
        case"1":
            Options_From_View.View_Extract()
        case"2":
            Options_From_View.putting_Information_Of_Depositing()
        case"3":
            Options_From_View.taking_Withdraw()

