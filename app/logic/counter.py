"""
Lógica do contador - Modelo (Model)
"""


class Counter:
    """Classe que gerencia a lógica do contador"""

    def __init__(self, initial_value=0):
        """
        Inicializa o contador
        
        Args:
            initial_value: Valor inicial do contador (padrão: 0)
        """
        self._value = initial_value
        self._history = [initial_value]

    def increment(self):
        """Incrementa o contador em 1"""
        self._value += 1
        self._history.append(self._value)
        return self._value

    def decrement(self):
        """Decrementa o contador em 1"""
        self._value -= 1
        self._history.append(self._value)
        return self._value

    def reset(self):
        """Reseta o contador para 0"""
        self._value = 0
        self._history = [0]
        return self._value

    def get_value(self):
        """Retorna o valor atual do contador"""
        return self._value

    def get_history(self):
        """Retorna o histórico de valores"""
        return self._history.copy()
