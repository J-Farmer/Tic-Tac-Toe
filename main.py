import pgzrun

WIDTH = 150
HEIGHT = 150

x = Actor("x")
o = Actor("o")

turn = True #turn == True means it is X's turn! 

positions = [[None, None, None],
            [None, None, None],
            [None, None, None]]

def draw():
  screen.clear()
  screen.fill("white")

  screen.draw.line((50, 0), (50,HEIGHT), "black")
  screen.draw.line((100,0),(100,HEIGHT), "black")

  screen.draw.line((0, 50), (WIDTH, 50), "black")
  screen.draw.line((0, 100), (WIDTH, 100), "black")

def update():
  pass

def changeTurn(x, y):
  global turn
  if positions[y][x] is not None:
      return
  positions[y][x] = turn
  turn = not(turn)
  print(positions)

def on_mouse_down(pos):
  global turn
  #TODO: Simplify to a loop?
  '''
  cellSize = 50
  for y in range(0, 4):
    for x in range(0, 4):
      if(cellSize*x < pos[0] <= cellSize*y and cellSize*x < pos[1] <= cellSize*y):
        print(f"{x},{y}", pos)
  '''
#First Row
  if(0 < pos[0] <= 50 and 0 <= pos[1] <= 50):
    print("0,0", pos)
    changeTurn(0,0)
  elif(50 < pos[0] <= 100 and 0 <= pos[1] <= 50):
    print("0,1", pos)
    changeTurn(0,1)
  elif(100 < pos[0] <= 150 and 0 <= pos[1] <= 50):
    print("0,2", pos)
    changeTurn(0,2)
#Second Row
  elif(0 < pos[0] <= 50 and 50 < pos[1] <= 100):
    print("1,0", pos)
    changeTurn(1,0)
  elif(50 < pos[0] <= 100 and 50 < pos[1] <= 100):
    print("1,1", pos)
    changeTurn(1,1)
  elif(100 < pos[0] <= 150 and 50 < pos[1] <= 100):
    print("1,2", pos)
    changeTurn(1,2)
#Third Row
  elif(0 < pos[0] <= 50 and 100 < pos[1] <= 150):
    print("2,0", pos)
    changeTurn(2,0)
  elif(50 < pos[0] <= 100 and 100 < pos[1] <= 150):
    print("2,1", pos)
    changeTurn(2,1)
  elif(100 < pos[0] <= 150 and 100 < pos[1] <= 150):
    print("2,2", pos)
    changeTurn(2,2)

pgzrun.go()