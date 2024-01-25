import random


# Fitness function
def calculate_fitness(value):
    return value


# Initial population
def initial_population(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


# Mutate function
def mutate(parent1, parent2):
    child = parent1 if random.random() < 0.5 else parent2
    mutate = child + random.randint(-1, 1)
    return mutate


# Evolution function
def evolution(population, mutate, max_generation):
    generation = 0
    while generation < max_generation:
        population = sorted(population, key=calculate_fitness, reverse=True)
        print('Generation %s: %s' % (generation, population))
        next_generation = []
        for _ in range(int(len(population)/2)):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child1 = mutate(parent1, parent2)
            child2 = mutate(parent1, parent2)
            next_generation += [child1, child2]
        population = next_generation
        generation += 1
    return max(population, key=calculate_fitness)


# Driving code
population = initial_population(10, 2, 11)
max_value = evolution(population, mutate, 10)
print('Max Value: %s' % max_value)


# В этом коде мы создаем начальную популяцию из случайных чисел, затем в
# каждом поколении мы выбираем двух родителей, создаем двух детей с помощью
# мутации и заменяем старое поколение новым. Мы продолжаем этот процесс
# до тех пор, пока не достигнем максимального числа поколений,
# и в конце возвращаем максимальное значение из последнего поколения.
