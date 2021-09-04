# from config import Config
from engine.config import Config
from logger.logger import Logger


class Rotor:
    """ Representa a un rotor de la maquina Enigma.

    Attributes:
        id (int): Identificador del rotor.
        pos (str): Posición en la que se encuentra.
        next (Rotor): El rotor al que referencia.
        last (Rotor): El rotor que lo referencia.
        alphabet (list): Alfabeto propio del rotor.
        reflector (bool): Indica si el rotor es un rotor espejo.
    """

    def __init__(self, id, pos, alphabet, reflector = False):
        self.id = id
        self.pos = pos
        self.alphabet = alphabet
        self.next = None
        self.last = None
        if reflector:
            self.next = self
            self.last = self
        self.reflector = reflector

    def rotate(self):
        if Config.verbose:
            Logger.log("rotor {0}: rotating...".format(self.id))
        self.pos += 1
        if self.pos == len(Config.standard_alphabet):
            self.pos = 0
            if self.next != None and not self.reflector:
                self.next.rotate()
        if Config.verbose:
            Logger.log("rotor {0}: new position: {1}".format(self.id, self.pos))

    def send_through(self, letter, reversed = False) -> str:
        if Config.verbose:
            Logger.log("rotor: sendind through rotor {0}".format(self.id))
            Logger.log("rotor: input letter: {0}".format(letter))
        index = self.alphabet.index(letter)
        new_letter = Config.standard_alphabet[index]
        if reversed:
            if self.last == None:
                return new_letter
            return self.last.send_through(new_letter, reversed)
        else:
            return self.next.send_through(new_letter, self.reflector)
