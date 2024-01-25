import random

# Создание графа
graph = [[0, 2, 5, 7],
         [2, 0, 8, 3],
         [5, 8, 0, 1],
         [7, 3, 1, 0]]

# Параметры муравьиного алгоритма
alpha = 1  # Влияние феромонов
beta = 2  # Влияние видимости
evaporation = 0.5  # Скорость испарения феромона
q = 100  # Количество феромона, оставляемое муравьем

# Количество итераций
iterations = 10

# Количество муравьев
ants = 5

# Количество вершин в графе
num_vertices = len(graph)

# Инициализация феромонов на ребрах
pheromone = [[1 for _ in range(num_vertices)] for _ in range(num_vertices)]


# Функция выбора следующей вершины
def select_next_vertex(current_vertex, available_vertices):
    probabilities = []

    # Рассчитываем вероятности перехода к доступным вершинам
    for vertex in available_vertices:
        pheromone_amount = pheromone[current_vertex][vertex]
        visibility = 1 / graph[current_vertex][vertex]
        probability = pheromone_amount ** alpha * visibility ** beta
        probabilities.append((vertex, probability))

    # Выбираем следующую вершину на основе вероятностей
    total_probability = sum(probability for _, probability in probabilities)
    probabilities = [
        (vertex, probability / total_probability)
        for vertex, probability in probabilities
    ]

    # Случайный выбор следующей вершины на основе вероятностей
    r = random.random()
    cumulative_probability = 0
    for vertex, probability in probabilities:
        cumulative_probability += probability
        if r <= cumulative_probability:
            return vertex


# Находим оптимальный маршрут при помощи муравьиного алгоритма
best_distance = float('inf')
best_route = []

for _ in range(iterations):
    for ant in range(ants):
        current_vertex = random.randint(0, num_vertices - 1)  # Случайный выбор начальной вершины
        unvisited_vertices = set(range(num_vertices)) - {current_vertex}
        visited_vertices = [current_vertex]
        distance = 0

        while unvisited_vertices:
            next_vertex = select_next_vertex(current_vertex, unvisited_vertices)
            visited_vertices.append(next_vertex)
            unvisited_vertices.remove(next_vertex)
            distance += graph[current_vertex][next_vertex]
            current_vertex = next_vertex

        distance += graph[visited_vertices[-1]][visited_vertices[0]]  # Добавляем расстояние от последней до первой вершины

        # Если найден новый оптимальный маршрут, обновляем переменные
        if distance < best_distance:
            best_distance = distance
            best_route = visited_vertices

    # Обновление феромонов на ребрах
    for i in range(num_vertices):
        for j in range(num_vertices):
            pheromone[i][j] *= evaporation  # Испарение феромона
            if i in best_route and j in best_route:
                pheromone[i][j] += q / best_distance  # Оставляем феромон на оптимальном маршруте

# Вывод результатов
print("Оптимальный маршрут:", best_route)
print("Длина оптимального маршрута:", best_distance)

# В этом примере рассматривается задача обхода всех вершин в полном графе
# с положительными весами ребер. Алгоритм случайным образом выбирает начальную
# вершину и пошагово перемещается от одной вершины к другой, выбирая следующую
# вершину на основе влияния феромонов и видимости. После прохождения всех
# муравьев выполняется обновление феромонов на ребрах,
# учитывая найденное оптимальное решение.
