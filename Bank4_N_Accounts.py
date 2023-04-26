# Wersja proceduralna.
# Bank - wersja 4.
# Dowolna liczba kont - implementacja wykorzystująca listy.

accountNameList = []
accountBalanceList = []
accountPasswordList = []


def newAccount(name, balance, password):
    global accountNameList, accountBalanceList, accountPasswordList

    accountNameList.append(name)
    accountBalanceList.append(balance)
    accountPasswordList.append(password)


def show(accountNumber):
    global accountNameList, accountBalanceList, accountPasswordList

    print('Konto', accountNumber)
    print('  imię: ', accountNameList[accountNumber])
    print('  Saldo: ', accountBalanceList[accountNumber])
    print('  Hasło: ', accountPasswordList[accountNumber])
    print()


def getBalance(accountNumber, password):
    global accountNameList, accountBalanceList, accountPasswordList

    if password != accountPasswordList[accountNumber]:
        print('Hasło jest nieprawidłowe! ')
        return None
    return accountBalanceList[accountNumber]


def deposit(accountNumber, amountToDeposit, password):
    global accountNameList, accountBalanceList, accountPasswordList

    if accountNumber == accountNumber:
        if amountToDeposit < 0:
            print('Kwota wypłaty musi beć dodatnią!')
            return None
        if password != accountPasswordList[accountNumber]:
            print('Hasło jest nieprawidłowe! ')
            return None
        accountBalanceList[accountNumber] = accountBalanceList[accountNumber] + amountToDeposit
        return accountBalanceList[accountNumber]


def withdraw(accountNumber, amountToWithdraw, password):
    global accountNameList, accountBalanceList, accountPasswordList

    if amountToWithdraw < 0:
        print('Kwota wypłaty musi być dodatnią!')
        return None
    if password != accountPasswordList[accountNumber]:
        print('Hasło tego konta jest nieprawidłowe!')
        return None
    if amountToWithdraw > accountBalanceList[accountNumber]:
        print('Kwota wypłaty nie może być większą od wysokości salda!')
        return None

        accountBalanceList[accountNumber] = accountBalanceList[accountNumber] - amountToWithdraw
        return accountBalanceList[accountNumber]


# Utworzenie dwóch przykładowych kont.

print("Numer konta bankowego Janka: ", len(accountNameList))
newAccount("Janek", 100, 'soup')

print("Numer konta bankowego Marysi: ", len(accountNameList))
newAccount("Marysia", 1234, '1234')

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
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input("Proszę podać hasło: ")
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Wysokość salda wynosi: ', theBalance)

    if action == 'd':
        print('Wpłata środków: ')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Proszę podać kwotę wpłaty: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi: ', newBalance)

    if action == 'w':
        print('Wypłata środków: ')
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Proszę podać kwotę wypłaty: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi: ', newBalance)

    if action == 's':
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        show(userAccountNumber)

    elif action == 'q':
        break

print('Gotowe!')






















