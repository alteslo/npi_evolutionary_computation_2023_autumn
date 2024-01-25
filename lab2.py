import math
import random


class AntColony:
    def __init__(self, num_ants, alpha, beta, evaporation, max_iterations) -> None:
        self.num_ants = num_ants

        self.alpha = alpha  # Коэффициент влияния феромона
        self.beta = beta  # Коэффициент влияния привлекательности города
        self.evaporation = evaporation  # Коэффициент испарения феромона
        self.max_iterations = max_iterations  # Максимальное количество итераций

    def add_cities_to_run(self, cities):
        self.cities = cities
        self.num_cities = len(cities)
        self.pheromone = [[1] * self.num_cities for _ in range(self.num_cities)]  # Коэффициент феромона

    def _distance(self, city1, city2):
        """Функция расчета расстояния между городами"""
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def _choose_next_city(self, current_city, visited_cities):
        """Функция выбора следующего города для перемещения муравья"""

        attractiveness = []

        for city in range(self.num_cities):
            if city not in visited_cities:
                pheromone_level = self.pheromone[current_city][city]
                dist = self._distance(current_city, city)
                attractiveness.append(
                    (city, (pheromone_level ** self.alpha) * ((1 / dist) ** self.beta))
                )

        total = sum(attr[1] for attr in attractiveness)
        probabilities = [(attr[0], attr[1] / total) for attr in attractiveness]

        next_city = random.choices([city[0] for city in probabilities], [
                                city[1] for city in probabilities])[0]
        return next_city

    def _update_pheromone(self, trails):
        """Функция обновления феромона после завершения итерации"""
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                self.pheromone[i][j] *= (1 - self.evaporation)
                for trail in trails:
                    length = trail["length"]
                    self.pheromone[i][j] += (1.0 / length)

    def ants_run(self,):
        """Муравьиный алгоритм"""

        best_tour = None
        best_length = float("inf")

        for iteration in range(self.max_iterations):
            ant_tours = []

            for ant in range(self.num_ants):
                visited = [0]  # Начинаем каждый тур с города 0
                tour_length = 0.0

                for _ in range(self.num_cities - 1):
                    current_city = visited[-1]
                    next_city = self._choose_next_city(current_city, visited)
                    visited.append(next_city)
                    tour_length += self._distance(current_city, next_city)

                tour_length += self._distance(visited[-1], 0)  # Замыкаем тур

                if tour_length < best_length:
                    best_length = tour_length
                    best_tour = visited

                ant_tours.append({"tour": visited, "length": tour_length})

            self._update_pheromone(ant_tours)

        return best_tour, best_length


num_cities = 5  # Количество городов
num_ants = 10  # Количество муравьев в колонии

# Координаты городов
cities = {
    0: (2, 3),
    1: (4, 1),
    2: (5, 3),
    3: (6, 6),
    4: (8, 2)
}
alpha = 1.5  # Коэффициент влияния феромона
beta = 2.5  # Коэффициент влияния привлекательности города
evaporation = 0.1  # Коэффициент испарения феромона
max_iterations = 100  # Максимальное количество итераций

if __name__ == "__main__":

    # Запуск муравьиного алгоритма
    colony = AntColony(num_ants, alpha, beta, evaporation, max_iterations)
    colony.add_cities_to_run(cities)
    best_tour, best_length = colony.ants_run()

    # Печать лучшего найденного пути и его длины
    print("Лучший найденный путь:", best_tour)
    print("Длина лучшего пути:", best_length)


# Это пример муравьиного алгоритма для решения задачи коммивояжера.
# В данном примере представлены пять городов с координатами, заданное
# количество муравьев и другие параметры алгоритма.
# Функция distance вычисляет расстояние между городами,
# а функции choose_next_city и update_pheromone определяют выбор следующего города
# и обновление феромона соответственно.
# Алгоритм выполняется с помощью функции ant_colony_optimization, которая запускает итерации и обновляет феромон
# на основе длин маршрутов, приобретенных муравьями. В конце выполнения алгоритма выводится лучший найденный путь и его длина.
