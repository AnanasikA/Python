# Wersja proceduralna.
# Bank - wersja 3.
# Dwa konta.

account0Name = ' '
account0Balance = 0
account0Password = ' '
account1Name = ' '
account1Balance = 0
account1Password = ' '
nAccounts = 0


def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password


def show():
    global userAccountNumber, account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if userAccountNumber == 0:
        print('Konto 1')
        print('Imię: ', account0Name)
        print('Saldo:', account0Balance)
        print('Hasło: ', account0Password)
        print()
    if userAccountNumber == 1:
        print('Konto 2')
        print('Imię: ', account1Name)
        print('Saldo:', account1Balance)
        print('Hasło: ', account1Password)
        print()


def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Hasło jest nieprawidłowe!')
            return None
        return account0Balance

    if accountNumber == 1:
        if password != account1Password:
            print('Hasło jest nieprawidłowe!')
            return None
        return account1Balance


def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amountToDeposit < 0:
            print('Kwota wypłaty musi beć dodatnią!')
            return None
        if password != account0Password:
            print('Hasło jest nieprawidłowe!')
            return None
        account0Balance = account0Balance + amountToDeposit
        return account0Balance

    if accountNumber == 1:
        if amountToDeposit < 0:
            print('Kwota wypłaty musi beć dodatnią!')
            return None
        if password != account1Password:
            print('Hasło jest nieprawidłowe!')
            return None
        account1Balance = account1Balance + amountToDeposit
        return account1Balance


def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amountToWithdraw < 0:
            print('Kwota wypłaty musi być dodatnią!')
            return None
        if password != account0Password:
            print('Hasło tego konta jest nieprawidłowe!')
            return None
        if amountToWithdraw > account0Balance:
            print('Kwota wypłaty nie może być większą od wysokości salda!')
            return None

        account0Balance = account0Balance - amountToWithdraw
        return account0Balance

    if accountNumber == 1:
        if amountToWithdraw < 0:
            print('Kwota wypłaty musi być dodatnią!')
            return None
        if password != account1Password:
            print('Hasło tego konta jest nieprawidłowe!')
            return None
        if amountToWithdraw > account1Balance:
            print('Kwota wypłaty nie może być większą od wysokości salda!')
            return None

        account1Balance = account1Balance - amountToWithdraw
        return account1Balance

# Utworzenie konta


newAccount(0, "Roman", 300, '3456')
newAccount(1, "Albert", 500, '1234')

# Kod główny odpowiedzialny za wywołanie funkcji

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
        userPassword = input('Proszę podać hasło: ')
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
        userWithdrawAmount = input('Proszę podać kwotę wypłaty: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Proszę podać hasło: ')

        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Wysokość salda po operacji wynosi: ', newBalance)

    if action == 's':
        userAccountNumber = input('Proszę podać numer konta: ')
        userAccountNumber = int(userAccountNumber)
        show()

    elif action == 'q':
        break

print('Gotowe!')
