# Cavaleri Merlin AStar
Problema Cavalerilor AStar

### Cerinta proiect:

24. Problema cavalerilor. La curtea regelui Arthur s-au adunat n cavaleri. Fiecare dintre
ei are printre cei prezenţi cel puţin un duşman. Verificaţi dacă Merlin, consilierul
regelui, poate să îi aşeze pe cavaleri la o masă rotundă astfel încât nici unul dintre ei
să nu fie alături de vreun duşman al său.
Rezolvaţi problema folosind strategia de căutare A*.

### Informatii:

Proiectul a fost realizat in limbajul de programare Python unde au fost importate modulele: <br/>
heapq - modul pentru algoritmul ,,heap queue sau priority queue" <br/>
tkinter - pentru interfata UI <br/>

### Fundamente teoretice despre proiect:

Pentru a rezolva problema acestui proiect se urmaresc acesti pasi : <br/>
1. Se primeste un set de date (n - nr cavaleri, enemies- dictionar cu dusmanii fiecarui cavaler). <br/>
```
class KnightProblem:
    def __init__(self, n, enemies):
        self.n = n
        self.enemies = enemies
```
2. Se verifica daca fiecare cavaler are dusman in stanga si dreapta sa. <br/>
```
if solution[i] in self.enemies[solution[(i - 1) % self.n]] or solution[i] in self.enemies[solution[(i + 1) % self.n]]:
    return False
```
3. Se foloseste calculul euristic pentru a afla solutia cea mai bine (h-ul cat mai mic). <br/>
   Aceasta este bazata pe nr de cavaleri care sunt langa un dusman. <br/>
```
if solution[i] in self.enemies[solution[(i - 1) % self.n]] or solution[i] in self.enemies[solution[(i + 1) % self.n]]:
    h += 1
```
4. Se foloseste agloritmul de cautare A* <br/>
   Acest are urmatorii pasi pentru acest proiect: <br/>
       - se initalizeaza starea initiala, lista deschisa si multimea inchisa: <br/>
       ```
       start_state = tuple(range(self.n))
       open_list = [(self.heuristic(start_state), start_state)]
       closed_set = set()
       ```
       - se extrage starea cu cel mai mic cost estimat <br/>
       ```
       while open_list:
       _, state = heapq.heappop(open_list)
       ```
       - daca starea(state) este o solutie valida aceasta este returnata <br/>
       ```
       if self.is_valid_solution(state):
           return state
       ```
       - daca nu starea(state) este adaugata in multimea inchisa <br/>
       ```
       closed_set.add(state)
       ```



### Structura Proiect:

Proiectul este structurat intr-un singur fisier Main.py si 4 fisiere text care contin diferite teste. <br/>

### Testele realizate pentru proiect:
Sunt existente 4 teste cu cate 4,5,6,10 cavaleri. <br/>
Teste cu 5,6,10 cavaleri sunt valide si exista o asezare corecta iar ce cu 4 este nevalid. <br/>
Mai jos este o reprezentare a cum arata datele care se introduc in aplicatie:
```
6
0:1,2
1:0,3
2:0,4
3:1,5
4:2,5
5:3,4
```








