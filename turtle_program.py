#
# File: main.py
#
# Author: E.Romelli
#
# Date: 2026/03/04
#
# Version: 1.0
#
# Description: My First Project Program to print "Hello, World!".
#

import turtle               # Importo modulo turtle

window = turtle.Screen()    # Creo una finestra dove lavorare

raffaello = turtle.Turtle() # Creo una tartaruga e la assegno alla variabile "raffaello"
raffaello.color('red')

for i in 'ciao':
    print(i)
    raffaello.forward(50)                  # movimenti per disegnare quadrato
    raffaello.left(90)                     # con raffaello

print('casa' == 'Casa')


#donatello = turtle.Turtle()
#donatello.color('violet')
#donatello.forward(100)
#donatello.right(90)
#donatello.forward(50)

window.mainloop()           # Attende che l'utente chiuda la finestra di gioco o fermi il programma