from engine.config import Config
from engine.enigma import Enigma
from engine.rotor import Rotor
from logger.logger import Logger

if __name__ == '__main__':
    rotor1 = Rotor(1, 0, 'PEZUOHXSCVFMTBGLRINQJWAYDK')
    rotor2 = Rotor(2, 0, 'ZOUESYDKFWPCIQXHMVBLGNJRAT')
    rotor3 = Rotor(3, 0, 'EHRVXGAOBQUSIMZFLYNWKTPDJC')
    rotor4 = Rotor(4, 0, 'IMETCGFRAYSQBZXWLHKDVUPOJN')
    rotor5 = Rotor(5, 0, 'QWERTZUIOASDFGHJKPYXCVBNML', reflector=True)
    enigma = Enigma(Config.plugs)
    enigma.add_rotor(rotor1)
    enigma.add_rotor(rotor2)
    enigma.add_rotor(rotor3)
    enigma.add_rotor(rotor4)
    enigma.add_rotor(rotor5)
    Logger.log("welcome")
    while True:
        enigma.show_current_state()
        Logger.log("waiting for user to type...")
        letter = input()
        encrypted = enigma.encrypt(letter.capitalize())
        Logger.log("result: {0}\n".format(encrypted))
