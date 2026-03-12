import turtle


window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Raffaello e le funzioni")

raffaello = turtle.Turtle() 

def koch(t, order, size):
  """
    La tartaruga t disegna frattale Koch di 'order' and 'size'
    lasciando la tartaruga nella direzioni iniziale
  """

  if order == 0:          
      # caso base che termina la ricorsione
      t.forward(size)
  else:
      # caso ricorsivo (ordine 1) in cui disegna i 4 segmenti
      koch(t, order-1, size/3)  
      t.left(60)
      koch(t, order-1, size/3)
      t.right(120)
      koch(t, order-1, size/3)
      t.left(60)
      koch(t, order-1, size/3)
      ##
      
      
koch(raffaello, 5, 200)

window.mainloop()