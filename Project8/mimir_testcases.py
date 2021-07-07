import unittest
import string
import math
import random
import cProfile

from Graph import Graph, Vertex, AStarPriorityQueue


class GraphTests(unittest.TestCase):

    def test_01_vertex_methods(self):

        ### degree ###

        vertex = Vertex('a')
        vertex.adj['b'] = 1
        assert vertex.degree() == 1
        vertex.adj['c'] = 3
        assert vertex.degree() == 2

        ### visit/reset ###

        assert not vertex.visited
        vertex.visit()
        assert vertex.visited
        vertex.reset()
        assert not vertex.visited

        ### get_edges ###

        vertex = Vertex('a')
        solution = [('b', 1), ('c', 2)]

        vertex.adj['b'] = 1
        vertex.adj['c'] = 2

        subject = vertex.get_edges()
        assert subject == solution

        ### euclidean_distance ###

        vertex_a = Vertex('a')
        vertex_b = Vertex('b', 3, 4)

        subject = vertex_a.euclidean_distance(vertex_b)
        assert subject == 5
        subject = vertex_b.euclidean_distance(vertex_a)
        assert subject == 5

    def test_03_get_vertices(self):

        ### get_vertex ###

        graph = Graph()

        # Test basic vertex
        vertex_a = Vertex('a')
        graph.vertices['a'] = vertex_a
        subject = graph.get_vertex('a')
        assert subject == vertex_a

        ### get_vertices ###

        solution = [vertex_a]

        # Check with two vertices
        vertex = Vertex('$')
        graph.vertices['$'] = vertex
        solution.append(vertex)
        subject = graph.get_vertices()
        assert subject == solution

    def test_05_reset_vertices(self):

        graph = Graph()

        # Add and visit vertices
        graph.vertices['a'] = Vertex('a')
        graph.vertices['b'] = Vertex('b')

        for vertex in graph.vertices.values():
            vertex.visit()

        # Reset graph and check
        graph.reset_vertices()
        for vertex in graph.vertices.values():
            assert not vertex.visited

    def test_06_get_edges(self):

        ### get_edge ###

        graph = Graph()

        # Neither vertex exists
        subject = graph.get_edge('a', 'b')
        assert subject is None

        # One vertex exists
        graph.vertices['a'] = Vertex('a')
        subject = graph.get_edge('a', 'b')
        assert subject is None

        # Both vertices exist, but no edge
        graph.vertices['a'] = Vertex('a')
        graph.vertices['b'] = Vertex('b')
        subject = graph.get_edge('a', 'b')
        assert subject is None

        # a -> b exists but b -> a does not
        graph.vertices.get('a').adj['b'] = 331
        subject = graph.get_edge('a', 'b')
        assert subject == ('a', 'b', 331)
        subject = graph.get_edge('b', 'a')
        assert subject is None

        ### get_edges ###

        graph = Graph()

        # Test empty graph
        subject = graph.get_edges()
        assert subject == []

        # Test graph with vertices but no edges
        graph.vertices['a'] = Vertex('a')
        graph.vertices['b'] = Vertex('b')
        subject = graph.get_edges()
        assert subject == []

        # Test graph with one edge
        graph.vertices.get('a').adj['b'] = 331
        subject = graph.get_edges()
        assert subject == [('a', 'b', 331)]

        # Test graph with two edges (compare setwise since dict does not guarantee ordering)
        graph = Graph()
        graph.vertices['a'] = Vertex('a')
        graph.vertices['b'] = Vertex('b')
        graph.vertices.get('a').adj['b'] = 331
        graph.vertices.get('b').adj['a'] = 1855
        subject = graph.get_edges()
        subject_set = set(subject)
        solution_set = set([('a', 'b', 331), ('b', 'a', 1855)])
        assert subject_set == solution_set

    def test_08_add_to_graph(self):

        graph = Graph()

        # Test creation of single vertex
        graph.add_to_graph('a')
        size = graph.size
        assert size == 1
        subject = graph.get_vertices()
        assert subject == [Vertex('a')]

        graph.add_to_graph('b')
        size = graph.size
        assert size == 2
        subject = graph.get_vertices()
        subject_set = set(subject)
        solution_set = set([Vertex('a'), Vertex('b')])
        assert subject_set == solution_set

        # Test creation of edge between existing vertices
        graph.add_to_graph('a', 'b', 331)
        size = graph.size
        assert size == 2
        subject = graph.get_edges()
        assert subject == [('a', 'b', 331)]

        graph.add_to_graph('b', 'a', 1855)
        size = graph.size
        assert size == 2
        subject = graph.get_edges()
        subject_set = set(subject)
        solution_set = set([('a', 'b', 331), ('b', 'a', 1855)])
        assert subject_set == solution_set

    def test_10_construct_from_matrix(self):

        graph = Graph()

        # Test empty matrix
        matrix = [[]]
        graph.construct_from_matrix(matrix)
        size = graph.size
        assert size == 0
        v_subject = graph.get_vertices()
        e_subject = graph.get_edges()
        assert v_subject == []
        assert e_subject == []

        # Test single vertex with no connection
        matrix = [[None, 'a'],
                  ['a', None]]
        graph.construct_from_matrix(matrix)
        size = graph.size
        assert size == 1
        v_subject = graph.get_vertices()
        e_subject = graph.get_edges()
        assert v_subject == [Vertex('a')]
        assert e_subject == []

        # Test single vertex with connection
        graph = Graph()
        matrix = [[None, 'a'],
                  ['a', 331]]
        graph.construct_from_matrix(matrix)
        size = graph.size
        assert size == 1
        e_subject = graph.get_edges()
        assert e_subject == [('a', 'a', 331)]

        # Test two vertices with no connection
        graph = Graph()
        matrix = [[None, 'a', 'b'],
                  ['a', None, None],
                  ['b', None, None]]
        graph.construct_from_matrix(matrix)
        size = graph.size
        assert size == 2
        v_subject = graph.get_vertices()
        v_subject_set = set(v_subject)
        e_subject = graph.get_edges()
        assert v_subject_set == set([Vertex('a'), Vertex('b')])
        assert e_subject == []

        # Test two vertices with 2-way connection
        graph = Graph()
        matrix = [[None, 'a', 'b'],
                  ['a', None, 100],
                  ['b', 200, None]]
        graph.construct_from_matrix(matrix)
        size = graph.size
        assert size == 2
        e_subject = graph.get_edges()
        e_subject_set = set(e_subject)
        assert e_subject_set == set([('a', 'b', 100), ('b', 'a', 200)])

    def test_12_bfs(self):

        graph = Graph()

        # Test on empty graph
        subject = graph.bfs('a', 'b')
        assert subject == ([], 0)

        # Test on graph missing start or dest
        graph.add_to_graph('a')
        subject = graph.bfs('a', 'b')
        assert subject == ([], 0)
        subject = graph.bfs('b', 'a')
        assert subject == ([], 0)

        # Test on graph with both vertices but no path
        graph.add_to_graph('b')
        subject = graph.bfs('a', 'b')
        assert subject == ([], 0)

        # Test on single edge
        graph = Graph()
        graph.add_to_graph('a', 'b', 331)
        subject = graph.bfs('a', 'b')
        assert subject == (['a', 'b'], 331)

        # Test on two edges
        graph = Graph()
        graph.add_to_graph('a', 'b', 331)
        graph.add_to_graph('b', 'c', 100)
        subject = graph.bfs('a', 'c')
        assert subject == (['a', 'b', 'c'], 431)

        # Test on edge triangle and ensure fewest hops
        graph = Graph()
        graph.add_to_graph('a', 'b', 331)
        graph.add_to_graph('b', 'c', 100)
        graph.add_to_graph('a', 'c', 999)
        subject = graph.bfs('a', 'c')
        assert subject == (['a', 'c'], 999)

        # Custom Test Case
        graph = Graph()
        graph.add_to_graph('a', 'b', 4)
        graph.add_to_graph('a', 'c', 1)
        graph.add_to_graph('b', 'd', 3)
        graph.add_to_graph('c', 'd', 2)
        graph.add_to_graph('b', 'e', 8)
        graph.add_to_graph('d', 'e', 4)
        graph.add_to_graph('c', 'f', 6)
        graph.add_to_graph('e', 'g', 2)
        graph.add_to_graph('f', 'g', 8)
        subject = graph.bfs('a', 'g')
        assert subject == (['a', 'b', 'e', 'g'], 14)

    def test_14_dfs(self):

        graph = Graph()

        # Test on empty graph
        subject = graph.dfs('a', 'b')
        assert subject == ([], 0)

        # Test on graph missing start or dest
        graph.add_to_graph('a')
        subject = graph.dfs('a', 'b')
        assert subject == ([], 0)
        subject = graph.dfs('b', 'a')
        assert subject == ([], 0)

        # Test on graph with both vertices but no path
        graph.add_to_graph('b')
        subject = graph.dfs('a', 'b')
        assert subject == ([], 0)

        # Test on single edge
        # graph = Graph()
        # graph.add_to_graph('a', 'b', 331)
        # subject = graph.dfs('a', 'b')
        # assert subject == (['a', 'b'], 331)
