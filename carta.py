class Carta:
    def __init__(self, valor, pinta):
        self.pinta = pinta
        self.valor = valor

    def obtener_valor(self):
        if self.valor == 'A':
            return 1
        if self.valor in ['J', 'Q', 'K']:
            return 10
        return int(self.valor)

    def mostrar_carta(self):
        return self.pinta, self.valor

class CartaFrancesa(Carta):
    def __init__(self, valor, pinta):
        super().__init__(valor, pinta)  # Llamar al constructor de la clase base

class CartaEspanola(Carta):
    def __init__(self, valor, pinta):
        super().__init__(valor, pinta)  # Llamar al constructor de la clase base


