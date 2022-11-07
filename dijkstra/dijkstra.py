costs = {}

grafo["a"] = ["alice", "bob", "claire"]

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
    for n in neighbor.key():
        new_cost = cost + neighbot[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            father[n] = node
    processed.append(node)
    node = find_low_cost(costs)