import turtle

def draw_rectangle(tartaruga, lunghezza, altezza):
  '''Disegno un rettangolo con la tartaruga'''

  for i in range(2):     # disegna 2 lati 2 volte
    tartaruga.forward(lunghezza)
    tartaruga.left(90)
    tartaruga.forward(altezza)
    tartaruga.left(90)

def draw_square(my_turtle, step):
  '''Disegno un quadrato con la tartaruga'''
  
  draw_rectangle(my_turtle, step, step)

def somma(a,b):
  '''sommo due numeri'''
  
  ris = a+b
  
  return ris

window = turtle.Screen()               # istanza "window" di Screen
window.bgcolor("lightgreen")           # imposto lo stato della "window"
# window.title("Raffaello & Donatello")

raffaello = turtle.Turtle()            # Istanza di Turtle chiamata raffaello
raffaello.color("red")                 # attributi per lo stato di raffaello    
raffaello.pensize(5)

#draw_square(raffaello, 50)
risultato_somma = somma(7,6)
print(risultato_somma)

raffaello.right(180)                   # giro e sposto dall'origine raffaello
raffaello.forward(80)                  # 

window.mainloop()                      # Attendo chiusura finestra di gioco o stop del programma