#
        # Test on two edges
        # graph = Graph()
        # graph.add_to_graph('a', 'b', 331)
        # graph.add_to_graph('b', 'c', 100)
        # subject = graph.dfs('a', 'c')
        # assert subject == (['a', 'b', 'c'], 431)

        # Test on linear chain with backtracking distractors
        # graph = Graph()
        # graph.add_to_graph('a', 'b', 1)
        # graph.add_to_graph('b', 'a', 2)
        # graph.add_to_graph('b', 'c', 1)
        # graph.add_to_graph('c', 'b', 2)
        # graph.add_to_graph('c', 'd', 1)
        # graph.add_to_graph('d', 'c', 2)
        # graph.add_to_graph('d', 'e', 1)
        # graph.add_to_graph('e', 'd', 2)
        # subject = graph.dfs('a', 'e')
        # assert subject == (['a', 'b', 'c', 'd', 'e'], 4)

        # Custom Test
        graph = Graph()
        graph.add_to_graph('6', '4', 1)
        graph.add_to_graph('4', '5', 1)
        graph.add_to_graph('4', '3', 1)
        graph.add_to_graph('5', '1', 1)
        graph.add_to_graph('5', '2', 1)
        graph.add_to_graph('3', '2', 1)
        graph.add_to_graph('2', '1', 1)
        graph.add_to_graph('2', '5', 1)
        subject = graph.dfs('6', '5')

    def test_16_a_star_msu(self):

        graph = Graph()
        vertices = [Vertex('A', 0, 0), Vertex('B', 2, 0), Vertex('C', 4, 0), Vertex('D', 6, 0), Vertex('E', 9, 0),
                    Vertex('F', 12, 0), Vertex('G', 2, 5), Vertex(
                        'H', 6, 4), Vertex('I', 12, 4), Vertex('J', 5, 9),
                    Vertex('K', 8, 8), Vertex('L', 12, 8), Vertex(
                        'M', 8, 10), Vertex('Breslin Center', 0, 2),
                    Vertex('Spartan Stadium', 4, 2), Vertex('Wells Hall',
                                                            9, 2), Vertex('Engineering Building', 9, -2),
                    Vertex('Library', 7, 6), Vertex('Union', 8, 11), Vertex('The Rock', 14, 8)]
        for vertex in vertices:
            graph.vertices[vertex.id] = vertex

        edges = [('A', 'B', 8), ('B', 'C', 8), ('C', 'D', 8), ('D', 'E', 12), ('E', 'F', 12), ('B', 'G', 5),
                 ('D', 'H', 4), ('F', 'I', 16),
                 ('G', 'H', 5), ('H', 'I', 6), ('G', 'J',
                                                5), ('I', 'L', 16), ('J', 'K', 4), ('K', 'L', 4),
                 ('J', 'M', 4), ('M', 'L', 4),
                 ('Breslin Center', 'A', 0), ('Spartan Stadium', 'C', 0), ('Wells Hall', 'E', 0),
                 ('Engineering Building', 'E', 0),
                 ('Library', 'K', 0), ('Union', 'M', 0), ('The Rock', 'L', 0)]
        for edge in edges:
            # add edge in both directions
            graph.add_to_graph(edge[0], edge[1], edge[2])
            graph.add_to_graph(edge[1], edge[0], edge[2])

        # test Breslin to Union shortest path
        subject = graph.a_star('Breslin Center', 'Union')
        path = ['Breslin Center', 'A', 'B', 'G', 'J', 'M', 'Union']
        print(subject)
        assert subject == (path, 22)
        graph.reset_vertices()
        path.reverse()
        subject = graph.a_star('Union', 'Breslin Center')
        print(subject)
        assert subject == (path, 22)
        graph.reset_vertices()

        # test Breslin to EB shortest path - bypass slow Shaw Ln
        # subject = graph.a_star('Breslin Center', 'Engineering Building')
        # path = ['Breslin Center', 'A', 'B', 'G', 'H', 'D', 'E', 'Engineering Building']
        # assert subject == (path, 34)
