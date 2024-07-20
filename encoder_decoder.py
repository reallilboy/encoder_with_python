import pickle

file = open('./engima_rotors','rb')
rotor1,rotor2,rotor3 = pickle.load(file)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def reflector(c):
    return alphabet[len(alphabet) - alphabet.find(c)-1]


def enigma_one_char(c):
    c1 = rotor1[alphabet.find(c)]
    c2 = rotor2[alphabet.find(c1)]
    c3 = rotor3[alphabet.find(c2)]
    reflected = reflector(c3)
    c3 = alphabet[rotor3.find(reflected)]
    c2 = alphabet[rotor2.find(c3)]
    c1 = alphabet[rotor1.find(c2)]
    return c1

def rotate_rotors():
    global rotor1 , rotor2 , rotor3
    rotor1 = rotor1[1:] + rotor1[0]
    if state % 26:
        rotor2 = rotor2[1:] + rotor2[0]
    if state % (26*26):
        rotor3 = rotor3[1:] + rotor3[0]


plain = 'hiihihihi'
cipher = ''
state = 0
for c in plain:
    state += 1
    cipher += enigma_one_char(c)
    rotate_rotors()

print(cipher)
