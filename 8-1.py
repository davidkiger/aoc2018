file = open("8-1.in", "r")
# file = open("8-1.in.test", "r")


def parse_node(values):
    count_children = values.pop(0)
    count_metadata = values.pop(0)

    child_sum = 0
    for x in range(count_children):
        child_sum += parse_node(values)

    metadata_sum = 0
    for x in range(count_metadata):
        metadata_sum += values.pop(0)

    return child_sum + metadata_sum

for line in file:
    values = [int(x) for x in line.strip().split()]

print(parse_node(values))
