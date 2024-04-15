# recursive_function
#
Funkcja rec_func przyjmuje listę list_ jako argument.

Inicjuje zmienną total_sum na wartość 0, która będzie przechowywać sumę wszystkich liczb.

Następnie iteruje przez elementy listy list_ za pomocą pętli for.

Dla każdego elementu sprawdza, czy jest on listą za pomocą funkcji isinstance(item, list). Jeśli tak, rekurencyjnie wywołuje funkcję rec_func dla tego zagnieżdżonego elementu i dodaje wynik do total_sum.

Jeśli element nie jest listą (czyli jest liczbą), dodaje go do total_sum.

Po zakończeniu iteracji zwraca całkowitą sumę.
