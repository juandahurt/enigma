# from config import Config
from engine.config import Config
from engine.rotor import Rotor
from logger.logger import Logger


class Enigma:
    """ Representa a la maquina Enigma utilizada por la armada Alemana para la encriptación de mensajes.

    Attributes:
        rotors (list): Es el corazón de la maquina Enigma. Es una lista de tipo `Rotor`.
    """
    def __init__(self):
        self.rotors = []

    def add_rotor(self, rotor: Rotor):
        if len(self.rotors) > 0:
            rotor.last = self.rotors[-1]
            self.rotors[-1].next = rotor
        self.rotors.append(rotor)

    def type(self, letter) -> str:
        if Config.verbose:
            Logger.log("engine: user typed: {0}".format(letter))
        new_letter = self.rotors[0].send_through(letter)
        self.rotors[0].rotate()
        return new_letter

    def show_current_state(self):
        string = ""
        for index in range(0, len(self.rotors)):
            rotor = self.rotors[index]
            string += "R{0}: {1} ".format(rotor.id, Config.standard_alphabet[rotor.pos])
        Logger.log(string)
