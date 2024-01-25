import random


POPULATION_SIZE = 10  # Количество особей в популяции
MAX_GENERATIONS = 100  # Максимальное количество поколений
NUMBERS = [10, 8, 6, 4, 2]  # Заданный список чисел
MUTATION_RATE = 0.1  # Вероятность мутации (от 0 до 1)


# Функция для вычисления фитнес-значения особи
def calculate_fitness(individual):
    total = sum(individual)
    return total


# Создание случайного индивида
def create_individual():
    return [random.randint(0, 1) for _ in range(len(NUMBERS))]


# Создание начальной популяции
def create_population():
    return [create_individual() for _ in range(POPULATION_SIZE)]


# Скрещивание двух индивидов
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(NUMBERS) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


# Мутация индивида
def mutate(individual):
    mutation_point = random.randint(0, len(NUMBERS) - 1)
    individual[mutation_point] = 1 - individual[mutation_point]
    return individual


# Генетический алгоритм
def genetic_algorithm():
    population = create_population()

    for generation in range(MAX_GENERATIONS):
        # Вычисление фитнес-значения всех особей в популяции
        fitness_values = [calculate_fitness(
            individual) for individual in population]

        # Нахождение индекса особи с наибольшим фитнес-значением
        max_fitness_index = fitness_values.index(max(fitness_values))
        max_fitness_individual = population[max_fitness_index]
        max_fitness = fitness_values[max_fitness_index]

        # Печать текущего поколения и лучшего результата
        print(
            f"Generation {generation+1}: {max_fitness_individual}, Fitness: {max_fitness}")

        # Создание новой популяции
        new_population = []

        # Селекция и скрещивание
        for _ in range(POPULATION_SIZE):
            parent1 = random.choices(population, weights=fitness_values)[0]
            parent2 = random.choices(population, weights=fitness_values)[0]
            child = crossover(parent1, parent2)
            new_population.append(child)

        # Мутация
        for individual in new_population:
            if random.random() < MUTATION_RATE:
                mutate(individual)

        population = new_population

    # Возвращение лучшего результата
    return max_fitness_individual, max_fitness


# Запуск генетического алгоритма
best_individual, best_fitness = genetic_algorithm()

# Печать полученного результата
print(f"Best Individual: {best_individual}, Best Fitness: {best_fitness}")
