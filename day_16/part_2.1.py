import networkx as nx
import matplotlib.pyplot as plt

# Doesn't work on the test data but works on actual input data lolol

def draw_graph(rooms, edges):
    graph = nx.Graph()
    colors = []
    for r in rooms:
        graph.add_node(r.name, flow_rate=r.flow_rate)
        colors.append(r.flow_rate)

    for e in edges:
        graph.add_edge(e.nodes[0], e.nodes[1], weight=e.weight)

    pos = nx.fruchterman_reingold_layout(graph)
    nx.draw_networkx(graph, pos=pos, node_color=colors, alpha=0.9)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels)
    plt.subplots_adjust(0, 0, 1, 1)
    plt.show()



def edge_key(node_1, node_2):
    return ''.join(sorted([node_1, node_2]))



class Room():
    def __init__(self, line):
        self.name = line.split(' ')[1]
        self.flow_rate = int(line.split('=')[1].split(';')[0])
        self.neighbours = [n.strip() for n in line.split(' valve')[1][1:].split(',')]
        self.active = False

    def __repr__(self) -> str:
        return f'{self.name} ({self.flow_rate}) => {self.neighbours}'


class Tunnel():
    def __init__(self, nodes, weight=1):
        self.nodes = sorted(nodes)
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.nodes[0]}-{self.nodes[1]} ({self.weight})'

    def key(self):
        return edge_key(self.nodes[0], self.nodes[1])



with open('input.txt') as f:
    lines = f.readlines()


# Set up room list & map
r_map = {}
for line in lines:
    room = Room(line)
    r_map[room.name] = room

# Set up edges
e_map = {}
for r in r_map.values():
    for n in r.neighbours:
        e_key = edge_key(r.name, n)
        if not e_key in e_map.keys():
            edge = Tunnel([r.name, n])
            e_map[e_key] = edge


# draw_graph(r_map.values(), e_map.values())



# Reduce graph
r_keys = list(r_map.keys())
for k in r_keys:
    r = r_map[k]
    if r and r.flow_rate == 0 and r.name != 'AA':
        rooms = r.neighbours
        for r1 in rooms:
            e1 = e_map.get(edge_key(r.name, r1))
            for r2 in rooms:
                e2 = e_map.get(edge_key(r.name, r2))
                if e1 and e2 and e1.key() != e2.key():
                    # Add new edge
                    edge = Tunnel([r1, r2], e1.weight + e2.weight)
                    if not e_map.get(edge_key(r1, r2)):
                        e_map[edge_key(r1, r2)] = edge
                        if r_map.get(r1):
                            r_map[r1].neighbours.append(r2)
                        if r_map.get(r2):
                            r_map[r2].neighbours.append(r1)

        # Remove old edges
        for n in rooms:
            r_map[n].neighbours.remove(r.name)
            if e_map.get(edge_key(n, r.name)):
                del e_map[edge_key(n, r.name)]

        # Remove node
        del r_map[k]


# [print(r) for r in r_map.values()]
# [print(e) for e in e_map.values()]
print(len(r_map.values()))


# draw_graph(r_map.values(), e_map.values())





def get_score(start, dest, time, e_map, r_map):
    # Get Shortest path
    distances = {}
    node = start.name
    dist_to_node = 0
    path_found = False
    # distances[node.name] = (0, True)
    while not path_found:
        # print(f'Visit {node}')
        room = r_map[node]
        for x in room.neighbours:
            x_dist = dist_to_node + e_map[edge_key(node, x)].weight
            if not distances.get(x):
                distances[x] = (x_dist, False)
            elif x_dist < distances[x][0]:
                distances[x] = (x_dist, distances[x][1])
            if x == dest.name:
                path_found = True
        # print(f'Set {node} to visited')
        distances[node] = (dist_to_node, True)
        # [k for k in ]
        # print(f'Potential: {distances.values()}')
        next_nodes = sorted([d for d in [(distances[k][0], k, distances[k][1]) for k in distances.keys()] if not d[2]])
        # print(f'Next: {next_nodes}')
        node = next_nodes[0][1]
        # node = next_name
        dist_to_node = distances[node][0]
        # print(f'New node: {node}')
        # input('pause')

    cost = distances[dest.name][0] + 1
    score = (time - cost) * dest.flow_rate if cost < time else 0

    return (score, cost)


time = 26
count = 0
total_rate = 0
node = r_map['AA']
while time > 0:
    options = [r for r in r_map.values() if r.name != node.name and not r.active]

    possible_scores = []
    for o in options:
        score, cost = get_score(node, o, time, e_map, r_map)
        rate = score / cost
        if score > 0:
            possible_scores.append((rate, o.name, score, cost, o.flow_rate))

    if len(possible_scores) > 0:
        possible_scores.sort(reverse=True)

        print(f'From {node.name} ({(30-time)}s, Rate: {total_rate})')
        for r, n, s, c, fr in possible_scores:
            print(f'   {n}: {s}, -{c}s ({r}/s) (fr: {fr})')

        # print(possible_scores)
        best = possible_scores[0]
        print(f'Select {best[1]}!\n')

        count += best[2]
        time -= best[3]
        total_rate += best[4]
        r_map[node.name].active = True
        node = r_map[best[1]]

    else:
        print(f'Finish time ({(30-time)}s, Rate:{total_rate})')
        # count += time * total_rate
        time = 0

    # input('Contine?')


print(count)



time = 26
node = r_map['AA']
while time > 0:
    options = [r for r in r_map.values() if r.name != node.name and not r.active]

    possible_scores = []
    for o in options:
        score, cost = get_score(node, o, time, e_map, r_map)
        rate = score / cost
        if score > 0:
            possible_scores.append((rate, o.name, score, cost, o.flow_rate))

    if len(possible_scores) > 0:
        possible_scores.sort(reverse=True)

        print(f'From {node.name} ({(30-time)}s, Rate: {total_rate})')
        for r, n, s, c, fr in possible_scores:
            print(f'   {n}: {s}, -{c}s ({r}/s) (fr: {fr})')

        # print(possible_scores)
        best = possible_scores[0]
        print(f'Select {best[1]}!\n')

        count += best[2]
        time -= best[3]
        total_rate += best[4]
        r_map[node.name].active = True
        node = r_map[best[1]]

    else:
        print(f'Finish time ({(30-time)}s, Rate:{total_rate})')
        # count += time * total_rate
        time = 0





print(count)


