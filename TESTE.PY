from kivy.app import App    
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from Cpf import Cpf
from validate_docbr import CPF


Window.clearcolor = (255,255,255,1)
Window.size = (400,690)


class tela(BoxLayout):
    def check(self):
        cpf_digitado = str(self.ids.cpf.text)
        cpf = CPF()
        self.ids.ck.text = str(cpf.validate(cpf_digitado))   

class principal(App):
    def build(self):
        return tela()

principal().run()