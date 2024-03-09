import graph

if __name__ == "__main__":        
    def setup():
        g = graph.Graph()
        g.vertices = g.gen_vertices(12)
        A = g.get_vertice('A')
        B = g.get_vertice('B')
        C = g.get_vertice('C')
        D = g.get_vertice('D')
        E = g.get_vertice('E')
        F = g.get_vertice('F')
        G = g.get_vertice('G')
        H = g.get_vertice('H')
        I = g.get_vertice('I')
        J = g.get_vertice('J')
        K = g.get_vertice('K')
        L = g.get_vertice('L')

        A.add_neighbour(B, 4)
        A.add_neighbour(C, 7)

        B.add_neighbour(D, 8)
        B.add_neighbour(E, 3)

        C.add_neighbour(D, 8)
        C.add_neighbour(I, 2)

        D.add_neighbour(F, 6)
        D.add_neighbour(J, 3)

        E.add_neighbour(F, 6)
        E.add_neighbour(G, 6)

        F.add_neighbour(H, 8)
        F.add_neighbour(K, 1)

        G.add_neighbour(H, 8)

        H.add_neighbour(L, 8)

        I.add_neighbour(C, 2)
        I.add_neighbour(J, 3)

        J.add_neighbour(K, 1)

        K.add_neighbour(L, 8)

        g.add_obj(A, L)
        
        return g
    
    def dijkstra(self):
        self.v_initial.total_distance = 0
        unvisited = list(self.vertices)

        while unvisited:
            current = min(unvisited, key=lambda v: v.total_distance)

            if current == self.v_final: # current.total_distance == np.inf
                break

            for neighbour, distance in current.get_neighbours():
                if neighbour in unvisited:
                    total_distance = current.total_distance + distance
                    if total_distance < neighbour.total_distance:
                        neighbour.total_distance = total_distance
                        neighbour.previous = current

            unvisited.remove(current)
                        
        path = []
        current = self.v_final
        while current is not None:
            path.append(current)
            current = current.previous
        path.reverse()

        return path, self.v_final.total_distance

    g = setup()
    best_path, distance = dijkstra(g)
    print(f'Caminho minimo: {[vertice.name for vertice in best_path]}')
    print(f'Distância total: {distance}')
