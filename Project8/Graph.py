"""
Name:
CSE 331 SS20 (Onsay)
"""

import queue, heapq, math, itertools
from collections import OrderedDict
import matplotlib.pyplot as plt, matplotlib.patches as patches, matplotlib.cm as cm
import numpy as np
import time
import random


class Vertex:
    """
    Class representing a Vertex object within a Graph
    """

    __slots__ = ['id', 'adj', 'visited', 'x', 'y']

    def __init__(self, idx, x=0, y=0):
        """
        DO NOT MODIFY
        Initializes a Vertex
        :param idx: A unique string identifier used for hashing the vertex
        :param x: The x coordinate of this vertex (used in a_star)
        :param y: The y coordinate of this vertex (used in a_star)
        """
        self.id = idx
        self.adj = OrderedDict()  # dictionary {id : weight} of outgoing edges
        self.visited = False      # Boolean flag used in search algorithms
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        DO NOT MODIFY
        Overloads equality operator for Graph Vertex class
        :param other: vertex to compare
        """
        return (self.id == other.id
                and self.adj == other.adj
                and self.visited == other.visited
                and self.x == other.x
                and self.y == other.y)

    def __repr__(self):
        """
        DO NOT MODIFY
        Represents Vertex as string
        :return: string representing Vertex object
        """
        lst = [f"<id: '{k}', weight: {v}>" for k, v in self.adj.items()]

        return f"<id: '{self.id}'" + ", Adjacencies: " + "".join(lst) + ">"

    def __str__(self):
        """
        DO NOT MODIFY
        Represents Vertex as string
        :return: string representing Vertex object
        """
        return repr(self)

    def __hash__(self):
        """
        DO NOT MODIFY
        Hashes Vertex into a set; used in unit tests
        :return: hash value of Vertex
        """
        return hash(self.id)

    def degree(self):
        """

        :return: number of connected vertex
        """
        return len(self.adj)

    def visit(self):
        """

        :return: visited vertex or not
        """
        self.visited = True

    def reset(self):
        """

        :return: reset visited
        """
        self.visited = False

    def get_edges(self):
        """

        :return: return edges
        """
        result = []
        if self.degree() > 0:
            for key, value in self.adj.items():
                result.append((key, value))
        return result

    def euclidean_distance(self, other):
        """

        :param other: another vertex
        :return: distance between two verticies
        """
        x_len = other.x - self.x
        y_len = other.y - self.y
        result = math.sqrt((x_len * x_len) + (y_len * y_len))
        if result == int(result):
            result = int(result)
        return result


class Graph:
    """
    Class implementing the Graph ADT using an Adjacency Map structure
    """

    __slots__ = ['size', 'vertices', 'plot_show', 'plot_delay']

    def __init__(self, plt_show=False):
        """
        DO NOT MODIFY
        Instantiates a Graph class instance
        :param: plt_show : if true, render plot when plot() is called; else, ignore calls to plot()
        """
        self.size = 0
        self.vertices = OrderedDict()
        self.plot_show = plt_show
        self.plot_delay = 0.2

    def __eq__(self, other):
        """
        DO NOT MODIFY
        Overloads equality operator for Graph class
        :param other: graph to compare
        """
        return self.vertices == other.vertices and self.size == other.size

    def __repr__(self):
        """
        DO NOT MODIFY
        :return: String representation of graph for debugging
        """
        return "Size: " + str(self.size) + ", Vertices: " + str(list(self.vertices.items()))

    def __str__(self):
        """
        DO NOT MODFIY
        :return: String representation of graph for debugging
        """
        return repr(self)

    def plot(self):
        """
        Modify if you'd like - use for debugging!
        :return: Plot a visual representation of the graph using matplotlib
        """
        if self.plot_show:
            # seed random generator to reproduce random placements if no x,y specified
            random.seed(2020)

            # show edges
            max_weight = max([edge[2] for edge in self.get_edges()])
            colormap = cm.get_cmap('cool')
            for edge in self.get_edges():
                origin = self.get_vertex(edge[0])
                destination = self.get_vertex(edge[1])
                weight = edge[2]

                # if no x, y coords are specified, randomly place in (0,1)x(0,1)
                if not origin.x and not origin.y:
                    origin.x, origin.y = random.random(), random.random()
                if not destination.x and not destination.y:
                    destination.x, destination.y = random.random(), random.random()

                # plot edge
                arrow = patches.FancyArrowPatch((origin.x, origin.y), (destination.x, destination.y),
                                                connectionstyle="arc3,rad=.2", color=colormap(weight / max_weight),
                                                zorder=0,
                                                **dict(arrowstyle="Simple,tail_width=0.5,head_width=8,head_length=8"))
                plt.gca().add_patch(arrow)

                # label edge
                plt.text((origin.x + destination.x) / 2 - (origin.x - destination.x) / 10,
                         (origin.y + destination.y) / 2 - (origin.y - destination.y) / 10,
                         weight, color=colormap(weight / max_weight))

            # show vertices
            x = np.array([vertex.x for vertex in self.get_vertices()])
            y = np.array([vertex.y for vertex in self.get_vertices()])
            labels = np.array([vertex.id for vertex in self.get_vertices()])
            colors = np.array(['yellow' if vertex.visited else 'black' for vertex in self.get_vertices()])
            plt.scatter(x, y, s=40, c=colors, zorder=1)

            # plot labels
            for i in range(len(x)):
                plt.text(x[i] - 0.03 * max(x), y[i] - 0.03 * max(y), labels[i])

            # show plot
            plt.show()
            # delay execution to enable animation
            time.sleep(self.plot_delay)

    def reset_vertices(self):
        """

        :return: reset all vertices
        """
        for vertex in self.vertices.values():
            vertex.reset()

    def get_vertex(self, vertex_id):
        """

        :param vertex_id: vertex id
        :return: vertex
        """
        return self.vertices.get(vertex_id)

    def get_vertices(self):
        """

        :return: all vertices in the graph
        """
        result = []
        for vertex in self.vertices.values():
            result.append(vertex)
        return result

    def get_edge(self, start_id, dest_id):
        """

        :param start_id: start vertex
        :param dest_id: end vertex
        :return: tuple of start id, dest, id and the weight
        """
        if self.get_vertex(start_id) is None or self.get_vertex(dest_id) is None:
            return None
        elif dest_id in self.get_vertex(start_id).adj:
            return start_id, dest_id, self.get_vertex(start_id).adj[dest_id]
        return None

    def get_edges(self):
        """

        :return: all edges in the graph
        """
        result = []
        for vertex in self.vertices.values():
            for edges in vertex.adj.items():
                result.append((vertex.id, edges[0], edges[1]))
        return result

    def add_to_graph(self, start_id, dest_id=None, weight=0):
        """

        :param start_id: start id
        :param dest_id: end it
        :param weight: weight of this edge
        :return: None
        """
        if self.get_vertex(start_id) is None:
            self.vertices[start_id] = Vertex(start_id)
            self.size += 1
        if self.get_vertex(dest_id) is None:
            if dest_id is not None:
                self.vertices[dest_id] = Vertex(dest_id)
                self.size += 1
        if dest_id is not None:
            self.vertices.get(start_id).adj[dest_id] = weight

    def construct_from_matrix(self, matrix):
        """

        :param matrix: matrix representation of the graph
        :return: none
        """
        if len(matrix) >= 2:
            r = 1
            while r < len(matrix[0]):
                c = 1
                while c < len(matrix[0]):
                    if matrix[r][c] is None:
                        if matrix[r][0] == matrix[0][c]:
                            self.add_to_graph(matrix[r][0])
                        else:
                            self.add_to_graph(matrix[r][0])
                            self.add_to_graph(matrix[0][c])
                    else:
                        self.add_to_graph(matrix[r][0], matrix[0][c], matrix[r][c])
                    c += 1
                r += 1

    def construct_from_csv(self, csv):
        pass

    def construct_matrix_from_graph(self):
        """

        :return: matrix repserentaion of the graph
        """
        matrix = [[None]]
        if not self.get_vertices():
            return None
        for vertex in self.get_vertices():
            matrix.append([vertex.id])
            matrix[0].append(vertex.id)
        for c in range(1, len(self.get_vertices()) + 1):
            for r in range(1, len(self.get_vertices()) + 1):
                id1 = matrix[0][c]
                id2 = matrix[r][0]
                edge = self.get_edge(id2, id1)
                if edge is None:
                    matrix[r].append(None)
                else:
                    matrix[r].append(edge[2])
        return matrix

    def bfs(self, start_id, target_id):
        """

        :param start_id: start id
        :param target_id: end id
        :return: tuple of path and distance
        """
        path = []
        distance = 0
        if start_id == target_id:
            return path, distance
        if self.get_vertex(start_id) is None or self.get_vertex(target_id) is None:
            return path, distance

        dict = OrderedDict()
        frontier = queue.Queue()
        frontier.put(start_id)
        while frontier.empty() is False:
            current = frontier.get()
            visit = self.get_vertex(current)
            visit.visited = True

            adjacent = visit.get_edges()
            for key, value in adjacent:
                adjv = self.get_vertex(key)
                if adjv.visited is False:
                    adjv.visited = True
                    frontier.put(adjv.id)
                    dict[key] = current

        reached = self.get_vertex(target_id)
        if reached.visited is True:
            value = dict[target_id]
            key = target_id
            path.append(key)
            while True:
                path.append(value)
                edge = self.get_edge(value, key)
                distance += edge[2]
                if value == start_id:
                    break
                key = value
                value = dict[key]
            path.reverse()
        return path, distance

    def dfs(self, start_id, target_id):
        """

        :param start_id: start id
        :param target_id: end id
        :return: tuple of path and distance
        """
        path = []
        dist = 0
        if start_id == target_id:
            return path, dist
        if self.get_vertex(start_id) is None or self.get_vertex(target_id) is None:
            return path, dist

        self._dfs_recursive(start_id, target_id, path, dist)
        reached = self.get_vertex(target_id)
        if reached.visited is False:
            return [], 0
        path.reverse()
        path = list(dict.fromkeys(path))
        for i in range(len(path)-1):
            v1 = self.get_vertex(path[i])
            v2 = self.get_vertex(path[i+1])
            edge = self.get_edge(v1.id, v2.id)
            dist += edge[2]
        return path, dist

    def _dfs_recursive(self, current_id, target_id, path=[], dist=0):
        """

        :param current_id: current id
        :param target_id: end id
        :param path: path to get to target
        :param dist: distance
        :return: depends
        """
        current_v = self.get_vertex(current_id)
        if current_v.visited is False:
            current_v.visited = True
            if current_id == target_id:
                path.append(current_id)
                return
            adjacent = current_v.get_edges()
            for adj_v in adjacent:
                check = self._dfs_recursive(adj_v[0], target_id, path, dist)
                if check != 'a':
                    path.append(current_id)
        else:
            return 'a'

    def a_star(self, start_id, target_id):
        """

        :param start_id: start id
        :param target_id: end it
        :return: tuple of path and distance
        """
        path = []
        visited = []
        distance = 0
        pq = AStarPriorityQueue()
        dict = OrderedDict()
        weight_dict = OrderedDict()
        if start_id != target_id:
            check_id = start_id
            check_v = self.get_vertex(check_id)
            check_v.visit()
            end_v = self.get_vertex(target_id)
            pq.push(0, check_v)
            weight_dict[start_id] = 0

            while check_v != end_v:
                adjacent = check_v.get_edges()
                for adj_v in adjacent:
                    ver = self.get_vertex(adj_v[0])
                    euc_val = ver.euclidean_distance(end_v)
                    edge = self.get_edge(check_v.id, ver.id)
                    priority = edge[2] + euc_val + distance
                    if ver.visited is False:
                        dict[ver.id] = check_v.id
                    pq.push(priority, ver)
                next = pq.pop()
                for i in visited:
                    if i == next[1].id:
                        if pq.empty() is True:
                            return [], 0
                        else:
                            next = pq.pop()
                visited.append(next[1].id)
                weight = next[0] - next[1].euclidean_distance(end_v) - distance
                distance += weight
                check_v = next[1]

            # while not pq.empty():
            #     next = pq.pop()
            #     i = 0
            #     while i < len(visited):
            #         if visited[i] == next[1].id:
            #             if not pq.empty():
            #                 next = pq.pop()
            #                 i = 0
            #             else:
            #                 break
            #         else:
            #             i += 1
            #     check_v = next[1]
            #     if check_v == end_v:
            #         break
            #     distance = weight_dict[check_v.id]
            #     visited.append(check_v.id)
            #
            #     adjacent = check_v.get_edges()
            #     for adj_v in adjacent:
            #         ver = self.get_vertex(adj_v[0])
            #         euc_val = ver.euclidean_distance(end_v)
            #         edge = self.get_edge(check_v.id, ver.id)
            #         priority = edge[2] + euc_val + distance
            #         if ver.visited is False:
            #             weight_dict[ver.id] = edge[2] + distance
            #             dict[ver.id] = check_v.id
            #             pq.push(priority, ver)
            #         else:
            #             pq.update(priority, ver)

            distance = 0
            value = dict[target_id]
            key = target_id
            path.append(key)
            path.append(value)
            while value != start_id:
                key = value
                value = dict[key]
                path.append(value)
                edge = self.get_edge(value, key)
                distance += edge[2]
            path.reverse()
            return path, distance
        pass

    def make_equivalence_relation(self):
        pass


class AStarPriorityQueue:
    """
    Priority Queue built upon heapq module with support for priority key updates
    Created by Andrew McDonald
    Inspired by https://docs.python.org/2/library/heapq.html
    """

    __slots__ = ['__data', '__locator', '__counter']

    def __init__(self):
        """
        Construct an AStarPriorityQueue object
        """
        self.__data = []                        # underlying data list of priority queue
        self.__locator = {}                     # dictionary to locate vertices within priority queue
        self.__counter = itertools.count()      # used to break ties in prioritization

    def __repr__(self):
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        lst = [f"[{priority}, {vertex}], " if vertex is not None else "" for priority,
              count, vertex in self.__data]
        return "".join(lst)[:-1]

    def __str__(self):
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        return repr(self)

    def empty(self):
        """
        Determine whether priority queue is empty
        :return: True if queue is empty, else false
        """
        return len(self.__data) == 0

    def push(self, priority, vertex):
        """
        Push a vertex onto the priority queue with a given priority
        :param priority: priority key upon which to order vertex
        :param vertex: Vertex object to be stored in the priority queue
        :return: None
        """
        count = next(self.__counter)
        # list is stored by reference, so updating will update all refs
        node = [priority, count, vertex]
        self.__locator[vertex.id] = node
        heapq.heappush(self.__data, node)

    def pop(self):
        """
        Remove and return the (priority, vertex) tuple with lowest priority key
        :return: (priority, vertex) tuple where priority is key,
        and vertex is Vertex object stored in priority queue
        """
        vertex = None
        while vertex is None:
            # keep popping until we have valid entry
            priority, count, vertex = heapq.heappop(self.__data)
        del self.__locator[vertex.id]                   # remove from locator dict
        vertex.visit()                  # indicate that this vertex was visited
        while len(self.__data) > 0 and self.__data[0] is None:
            heapq.heappop(self.__data)  # remove Nones after valid vertex
        return priority, vertex

    def update(self, new_priority, vertex):
        """
        Update given Vertex object in the priority queue to have new priority
        :param new_priority: new priority on which to order vertex
        :param vertex: Vertex object for which priority is to be updated
        :return: None
        """
        node = self.__locator.pop(vertex.id)    # delete from dictionary
        node[-1] = None                         # invalidate old node
        self.push(new_priority, vertex)         # push new node
