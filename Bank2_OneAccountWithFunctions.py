# Wersja proceduralna
# Bank - wersja 2
# Tylko jedno konto.

accountName = ' '
accountBalance = 0
accountPassword = ' '


def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
    global accountName, accountBalance, accountPassword
    print('     Imię: ', accountName)
    print('     Saldo: ', accountBalance)
    print('     Hasło: ', accountPassword)
    print()


def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Hasło jest nieprawidłowe! ')
        return None
    return accountBalance


def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('Kwota wypłaty musi być dodatnią!')
        return None

    if password != accountPassword:
        print('Hasło jest nieprawidłowe! ')
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance


def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('Kwota wypłaty musi być wartością dodatnią!')
        return None

    if password != accountPassword:
        print('Hasło jest nieprawidłowe! ')
        return None

    if amountToWithdraw > accountBalance:
        print('Kwota wypłaty nie może być większa od wysokości salda. ')

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance


newAccount("Franek", 200, '1234')  # Utworzenie konta

while True:
    print()
    print('Wybierz opcję b, aby wyświetlić saldo')
    print('Wybierz opcję d, aby dokonać wpłaty')
    print('Wybierz opcję w, aby dokonać wypłaty')
    print('Wybierz opcję s, aby wyświetlić informację o koncie')
    print('Wybierz opcję q, aby zakończyć dziłanie programu')
    print()

    action = input('Co chcesz teraz zrobić? ')
    action = action.lower()  # Wymuszenie użycia małych liter
    action = action[0]  # Użycie po prostu pierwszej litery
    print()

    if action == 'b':
        print('Wyświetl saldo: ')
        userPassword = input('Proszę podać hasło: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Wysokość salda wynosi: ', theBalance)

    if action == 'd':
        print('Wpłata środków: ')
        userDepositAmount = input('Proszę podać kwotę wpłaty: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi: ', newBalance)

    if action == 'w':
        print('Wypłata środków: ')
        userWithdrawAmount = input('Proszę podać kwotę wypłaty: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi: ', newBalance)

    if action == 's':
        print('informacja o koncie:  ')
        show()

    elif action == 'q':
        break


print('Gotowe!')
