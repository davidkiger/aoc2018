file = open("8-1.in", "r")
# file = open("8-1.in.test", "r")


def parse_node(values):
    count_children = values.pop(0)
    count_metadata = values.pop(0)

    children = []
    for x in range(count_children):
        children.append(parse_node(values))

    node_sum = 0
    if count_children == 0:
        for x in range(count_metadata):
            node_sum += values.pop(0)
    else:
        for x in range(count_metadata):
            idx = values.pop(0) - 1
            if idx < len(children):
                node_sum += children[idx]

    return node_sum

for line in file:
    values = [int(x) for x in line.strip().split()]

print(parse_node(values))
