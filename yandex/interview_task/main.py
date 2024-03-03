if __name__ == "__main__":
    n = int(input())

    values = [1, 1]
    prev_n = 1

    for cur_n in range(1, n):
        new_values = []
        for i in range(len(values) - 1):
            new_values.append(values[i])
            new_values.append(values[i] + values[i + 1])
        new_values.append(values[-1])
        values = new_values
        print(f"{cur_n + 1}: {values.count(cur_n + 1)}")
