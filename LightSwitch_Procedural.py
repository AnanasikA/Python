# Włącznik swiatła utworzony w podejściu proceduralnym

def turnOn():
    global switchIsOn
    switchIsOn = True


def turnOff():
    global switchIsOn
    switchIsOn = False


# kod główny
switchIsOn = False

# kod tekstowy

print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)