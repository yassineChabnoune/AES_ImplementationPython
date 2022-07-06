# AES implementation en python

ce code contient tous les phases de l'algorithme de cryptage de l'AES : 
## KEY GENERATION
- ROT WORD OF LAST COLUMN
- SUB BYTE OF ROT WORD
- XOR WITH RCON AND FIRST COLUMN OF KEY AND SUBBYTE

## ROUNDS (10 ROUNDS)
###### INIAL ROUND
- XOR WITH ROUND KEY 0 
###### MAIN ROUND  
- SUB BYTES
- SHIFT ROWS
- MIX COLUMNS
- ADD ROUND KEY
###### FINAL ROUND
- SUB BYTE
- SHIFT ROWS
- ADD LAST ROUND KEY

## NUMPY
NumPy est une bibliothèque pour langage de programmation Python, destinée à manipuler des matrices ou tableaux multidimensionnels ainsi que des fonctions mathématiques opérant sur ces tableaux. 
###### POUR INSTALLER NUMPY
vous pouvez utiliser 
```
pip install numpy
```
