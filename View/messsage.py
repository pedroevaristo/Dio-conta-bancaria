from Controller import deposit, extract, withdraw

def main():
    
    option = input('''Seja bem-vindo ao The Bank 
    \n Selecione as opções abaixo ?
    \n  1- ver o extrato 2- depositar 3- sacar''')
    
    match option:
        case"1":
            deposit.depositing_In_Account()
        case"2":
            extract._Information_Of_Account()
        case"3":
            withdraw.taking_Withdraw()
            

