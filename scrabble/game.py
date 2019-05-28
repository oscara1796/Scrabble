import random
import string
import sys
import itertools
# Aqui importamos random string y sys para exit

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
n = HAND_SIZE
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

TOTAL_SCORE = 0
TOTAL_COMP_SCORE = 0
#helper code
WORDLIST_FILENAME = "words.txt"





def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------
# Problem #2: Make sure you understand how this function works and what it does!
#


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#



# funcion verify_word
def verify_word(word):
    # llamamos la variable global WORDLIST
    global WORDLIST
    # si la palabra se encuentra en WORLD LIST
    if word  in WORDLIST:
        # aPLICAMOS LA FUNCIÓN UPDATE HAND (WORD)
        updatehand(word)
    # Si no aplicamos un else que diga que la palabra es incorrecta
    else:
        print("That word is incorrect")
        print("X"*50)
        return False

def updatehand(word):
    # Lamamos a la variable global hand
    global hand
    # Nombramos una variable sequence
    sequence = word
    # convertimos la variable sequence a un diccionario
    dict_word = getFrequencyDict(sequence)
    # Usamos el metodo items para convertir el diccionario en tupla y lo guardamos en una variable
    dict_word_item = dict_word.items()
    # usamos la variable hand y le aplicamos una comprension de dccionario
    # La comprensión es asi {k:v for k,v in hand.items() -  dict_word.items()}
    # Lo que quiere decir es que para la llave de la derecha y el valor de la izquierda en los items del ddcionario hand
    # Le borramos los items  del diccionario de nuestra word
    hand = {k:v for k,v in hand.items() -  dict_word.items()}
    # Aplicamos un ciclo for a los items de hand llamando a su k y v
    for k,v in hand.items():
        # Aplicamos un ciclo for dentro de for llamando a los tems x y z de nuestra varieble items de nuestro dict
        for x,z in dict_word_item:
            # Si los los keys de hand y dict son iguales
            if k == x:
                # y si sus valores son diferentes
                if v != z:
                    # Eliminas k o key de hand con del
                    del hand[k]
                    # Ylo vuelves agregar con un valor de 1
                    hand[k] = 1
    # Retorna el valor de la mano
    return hand



def list_for_score(word):
    # Llamamos a lavariable hand
    global hand
    # Llamamos a la variable sacrabble letters
    global SCRABBLE_LETTER_VALUES
    # Nombramos una variable sequence
    sequence = word
    # convertimos la variable sequence a un diccionario
    dict_word = getFrequencyDict(sequence)
    # Nombreamos una variable con una lista vacia llamada score
    score = []
    # Nombramos una variable con el largo de nuestro dict_word
    largodeword = len(word)
    # Otra variable con el largo de hand largodelamano
    largodelamano = len(hand)
    # ciclo for para x en dict_word
    for x in dict_word:
        # ciclo for para x en SCRABBLE_LETTER_VALUES
        if x in SCRABBLE_LETTER_VALUES:
            # Nombramos otra variable con los valores de SCRABBLE_LETTER_VALUES con el metodo get.(x)
            scrabble_word_value = SCRABBLE_LETTER_VALUES.get(x)
            # Y añadimos ese valor con append a score
            score.append(scrabble_word_value)
    # Creamos una variable llamada lasuma  que contiene enteros y esta en 0
    lasuma = 0
    # ciclo for para cada cos i en score
    for i in score:
        # a la variable suma le sumamos ella misma y cada elemento i de score
        lasuma = lasuma + i
    # nombremoa suna variable pre_score a la cual la multiplicamos la suma por el largodelamano
    pre_score = lasuma* largodeword
    # Si el lagro de la mano es 0  nombramos una variable total score y al pre score le sumamos 50
    if largodelamano == 0:
        total_plus_score = pre_score + 50
        # retornamos el valor del total score
        return total_plus_score
    else:
        # else retorna el valor del pre score
        return pre_score






