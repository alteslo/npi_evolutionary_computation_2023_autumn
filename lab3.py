import numpy as np


class Particle:
    def __init__(self, num_dimensions, min_bound, max_bound):
        self.position = np.random.uniform(min_bound, max_bound, num_dimensions)
        self.velocity = np.zeros(num_dimensions)
        self.best_position = self.position.copy()
        self.best_fitness = np.inf


class PSO:
    def __init__(
            self, num_particles, num_dimensions,
            min_bound, max_bound, fitness_function,
            max_iterations=50, inertia_weight=0.7298,
            cognitive_weight=1.49445, social_weight=1.49445
    ):
        self.num_particles = num_particles
        self.num_dimensions = num_dimensions
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.fitness_function = fitness_function
        self.max_iterations = max_iterations
        self.inertia_weight = inertia_weight
        self.cognitive_weight = cognitive_weight
        self.social_weight = social_weight
        self.gbest_position = np.zeros(num_dimensions)
        self.gbest_fitness = np.inf
        self.particles = []

    def optimize(self):
        # Initialize particles
        for _ in range(self.num_particles):
            particle = Particle(self.num_dimensions,
                                self.min_bound, self.max_bound)
            self.particles.append(particle)

        # Run optimization iterations
        for iteration in range(self.max_iterations):
            for particle in self.particles:
                # Evaluate fitness
                fitness = self.fitness_function(particle.position)

                # Update personal best
                if fitness < particle.best_fitness:
                    particle.best_fitness = fitness
                    particle.best_position = particle.position.copy()

                # Update global best
                if fitness < self.gbest_fitness:
                    self.gbest_fitness = fitness
                    self.gbest_position = particle.position.copy()

                # Update velocity and position
                particle.velocity = (self.inertia_weight * particle.velocity +
                                     self.cognitive_weight * np.random.random() * (particle.best_position - particle.position) +
                                     self.social_weight * np.random.random() * (self.gbest_position - particle.position))
                particle.position += particle.velocity

                # Clamp position within bounds
                particle.position = np.clip(
                    particle.position, self.min_bound, self.max_bound)

            # Print iteration information
            print("Iteration:", iteration + 1,
                  " Best Fitness:", self.gbest_fitness)

        return self.gbest_position


def sphere_function(x):
    return np.sum(x ** 2)


num_particles = 20
num_dimensions = 10
min_bound = -5
max_bound = 5

pso = PSO(num_particles, num_dimensions, min_bound, max_bound, sphere_function)
best_position = pso.optimize()
print("Best Position:", best_position)
print("Best Fitness:", sphere_function(best_position))


# В этом примере реализован класс Particle, представляющий частицу,
# которая хранит свою позицию, скорость и лучшую позицию, которую
# она обнаружила. Затем создается класс PSO, который содержит логику
# оптимизации роя частиц. Он принимает на вход параметры, такие как
# количество частиц, размерность пространства, границы значений, функцию
# приспособленности, максимальное количество итераций и веса в формуле обновления частиц.

# Главная функция optimize выполняет итерации оптимизации,
# обновляя положение и скорость каждой частицы на основе формул PSO,
# а также сохраняет лучшую позицию как для каждой частицы, так и для роя в целом.
# Затем она возвращает лучшую позицию, найденную в результате оптимизации.

# В данном примере также предоставляется пример использования функции
# пригодности в виде sphere_function, которая вычисляет сумму квадратов
# всех значений вектора. Вы можете заменить эту функцию на свою собственную,
# соответствующую вашей задаче.

# После завершения оптимизации выводятся лучшая позиция
# и соответствующая ей функция пригодности.