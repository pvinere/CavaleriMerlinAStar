import heapq

# 24. Problema cavalerilor. La curtea regelui Arthur s-au adunat n cavaleri. Fiecare dintre
# ei are printre cei prezenţi cel puţin un duşman. Verificaţi dacă Merlin, consilierul
# regelui, poate să îi aşeze pe cavaleri la o masă rotundă astfel încât nici unul dintre ei
# să nu fie alături de vreun duşman al său.
# Rezolvaţi problema folosind strategia de căutare A*.

# Constructor n - nr. Cavaleri, enemies - dictionar ce contine dusmanii fiecarui cavaler
class KnightProblem:
    def __init__(self, n, enemies):
        self.n = n
        self.enemies = enemies


#Verificare solutie valida - primeste o lista solution - pt fiecare cavaler din lista se verifica
#daca are dusman in stanga si dreapta

    def is_valid_solution(self, solution):
        for i in range(self.n):
            if solution[i] in self.enemies[solution[(i - 1) % self.n]] or solution[i] in self.enemies[solution[(i + 1) % self.n]]:
                return False
        return True

#Primeste o permutare a cavalerilor si calculeaza o euristica simpla bazata pe nr de cavaleri care sunt langa un dusman
#Cu cat h este mai mic cu atat solutia este considerata mai buna
    def heuristic(self, solution):
        h = 0
        for i in range(self.n):
            if solution[i] in self.enemies[solution[(i - 1) % self.n]] or solution[i] in self.enemies[solution[(i + 1) % self.n]]:
                h += 1
        return h

#Metoda A*
    def a_star_search(self):
        # Initializare starea initiala, lista deschisa, multime inchisa
        start_state = tuple(range(self.n))
        open_list = [(self.heuristic(start_state), start_state)]
        closed_set = set()

        # Cat timp ce lista deschisa nu este goala,se extrage starea cu cel mai mic cost estimat.
        while open_list:
            _, state = heapq.heappop(open_list)

            # Daca state este o solutie vaida, aceasta este returnata
            if self.is_valid_solution(state):
                return state

            # Altfel, state este adaugata in multimea inchisa
            closed_set.add(state)


            neighbors = self.get_neighbors(state)

            # Vecini sunt generati si adaugati in lista deschisa daca nu se afla in multimea inchisa
            for neighbor in neighbors:
                if neighbor not in closed_set:
                    heapq.heappush(open_list, (self.heuristic(neighbor) + len(state), neighbor))

        return None

    #get_neighbors - primeste o permutare a cavalerilor si returneaza toti vecinii acestei permutari
    def get_neighbors(self, state):
        neighbors = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Obtinut prin interschimbarea pozitiilor a doi cavaleri in permutare
                neighbor = list(state)
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(tuple(neighbor))
        return neighbors

# NEVALID - NU SE POT ASEZA
# n = 4
# enemies = {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0, 3],
#     3: [1, 2]
# }

# VALID 5 CAVALERI
n = 5
enemies = {
    0: [2],
    1: [2, 3],
    2: [0, 1],
    3: [1, 4],
    4: [3]
}



# VALID 6 cavaleri
# Exemplu de utilizare
# n = 6
# enemies = {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0, 4],
#     3: [1, 5],
#     4: [2, 5],
#     5: [3, 4]
# }

# VALID 10 cavaleri
# n = 10
# enemies = {
#     0: [1, 2, 3],
#     1: [0, 4, 5],
#     2: [0, 6, 7],
#     3: [0, 8, 9],
#     4: [1, 8, 9],
#     5: [1, 6, 9],
#     6: [2, 5, 8],
#     7: [2, 4, 9],
#     8: [3, 4, 6],
#     9: [3, 5, 7]
# }

knight_problem = KnightProblem(n, enemies)
solution = knight_problem.a_star_search()

if solution:
    print("O soluție posibilă este:", solution)
else:
    print("Nu există soluție pentru această configurație.")

