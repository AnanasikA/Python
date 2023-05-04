class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Lista kanałów
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM // 2

    def power(self):
        self.isOn = not self.isOn

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)

    def showInfo(self):
        print()
        print('Stan telewizora: ')
        if self.isOn:
            print('     Telewizor jest: włączony')
            print('     Aktualny kanał: ', self.channelList[self.channelIndex])

            if self.isMuted:
                print('     Głosność: ', self.volume, '(dżwięk jest wyciszomy.)')
            else:
                print('     Głosność: ', self.volume)
        else:
            print('     Telewizor jest wyłączony!')

# Kod główny


oTV = TV()

# Testowanie programu

# Włączenie telewizora i info o stanie
oTV.power()
oTV.showInfo()

# 2x zmiana kanalu na następny. 2x zwększenie głosności i info o stanie

oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# wyłączenie, a póżniej włączenie telewizora oraz info o stanie

oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Zmniejszenie głosniści, wyłączenie dżwięku oraz wyświetlenie info o stanie

oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# Zmiana kanału  na 11, wyłączenie i info o stanie

oTV.setChannel(11)
oTV.mute()
oTV.showInfo()




















