import numpy as np
#Look in the mesh.py file and give me the Mesh
from mesh import Mesh
from vispy import app, gloo
#This is for makings the numbers look better
np.set_printoptions (suppress=True, precision=2)


#Import Mesh
monkey = Mesh('monkey.obj', [1, 2, 3], [90, 100, 10], [1, 2, 3])
print(monkey.model_matrix)
print(monkey.position)


#Make Window
canvas = app.Canvas(keys='interactive')



@canvas.connect
def on_draw(event):
    gloo.clear([0,0,0])
    canvas.update()

#Show Window, Run Program
canvas.show()
app.run()
