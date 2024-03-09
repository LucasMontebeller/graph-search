import string
import numpy as np

class Vertice():
    def __init__(self, name):
        self.name = name
        self.neighbours = {}
        self.total_distance = np.inf
        self.previous = None

    def add_neighbour(self, vertice, distance:int):
        self.neighbours[vertice] = distance

    def get_neighbours(self):
        return self.neighbours.items()
        

class Graph():
    def __init__(self):
        self.vertices = None
        self.v_initial = None
        self.v_final = None

    @staticmethod
    def gen_vertices(n:int):
        alphabet = list(string.ascii_uppercase)
        if n > len(alphabet):
            raise ValueError("The number of vertices is greater than the alphabet")
        
        vertices = set()
        for i in range(n):
            vertice = Vertice(alphabet[i])
            vertices.add(vertice)
        return vertices

    def add_obj(self, v_initial:Vertice, v_final:Vertice):
        if v_initial not in self.vertices or v_final not in self.vertices:
            raise ValueError("The initial or final vertices are not in the graph")
        self.v_initial = v_initial
        self.v_final = v_final

    def get_vertice(self, name:str):
        for vertice in self.vertices:
            if vertice.name == name:
                return vertice
        return None