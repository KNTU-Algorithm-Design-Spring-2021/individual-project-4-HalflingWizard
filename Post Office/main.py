weights = [int(n) for n in input("Please type in the weights (seperated by space): ").split()]
k = int(input("How many trucks? "))

truck_weights = [0] * k
weights.sort()

while weights:
    w = weights.pop()
    min = float('inf')
    min_index = 0
    for i, t_w in enumerate(truck_weights):
        if t_w + w <= min:
            min = t_w + w
            min_index = i
    truck_weights[min_index] = min

for i, truck_weight in enumerate(truck_weights):
    print(f'truck #{i}: {truck_weight}')
print()
