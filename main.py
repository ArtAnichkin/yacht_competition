from itertools import combinations
import csv
import sys

def generate_race_schedule(n: int, m: int) -> list:
    # Генерация всех возможных пар участников
    participants = list(range(1, n + 1))
    pairs = list(combinations(participants, 2))

    # Формирование заездов с учётом ограничения на количество лодок
    races = []
    while pairs:
        race = set()
        used_participants = set()
        
        for pair in pairs[:]:
            if len(used_participants.union(pair)) <= m:
                race.add(pair)
                used_participants.update(pair)
                pairs.remove(pair)
        
        races.append(race)
    
    # Формирование заездов с учётом ограничения на количество лодок
    races_persons = []
    for race in races:
        sup = []
        for p1, p2 in race:
            sup.extend([p1, p2])
        races_persons.append(list(set(sup)))

    return races_persons

def main(n, m):
    data = generate_race_schedule(n, m)
    with open('test.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == '__main__':
    print('')
    n = 21  # количество участников
    m = 7  # количество лодок
    main(n, m)
