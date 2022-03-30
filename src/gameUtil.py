import random

HANGMAN = ['H', 'A', 'N', 'G', 'M', 'A', 'N']


def toUpper(mesaj):
    return mesaj.upper()


def removeEnd(mesaj):
    if '\n' in mesaj:
        return mesaj[:len(mesaj) - 1]
    return mesaj


def generateRandomWord(fisier):
    file = list(open(fisier, 'r'))
    listaCuvinte = list(map(removeEnd, list(map(toUpper, file))))
    numarRandom = random.randint(0, len(listaCuvinte) - 1)
    return listaCuvinte[numarRandom]


def cuvantToHangman(cuvant):
    cuvant = list(cuvant)
    cuvantEditat = list('_' if elem != ' ' else ' ' for elem in cuvant)
    cuvantEditat[0] = cuvant[0]
    cuvantEditat[len(cuvantEditat) - 1] = cuvant[len(cuvant) - 1]
    return cuvantEditat


def strListFormat(cuvant):
    if '|' in cuvant:
        cuvant = cuvant.split('|')

    for i in range(0, 2):
        cuvant[i] = cuvant[i].replace("'", "")
        cuvant[i] = cuvant[i].replace(",", "")
        cuvant[i] = cuvant[i].replace("[", "")
        cuvant[i] = cuvant[i].replace("]", "")

    return cuvant


def completareCuvant(cuvantTinta, cuvantCurent, litera):
    for i in range(1, len(cuvantTinta) - 1):
        if litera == cuvantTinta[i]:
            cuvantCurent[i] = cuvantTinta[i]
    return cuvantCurent


def completareHangman(hangman: list):
    hangman.append(HANGMAN[0])
    HANGMAN.pop(0)

    return hangman


def hasWon(hangman, cuvantCurent):
    if '_' not in cuvantCurent:
        return 1

    if len(hangman) == 7:
        return 0

    return -1

# strListFormat("['C', '_', '_', '_', '_', '_', '_', '_', 'A']|[]")