#         graph.reset_vertices()
#         path.reverse()
#         subject = graph.a_star('Engineering Building', 'Breslin Center')
#         assert subject == (path, 34)
#         graph.reset_vertices()
#         # test EB to The Rock shortest path - bypass slow Farm Ln
#         subject = graph.a_star('Engineering Building', 'The Rock')
#         path = ['Engineering Building', 'E', 'D', 'H', 'G', 'J', 'K', 'L', 'The Rock']
#         assert subject == (path, 34)
#         graph.reset_vertices()
#         path.reverse()
#         subject = graph.a_star('The Rock', 'Engineering Building')
#         assert subject == (path, 34)
#         graph.reset_vertices()
#
#         # test Union to Library - despite equal path lengths, A* heuristic will direct search to left
#         subject = graph.a_star('Union', 'Library')
#         path = ['Union', 'M', 'J', 'K', 'Library']
#         assert subject == (path, 8)
#         graph.reset_vertices()
#         path.reverse()
#         subject = graph.a_star('Library', 'Union')
#         assert subject == (path, 8)
#         graph.reset_vertices()
#
    def test_18_construct_matrix_from_graph(self):

        graph = Graph()

        # Test Empty Graph
        subject = graph.construct_matrix_from_graph()
        assert not subject

        # Test single vertex with no connection
        matrix = [[None, 'a'],
                  ['a', None]]
        graph.construct_from_matrix(matrix)
        subject = graph.construct_matrix_from_graph()
        assert subject == matrix

        # Test single vertex with connection
        graph = Graph()
        matrix = [[None, 'a'],
                  ['a', 331]]
        graph.construct_from_matrix(matrix)
        subject = graph.construct_matrix_from_graph()
        assert subject == matrix

        # Test two vertices with no connection
        graph = Graph()
        matrix = [[None, 'a', 'b'],
                  ['a', None, None],
                  ['b', None, None]]
        graph.construct_from_matrix(matrix)
        subject = graph.construct_matrix_from_graph()
        assert subject == matrix

        # Test two vertices with 2-way connection
        graph = Graph()
        matrix = [[None, 'a', 'b'],
                  ['a', None, 100],
                  ['b', 200, None]]
        graph.construct_from_matrix(matrix)
        subject = graph.construct_matrix_from_graph()
        assert subject == matrix
