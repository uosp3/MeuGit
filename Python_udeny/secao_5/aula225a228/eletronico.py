from log import LogPrintMixin, LogFileMixin


class Eletronico:
    def __init__(self, nome) -> None:
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False

# Gravar frase: Prefira composição em vez de herança
class Smartphone(Eletronico, LogFileMixin): #usou herança múltipla para colocar algo que não é da família de Eletronico dentro de Smartphome para adicionar uma funcionalidade a mais que é fazer log
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)
