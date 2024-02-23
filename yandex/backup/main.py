def solution(n, k, ps):
    if n == 1:
        return 0
    time = -1
    capacities = [1] * n
    turned_off, to_turn_off = set(), []
    machines_map = {i + 1: [] for i in range(n)}

    # fill machines_map
    for child, parent in enumerate(ps):
        machines_map[parent].append(child + 1)

    # safely turn off machines dependent on the machine #n
    while capacities[n - 1] < k - 1:
        child = machines_map[n].pop()
        to_turn_off.append(child)
        capacities[n - 1] += 1

    # turn off machines dependent on ones that were just turned off
    while to_turn_off:
        parent = to_turn_off.pop()
        turned_off.add(parent)
        while machines_map[parent]:
            child = machines_map[parent].pop()
            turned_off.add(child)
            to_turn_off.extend(machines_map[child])
            time += 1
        time += 1

    # turn off machines sequentially while machine #n is ON
    for child, parent in enumerate(ps):
        to_turn_off_next_step = []

        while to_turn_off:
            machine = to_turn_off.pop(0)
            turned_off.add(machine)
            capacities[ps[machine - 2] - 1] += capacities[machine - 1]
            if capacities[ps[machine - 2] - 1] >= k:
                to_turn_off_next_step.append(ps[machine - 2])

        to_turn_off = to_turn_off_next_step

        if n in turned_off:
            time += 1
            break
        if (child + 1) not in turned_off:
            turned_off.add(child + 1)
            if parent not in turned_off:
                capacities[parent - 1] += capacities[child]
                if capacities[parent - 1] >= k:
                    to_turn_off.append(parent)
        else:
            continue

        time += 1

    if n not in turned_off:
        time += 1
        turned_off.add(n)

    return time


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        ps = map(int, input().split())

        time = solution(n, k, ps)
        print(time)


"""
4
6 3
6 6 6 6 6
4 3
2 3	4
1 3	
 	 
10 3	
8 8 8 9 9 9 10 10 10
"""
