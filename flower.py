t=turtle.Turtle()
for i in range(8):
  t.forward(50)
  t.fillcolor('#e38fae')
  t.begin_fill()
  t.circle(30)
  t.end_fill()
  t.fillcolor('#de721f')
  t.begin_fill()
  t.circle(20)
  t.end_fill()
  
  t.backward(50)
  t.left(45)
  
t.right(90)
t.forward(150)
t.endfill()
