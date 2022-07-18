def hanoi_tower(numbers, start, aux, end):
    if numbers == 0:
        return
    hanoi_tower(numbers - 1, start, end, aux)
    print(f'disk {numbers} from {start} to {end}')
    hanoi_tower(numbers - 1, aux, start, end)



hanoi_tower(3, "a", "b", "c")