def twosum(num: list, target: int):
    memory = {}
    for index, num in enumerate(num):
        needed = target - num

        if needed in memory:
            return [memory[needed], index]
        memory[num] = index
    return []
