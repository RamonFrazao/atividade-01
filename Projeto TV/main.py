import Control
import Tv


class Main (Control.Control, Tv.Tv):
    def __init__ (self, brand, size):
        super ().__init__ (brand, size)

    def on (self):
        if not self.get_connect():
            self.set_connect(True)
            print ('Tv ligada!')
        else:
            print ('A tv ja esta ligada!')

    def off (self):
        if self.get_connect():
            self.set_connect(False)
            print ("Tv desligada!")
        else:
            print ('A tv ja esta deligada!')

    def setChannel (self, channel):
        try:
            if self.get_connect():
                if channel > 0:
                    self.set_channel(channel)
                    print ('Canal alterado!')
                else:
                    print ('Nao foi possivel alterar o canal!')
            else:
                print ('Tv desligada!')
        except TypeError:
            print("Informe um caracter valido!")

    def upChannel (self):
        if self.get_connect():
            channel = self.get_channel()
            channel += 1
            self.set_channel(channel)
            print ('Canal alterado!')
        else:
            print ('Tv desligada!')

    def downChannel (self):
        if self.get_connect():
            if self.get_channel() > 1:
                channel = self.get_channel()
                channel -= 1
                self.set_channel(channel)
                print ('canal alterado!')
            else:
                print ('Nao foi possivel alterar o canal!')
        else:
            print ('Tv desligada! ')

    def upVolume (self):
        if self.get_connect():
            if self.get_sound() < 100:
                sound = self.get_sound()
                sound += 1
                self.set_sound(sound)
                print ('Volume aumentado!')
            else:
                print ('O volume está no maximo!')
        else:
            print ('A tv esta desligada!')

    def downVolume (self):
        if self.get_connect():
            if self.get_sound() > 0:
                sound = self.get_sound()
                sound -= 1
                self.set_sound(sound)
                print ('Volme diminuido!')
            else:
                print ('O volume esta no minimo!')
        else:
            print ('A tv esta desligada!')

    def mute (self):
        if self.get_connect():
            if self.get_sound() > 0:
                self.set_sound(0)
                print ('Som mutado!')
            else:
                print ('A Som ja está mutado!')
        else:
            print ('A tv esta desligada!')

    def getInfo (self):
        print (f'Marca: {self.get_brand ()}')
        print (f'Tamanho: {self.get_size ()}')
        print (f'Volume: {self.get_sound()}')
        print (f'Canal: {self.get_channel()}')
        print (f'Estado: Ligada' if self.get_connect() else 'Estado: Desligada')

