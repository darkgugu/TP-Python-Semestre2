import os

def lancer_exercice(ex, fichier):
    chemin = f"./{ex}/{fichier}"
    print(f"Exécution de : {chemin}")
    os.system(f"python {chemin}")

def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Exercice 1 - Recherche et Parcours de Graphes")
        print("2. Exercice 2 - Dijkstra")
        print("3. Exercice 3 - Bellman-Ford")
        print("4. Exercice 4 - Algorithme de Flot (Ford-Fulkerson / Edmonds-Karp)")
        print("5. Exercice 5 - Tri Rapide Randomisé")
        print("6. Exercice 6 - Arbres AVL")
        print("7. Exercice 7 - Problèmes NP-complets et NP-difficiles")
        print("0. Quitter")
        
        choix = input("Choisissez un exercice (0-7) : ")

        if choix == "1":
            lancer_exercice("Ex1", "Code.py")
        elif choix == "2":
            lancer_exercice("Ex2", "dijkstra.py")
        elif choix == "3":
            lancer_exercice("Ex3", "Code.py")
        elif choix == "4":
            print("\n--- Exercice 4 ---")
            print("1. Edmonds-Karp")
            print("2. Ford-Fulkerson")
            sous_choix = input("Choisissez l'algorithme (1 ou 2) : ")
            if sous_choix == "1":
                lancer_exercice("Ex4", "edmonds-karp.py")
            elif sous_choix == "2":
                lancer_exercice("Ex4", "ford-fulkerson.py")
            else:
                print("Choix invalide.")
        elif choix == "5":
            lancer_exercice("Ex5", "Code.py")
        elif choix == "6":
            lancer_exercice("Ex6", "arbres-avl.py")
        elif choix == "7":
            print("\n--- Exercice 7 ---")
            print("1. Code principal")
            print("2. Code TSP")
            sous_choix = input("Choisissez le fichier à exécuter (1 ou 2) : ")
            if sous_choix == "1":
                lancer_exercice("Ex7", "Code.py")
            elif sous_choix == "2":
                lancer_exercice("Ex7", "Code_TSP.py")
            else:
                print("Choix invalide.")
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()
