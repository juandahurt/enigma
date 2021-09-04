from engine.config import Config
from engine.enigma import Enigma
from engine.rotor import Rotor
from logger.logger import Logger

if __name__ == '__main__':
    rotor1 = Rotor(1, 0, Config.wiring1)
    rotor2 = Rotor(2, 0, Config.wiring1)
    rotor3 = Rotor(3, 0, Config.wiring1)
    rotor4 = Rotor(4, 0, Config.wiring1)
    rotor5 = Rotor(5, 0, Config.wiring1, mirror=True)
    enigma = Enigma()
    enigma.add_rotor(rotor1)
    enigma.add_rotor(rotor2)
    enigma.add_rotor(rotor3)
    enigma.add_rotor(rotor4)
    enigma.add_rotor(rotor5)
    Logger.log("welcome")
    while True:
        Logger.log("waiting for user to type...")
        letter = input()
        ecrypted = enigma.type(letter)
