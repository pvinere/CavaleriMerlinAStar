import heapq
import tkinter as tk
from tkinter import messagebox

# 24. Problema cavalerilor. La curtea regelui Arthur s-au adunat n cavaleri. Fiecare dintre
# ei are printre cei prezenţi cel puţin un duşman. Verificaţi dacă Merlin, consilierul
# regelui, poate să îi aşeze pe cavaleri la o masă rotundă astfel încât nici unul dintre ei
# să nu fie alături de vreun duşman al său.
# Rezolvaţi problema folosind strategia de căutare A*.

# Constructor n - nr. Cavaleri, enemies - dictionar ce contine dusmanii fiecarui cavaler

filename = "date10cav.txt"

class KnightProblem:
    def __init__(self, n, enemies):
        self.n = n
        self.enemies = enemies


# Verificare solutie valida - primeste o lista solution - pt fiecare cavaler din lista se verifica
# daca are dusman in stanga si dreapta

    def is_valid_solution(self, solution):
        for i in range(self.n):
            if solution[i] in self.enemies[solution[(i - 1) % self.n]] or solution[i] in self.enemies[solution[(i + 1) % self.n]]:
                return False
        return True

# Primeste o permutare a cavalerilor si calculeaza o euristica simpla bazata pe nr de cavaleri care sunt langa un dusman
# Cu cat h este mai mic cu atat solutia este considerata mai buna
    def heuristic(self, solution):
        h = 0
        for i in range(self.n):
            if solution[i] in self.enemies[solution[(i - 1) % self.n]] or solution[i] in self.enemies[solution[(i + 1) % self.n]]:
                h += 1
        return h

# Metoda A*
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

    # get_neighbors - primeste o permutare a cavalerilor si returneaza toti vecinii acestei permutari
    def get_neighbors(self, state):
        neighbors = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Obtinut prin interschimbarea pozitiilor a doi cavaleri in permutare
                neighbor = list(state)
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(tuple(neighbor))
        return neighbors


def load_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Eliminare linii goale din fisier
    lines = [line.strip() for line in lines if line.strip()]

    # Verificare daca contine date valide
    if len(lines) == 0:
        print("Fisierul este gol sau nu contine date valide!")
        exit()

    n = int(lines[0])
    enemies = {}
    for line in lines[1:]:
        parts = line.strip().split(':')
        knight = int(parts[0])
        enemy_list = list(map(int, parts[1].split(',')))
        enemies[knight] = enemy_list

    return n, enemies



def solve_problem():
    fn = filename
    n, enemies = load_data_from_file(fn)

    if n is None or enemies is None:
        return

    knight_problem = KnightProblem(n, enemies)
    solution = knight_problem.a_star_search()

    if solution:
        messagebox.showinfo("Solutie gasita", f"O solutie posibila este: {solution}")
    else:
        messagebox.showinfo("Informatie", "Nu exista solutie pentru aceasta configuratie.")


def display_file_content():
    fn = filename
    with open(fn, 'r') as file:
        file_content = file.read()
    text_box.delete("1.0", "end")
    text_box.insert("1.0", file_content)


# Interfata grafica
root = tk.Tk()
root.title("Problema Cavalerilor")

# Butonul pentru rezolvarea problemei
solve_button = tk.Button(root, text="Rezolva problema", command=solve_problem)
solve_button.pack()

# Butonul pentru afisarea conținutului fisierului
display_button = tk.Button(root, text="Afiseaza continutul fisierului", command=display_file_content)
display_button.pack()

# Campul de text pentru afisarea continutului fisierului
text_box = tk.Text(root, height=10, width=50)
text_box.pack()

root.mainloop()

