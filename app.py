import numpy as np
#Look in the mesh.py file and give me the Mesh
from mesh import Mesh
from vispy import app, gloo
#This is for makings the numbers look better
np.set_printoptions (suppress=True, precision=2)

VERT_SHADER = """
attribute vec3 vertex;
void main(){
    gl_Position = vec4(vertex, 1.);
}
"""

FRAG_SHADER = """
void main(){
    gl_FragColor = vec4(1., 0., 0., 1.);
}
"""

program = gloo.Program(VERT_SHADER, FRAG_SHADER)



#Import Mesh
monkey = Mesh('monkey.obj', [1, 2, 3], [90, 100, 10], [1, 2, 3])
print(monkey.model_matrix)
print(monkey.position)

attributes = [
    ('vertex', np.float32, 3)
]
data = np.zeros(len(monkey.vertices), attributes)
data['vertex'] = monkey.vertices
print(data)
vertex_buffer = gloo.VertexBuffer(data)

program.bind(vertex_buffer)

index_buffer = gloo.IndexBuffer(monkey.faces)

#Make Window
canvas = app.Canvas(keys='interactive')



@canvas.connect
def on_draw(event):
    gloo.clear([1,1,0])
    program.draw('triangles', index_buffer)
    canvas.update()

#Show Window, Run Program
canvas.show()
app.run()
