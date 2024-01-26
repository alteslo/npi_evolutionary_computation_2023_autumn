import random


class Evolution:
    def __init__(self, ) -> None:
        pass

    def initial_population(self, size, min_value, max_value):
        """Initial population"""
        initial_population = [random.randint(
            min_value, max_value) for _ in range(size)]
        return initial_population

    def calculate_fitness(self, value):
        """Fitness function"""
        return value

    def mutate(self, parent1, parent2):
        """Mutate function"""
        child = parent1 if random.random() < 0.5 else parent2
        mutate = child + random.randint(-1, 1)
        return mutate

    def evolution(self, population, max_generation):
        """Evolution function"""

        generation = 0
        while generation < max_generation:
            population = sorted(population, key=self.calculate_fitness, reverse=True)
            print(f'Generation {generation}: {population}')
            next_generation = []
            for _ in range(int(len(population)/2)):
                parent1 = random.choice(population[:10])
                parent2 = random.choice(population[:10])
                child1 = self.mutate(parent1, parent2)
                child2 = self.mutate(parent1, parent2)
                next_generation += [child1, child2]
            population = next_generation
            generation += 1
        print(f'Generation {generation}: {population}')
        return max(population, key=self.calculate_fitness)


# Driving code
evolution_algo = Evolution()
population = evolution_algo.initial_population(20, 2, 20)
max_value = evolution_algo.evolution(population, 50)
print(f'Max Value: {max_value}')


# В этом коде мы создаем начальную популяцию из случайных чисел, затем в
# каждом поколении мы выбираем двух родителей, создаем двух детей с помощью
# мутации и заменяем старое поколение новым. Мы продолжаем этот процесс
# до тех пор, пока не достигнем максимального числа поколений,
# и в конце возвращаем максимальное значение из последнего поколения.
