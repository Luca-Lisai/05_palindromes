"""Ce module contient des fonctions pour vérifier et manipuler des palindromes."""
#### Fonction secondaire
import unicodedata
import string

def clean(chaine) :
    "Rearrange la chaine pour pouvoir faire le test"
    p2 = chaine
    p2 = p2.lower()
    p2 = p2.replace(" ", "")

    p2 = unicodedata.normalize('NFD', p2)
    p2 = ''.join(c for c in p2 if not unicodedata.combining(c))

    p2 = ''.join(caractere for caractere in p2 if caractere not in string.punctuation)
    return p2

def ispalindrome(p):
    "Teste si la chaine est un palindrome"
    # votre code ici
    p2 = clean(p)
    return p2 == p2[::-1]


#### Fonction principale


def main():
    "Fonction principale de test"
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie", "La mariée ira mal"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
