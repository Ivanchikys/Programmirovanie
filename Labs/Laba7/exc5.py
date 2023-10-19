numbers = [1, 3, 4, 6, 2, 3, 5, 4, 1, 0, 1]
notreplay = set()
replay = set()

for number in numbers:
    if number in notreplay:
        replay.add(number)
    notreplay.add(number)

print(list(replay))