def _print_welcome():
    # funcion print con el menu y bienvenida
        print("Welcome to the scrabble game")
        print("*"*50)
        print("What would you like to do?")
        print("[N] play  a new random hand")
        print("[R] play de last hand again")
        print("[E]xit the game ")


 # La nueva bienvenida con unos menus sencillos
def new_welcome():
        print("*"*50)
        print("What would you like to do?")
        print("[N] play  a new random hand")
        print("[R] play de last hand again")
        print("[E]xit the game ")


def play_random_hand():
    #Imprimimos las letrascon las que vamos a trabajar
    print("letters to work with:")
    # Llamamos a la función displayhand
    displayHand(hand)

# Función para insertar la palabra  o word usamos un input
def inserting_guessing_word():
    return input("insert your word:" + " ")

# Función para volver a jugar  o newgame
def newgame(score, word):
    # Llamamos a las variables globlaes n, total score y hand
    global n
    global TOTAL_SCORE
    global hand
    # Llamamos a welcome
    new_welcome()
    # Hacemos una variable command al cual sele ingrese un input
    COMMAND = input()
    # No importa como sea el input tiene que venir e minusculas
    COMMAND = COMMAND.lower()
    # Condicional comando n
    if COMMAND == "n":
        # Primero realizamos una variable hand que conetnga el diccionario de hand
        hand = dealHand(n)
        # Enseñamos lasletras con las que vaa jugar
        play_random_hand()
        # Insertamos la palabra con las letras que nos dia playrandom hand
        word = inserting_guessing_word()
        # tranformamos esa palabra a un diccionario
        sequence = word
        dict_word = getFrequencyDict(sequence)
        # Nombramos una variable de predicamento  y albergamos la funcion verify word
        predicament = verify_word(word)
        # nombramos una variable que contenga score
        score = list_for_score(word)
        # Si el predicamento resulta falso se empieza otro newgame
        if predicament == False:
                newgame(score,word)
        else:
            # Si no que imprima los puntos totales de score y se los sumos a total score ye mepizas un nuevo juego
            print("Tus puntos son")
            print(score)
            TOTAL_SCORE += score
            newgame(score,word)
# El comando para salir del juego con el modulo importado sys usamos el metodo sys.exit() eimprimimos los puntos tottales
    if COMMAND == "e":
        print("Your total points are:")
        print(TOTAL_SCORE)
        sys.exit()
# Comando r para volver a jugar la mano
    if COMMAND == "r":
        # Enseñamos lo que esta actualmente en lamano
        displayHand(hand)
        # Insertamos una palabra formulado por el usuario con la función creada
        word = inserting_guessing_word()
        # Hacemos el diccionario con esa palabra
        sequence = word
        dict_word = getFrequencyDict(sequence)
        # Hacemos el predicamento
        predicament = verify_word(word)
        # Vemos cuantos puntos da con la variable score
        score = list_for_score(word)
        # Y hacemos la condicional if si el predicamento es falso o si no 
        if predicament == False:
                newgame(score,word)
        else:
            print("Tus puntos son")
            print(score)
            TOTAL_SCORE += score
            newgame(score,word)



if __name__ == '__main__':
    WORDLIST = loadWords()
    _print_welcome()


    COMMAND = input()
    COMMAND = COMMAND.lower()

    if COMMAND == "n":
        hand = dealHand(n)
        play_random_hand()
        word = inserting_guessing_word()
        sequence = word
        dict_word = getFrequencyDict(sequence)
        predicament = verify_word(word)
        score = list_for_score(word)
        if predicament == False:
                newgame(score,word)
        else:
            print("Tus puntos son")
            print(score)
            TOTAL_SCORE += score
            newgame(score,word)



    if COMMAND == "e":
        print("Your total points are:")
        print(TOTAL_SCORE)
        sys.exit()

    if COMMAND == "r":
        print("you dont have remains hands, run again the script")