#
#     def test_20_construct_from_csv(self):
#
#         graph = Graph()
#
#         # Empty csv
#         graph.construct_from_csv('test1.csv')
#         assert graph == Graph()
#
#         # Varied, different edge weights
#         graph.construct_from_csv('test2.csv')
#         size = graph.size
#         assert size == 3
#         e_subject = graph.get_edges()
#         e_subject_set = set(e_subject)
#         v_subject = graph.get_vertices()
#         v_subject_set = set(v_subject)
#         vertex_a = Vertex('a')
#         vertex_b = Vertex('b')
#         vertex_c = Vertex('c')
#         vertex_b.adj['a'] = 2.0
#         vertex_b.adj['c'] = 3.0
#         vertex_c.adj['b'] = 1.0
#         vertex_a.adj['b'] = 1.0
#         v_solution_set = set([vertex_a, vertex_b, vertex_c])
#         e_solution_set = set([('a', 'b', 1.0), ('b', 'a', 2.0), ('c', 'b', 1.0), ('b', 'c', 3.0)])
#         assert e_subject_set == e_solution_set
#         assert v_subject_set == v_solution_set
#
#     def build_msu_graph(self, plt_show=False):
#
#         graph = Graph(plt_show)
#         vertices = [Vertex('A', 0, 0.01), Vertex('B', 2, 0), Vertex('C', 4, 0), Vertex('D', 6, 0), Vertex('E', 9, 0),
#                     Vertex('F', 12, 0), Vertex('G', 2, 5), Vertex(
#                         'H', 6, 4), Vertex('I', 12, 4), Vertex('J', 5, 9),
#                     Vertex('K', 8, 8), Vertex('L', 12, 8), Vertex(
#                         'M', 8, 10), Vertex('Breslin Center', 0, 2),
#                     Vertex('Spartan Stadium', 4, 2), Vertex('Wells Hall',
#                                                             9, 2), Vertex('Engineering Building', 9, -2),
#                     Vertex('Library', 7, 6), Vertex('Union', 8, 11), Vertex('The Rock', 14, 8)]
#         for vertex in vertices:
#             graph.vertices[vertex.id] = vertex
#
#         edges = [('A', 'B', 8), ('B', 'C', 8), ('C', 'D', 8), ('D', 'E', 12), ('E', 'F', 12), ('B', 'G', 5), ('D', 'H', 4), ('F', 'I', 16),
#                  ('G', 'H', 5), ('H', 'I', 6), ('G', 'J', 5), ('I', 'L',
#                                                                16), ('J', 'K', 4), ('K', 'L', 4), ('J', 'M', 4), ('M', 'L', 4),
#                  ('Breslin Center', 'A', 0), ('Spartan Stadium', 'C',
#                                               0), ('Wells Hall', 'E', 0), ('Engineering Building', 'E', 0),
#                  ('Library', 'K', 0), ('Union', 'M', 0), ('The Rock', 'L', 0)]
#         for edge in edges:
#             # add edge in both directions
#             graph.add_to_graph(edge[0], edge[1], edge[2])
#             graph.add_to_graph(edge[1], edge[0], edge[2])
#
#         return graph
#
#
if __name__ == '__main__':
    unittest.main()
