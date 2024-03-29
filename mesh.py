import numpy as np
from vispy import io
from vispy.util import transforms as tr




#We define a function. In a function you do not know what is happening inside. Just give input and get output

def make_model_matrix(translate, rotation, scale):
    """
    Returns a 4x4 model matrix from translation, rotation, and scalation

    Arguments:
        -translation: x,y,z coordinates
        -rotation: x,y,z rotations (degrees)
        -scale: x,y,z scale.

    Returns:
        -model_matrix: 4x4 numpy array
    """
    sm = tr.scale(scale)
    rx, ry, rz = rotation
    rzm = tr.rotate(rz, [0,0,1]).T
    rym = tr.rotate(ry, [0,1,0]).T
    rxm = tr.rotate(rx, [1,0,0]).T
    trm = tr.translate(translate).T
    mm = trm @ rxm @ rym @ rzm @ sm
    return mm


class Mesh:

    def __init__(self, obj_filename, position, rotation, scale):

        vertices, faces, normals, texcoords = io.read_mesh(obj_filename)
        assert len(vertices[0]) == 3, "Vertices are 3D"
        assert len(faces[0]) == 3, "Mesh must be triangulated"
        self.vertices = vertices - np.mean(vertices, axis=0)
        self.faces = faces
        self.position = position
        self.rotation = rotation
        self.scale = scale

    @property
    def model_matrix(self):
        return make_model_matrix(self.position, self.rotation, self.scale)
