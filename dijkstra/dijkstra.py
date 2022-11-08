infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

graph = {}
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

processed = []


def find_low_cost(costs):
    low_cost = float("inf")
    node_low_cost_more_low = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in processed:
            low_cost = cost
            node_low_cost_more_low = node
    return node_low_cost_more_low


node = find_low_cost(costs)
while node is not None:
    cost = costs[node]
    neighbor = graph[node]
    for n in neighbor.keys():
        new_cost = cost + neighbor[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_low_cost(costs)

print("Cost from the start to each node:")
print(costs)