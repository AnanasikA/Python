# Wersja proceduralna.
# Bank - wersja 5.
# Dowolna liczba kont - implementacja wykorzystująca listę slowników.

accountsList = []


def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name': aName, 'balance': aBalance, 'password': aPassword}
    accountsList.append(newAccountDict)


def show(accountNumber):
    global accountsList
    print('Konto ', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('     Imię: ', thisAccountDict['name'])
    print('     Saldo: ', thisAccountDict['balance'])
    print('     Hasło: ', thisAccountDict['password'])
    print()


def getBalance(accountNumber, password):
    global accountsList

    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Hasło jest nieprawidłowe!')
        return None
    return thisAccountDict['balance']


def deposit(accountNumber, amountToDeposit, password):
    global accountsList

    thisAccountDict = accountsList[accountNumber]

    if accountNumber == accountNumber:
        if amountToDeposit < 0:
            print('Kwota wypłaty musi być dodatnią!')
            return None
        if password != thisAccountDict['password']:
            print('Hasło jest nieprawidłowe! ')
            return None
        thisAccountDict['balance'] = thisAccountDict['balance'] + amountToDeposit
    return thisAccountDict['balance']


def withdraw(accountNumber, amountToDeposit, password):
    global accountsList

    thisAccountDict = accountsList[accountNumber]
    if accountsList[accountNumber] == accountsList[accountNumber]:
        if thisAccountDict['balance'] < 0:
            print('Kwota wypłaty musi być dodatnią!')
            return None
        if password != thisAccountDict['password']:
            print('Hasło tego konta jest nieprawidłowe!')
            return None
        if amountToDeposit > thisAccountDict['balance']:
            print('Kwota wypłaty nie może być większą od wysokości salda!')
            return None

        thisAccountDict['balance'] = thisAccountDict['balance'] - amountToDeposit
        return thisAccountDict['balance']

# Utworzenie dwóch dodatkowych kont.


print("Numer konta bankowego Tymka: ", len(accountsList))
newAccount("Tymek", 400, '8888')

print("Numer konta bankowego Janka: ", len(accountsList))
newAccount("Janek", 600, '6666')

while True:
    print()
    print('Wybierz opcję b, aby wyświetlić saldo')
    print('Wybierz opcję d, aby dokonać wpłaty')
    print('Wybierz opcję n, aby utworzyć nowe konto')
    print('Wybierz opcję w, aby aby dokonać wypłaty')
    print('Wybierz opcję s, aby wyświetlić informacje o koncie')
    print('Wybierz opcję q, aby zakonczyć działanie programu')
    print()

    action = input('Co chciałbyś zrobić teraz?')
    action = action.lower() # Wymuszenie użycia małych liter
    action = action[0] # Użycie pierwszej litery
    print()

    if action == 'b':
        print('Wyświetl saldo: ')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Proszę podać hasło: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Wysokość salda wynosi: ', theBalance)

    elif action == 'd':
        print('Wpłata środków: ')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Proszę podać kwotę wypłaty: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi: ', newBalance)

    elif action == 'n':
        print('Nowe konto: ')
        userName = input('Jak masz na imię? ')
        userStartingAmount = input('Jakie jest początkowe saldo? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('Podaj hasło do tego konta: ')
        userAccountNumber = len(accountsList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Numer nowego konta: ', userAccountNumber)

    elif action == 'w':
        print('Wypłata środków: ')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Proszę podać kwotę wypłaty: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi: ', newBalance)

    elif action == 's':
        print('Informacja o koncie: ')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        show(userAccountNumber)

    elif action == 'q':
        break

print('Gotowe!')
