def hanoi(n, start, goal, temp):
    if n <= 0:
        return

    hanoi(n-1, start, temp, goal)
    print(f'Disk {n} move from {start} to {goal}')
    hanoi(n-1, temp, goal, start)


if __name__ == '__main__':
    hanoi(3, 'A', 'C', 'B')
