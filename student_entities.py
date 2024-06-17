"""
CPSC 5510, Seattle University, Project #3
:Author: Robert Widjaja
:Version: s23
"""

# YOU MAY NOT ADD ANY IMPORTS
from entity import Entity
from student_utilities import to_layer_2


def common_init(self, entity_id, neighbors):
    """
    You may call a common function like this from your individual __init__ 
    methods if you want.
    """
    self.id = entity_id
    self.neighbors = neighbors
    self.distance_table = {i: [float('inf')] * 4 for i in range(4)}
    self.distance_vector = [float('inf')] * 4
    self.distance_vector[entity_id] = 0

    # Initialize distance table with direct costs
    for neighbor, cost in neighbors.items():
        self.distance_table[entity_id][neighbor] = cost
        self.distance_vector[neighbor] = cost
    self.distance_table[entity_id][entity_id] = 0

    print(f"entity {self.id}: initializing")
    print(f"node {self.id}:")
    self.print_distance_table()
    self.send_update()

def common_update(self, packet):
    """
    You may call a common function like this from your individual update 
    methods if you want.
    """
    updated = False
    src = packet.src
    vector = packet.mincost

    print(f"node {self.id}: update from {src} received")
    for dest in range(4):
        if vector[dest] < self.distance_table[src][dest]:
            self.distance_table[src][dest] = vector[dest]
            new_cost = self.distance_table[self.id][src] + vector[dest]
            if new_cost < self.distance_vector[dest]:
                self.distance_vector[dest] = new_cost
                updated = True

    if updated:
        print("  changes based on update")
        self.print_distance_table()
        print("  sending mincost updates to neighbors")
        self.send_update()
    else:
        print(f"  no changes in node {self.id}, so nothing to do")
        self.print_distance_table()


def common_link_cost_change(self, to_entity, new_cost):
    """
    You may call a common function like this from your individual 
    link_cost_change methods if you want.
    Note this is only for extra credit and only required for Entity0 and 
    Entity1.
    """
    if to_entity in self.neighbors:
        self.neighbors[to_entity] = new_cost
        self.distance_table[self.id][to_entity] = new_cost
        self.recalculate_distance_vector()
        self.send_update()


def send_update(self):
    for neighbor in self.neighbors:
        to_layer_2(self.id, neighbor, self.distance_vector)


def recalculate_distance_vector(self):
    for dest in range(4):
        min_cost = float('inf')
        for neighbor in self.neighbors:
            new_cost = self.neighbors[neighbor] + self.distance_table[neighbor][dest]
            if new_cost < min_cost:
                min_cost = new_cost
        self.distance_vector[dest] = min_cost


def print_distance_table(self):
    for row in range(4):
        print([round(self.distance_table[row][col], 2) if self.distance_table[row][col] != float('inf') else 'inf' for col in range(4)])


class Entity0(Entity):
    """Router running a DV algorithm at node 0"""
    def __init__(self):
        super().__init__()
        common_init(self, 0, {1: 1, 2: 3, 3: 7})

    def update(self, packet):
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        common_link_cost_change(self, to_entity, new_cost)

    def send_update(self):
        send_update(self)

    def recalculate_distance_vector(self):
        recalculate_distance_vector(self)

    def print_distance_table(self):
        print_distance_table(self)


class Entity1(Entity):
    """Router running a DV algorithm at node 1"""
    def __init__(self):
        super().__init__()
        common_init(self, 1, {0: 1, 2: 1})

    def update(self, packet):
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        common_link_cost_change(self, to_entity, new_cost)

    def send_update(self):
        send_update(self)

    def recalculate_distance_vector(self):
        recalculate_distance_vector(self)

    def print_distance_table(self):
        print_distance_table(self)


class Entity2(Entity):
    """Router running a DV algorithm at node 2"""
    def __init__(self):
        super().__init__()
        common_init(self, 2, {0: 3, 1: 1, 3: 2})

    def update(self, packet):
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        common_link_cost_change(self, to_entity, new_cost)

    def send_update(self):
        send_update(self)

    def recalculate_distance_vector(self):
        recalculate_distance_vector(self)

    def print_distance_table(self):
        print_distance_table(self)


class Entity3(Entity):
    """Router running a DV algorithm at node 3"""
    def __init__(self):
        super().__init__()
        common_init(self, 3, {0: 7, 2: 2})

    def update(self, packet):
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        common_link_cost_change(self, to_entity, new_cost)

    def send_update(self):
        send_update(self)

    def recalculate_distance_vector(self):
        recalculate_distance_vector(self)

    def print_distance_table(self):
        print_distance_table(self)
