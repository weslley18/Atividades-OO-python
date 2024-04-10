class Televisao:
    def __init__(self):
        self.ligada = False
        self.volume = 0
        self.salvar_volume= 0
        self.canal = 1
        self.mudo = False
    def liga_desliga(self):

        if self.ligada == False:
            self.ligada = True
            print('televisão ligada')
        elif self.ligada == True:
            self.ligada = False
            print('televisão desligada')
    def aumentar_volume(self):
        if self.ligada == True:
            self.volume += 1
            print('volume atual: ',self.volume)
    def baixar_volume(self):
        if self.ligada == True:
            self.volume -= 1
            print('volume atual: ', self.volume)
    def canal_subir(self):
        if self.ligada == True:
            self.canal += 1
            print('canal atual: ', self.canal)
    def canal_descer(self):
        if self.ligada == True:
            self.canal -= 1
            print('canal atual: ', self.canal)
    def liga_desliga_mudo(self):
        if self.ligada == True:
            if self.volume > 0:
                self.salvar_volume = self.volume
                self.volume = 0
                self.mudo = True
                print('televisão no mudo')
            else:
                self.volume = self.salvar_volume
                print('mudo desativado')


tv = Televisao()

tv.liga_desliga()
tv.aumentar_volume()
tv.aumentar_volume()
tv.liga_desliga()
tv.liga_desliga_mudo()
tv.liga_desliga_mudo()
tv.canal_subir()
tv.liga_desliga()
tv.canal_subir()
tv.canal_subir()
tv.canal_descer()