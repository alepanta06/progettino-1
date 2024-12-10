# Inizializza la lista della spesa
lista_spesa = []

# Metodo per aggiungere un elemento alla lista
def aggiungi():
    elemento = input("Inserisci l'elemento da aggiungere: ")
    lista_spesa.append(elemento)
    print(f'"{elemento}" è stato aggiunto alla lista.')

# Metodo per visualizzare la lista
def visualizza():
    if not lista_spesa:
        print("La lista è vuota.")
    else:
        print("Ecco la tua lista della spesa:")
        for i, elemento in enumerate(lista_spesa, start=1):
            print(f"{i}. {elemento}")

# Metodo per rimuovere un elemento dalla lista
def rimuovi():
    visualizza()
    try:
        indice = int(input("Inserisci il numero dell'elemento da rimuovere: ")) - 1
        elemento_rimosso = lista_spesa.pop(indice)
        print(f'"{elemento_rimosso}" è stato rimosso dalla lista.')
    except (IndexError, ValueError):
        print("Indice non valido. Riprova.")

# Metodo per contare gli elementi nella lista
def conta():
    print(f"Ci sono {len(lista_spesa)} elementi nella lista.")

# Metodo per svuotare la lista
def svuota_lista():
    lista_spesa.clear()
    print("La lista è stata svuotata.")

# Menu principale
def menu():
    while True:
        print("\nMenu:")
        print("0. Esci")
        print("1. Aggiungi un elemento")
        print("2. Visualizza la lista")
        print("3. Rimuovi un elemento")
        print("4. Conta gli elementi")
        print("5. Svuota la lista")

        try:
            scelta = int(input("Scegli un'opzione: "))
        except ValueError:
            print("Inserisci un numero valido.")
            continue

        if scelta == 0:
            print("Grazie per aver usato il programma. Arrivederci!")
            break
        elif scelta == 1:
            aggiungi()
        elif scelta == 2:
            visualizza()
        elif scelta == 3:
            rimuovi()
        elif scelta == 4:
            conta()
        elif scelta == 5:
            svuota_lista()
        else:
            print("Opzione non valida. Riprova.")

# Avvia il menu
if __name__ == "__main__":
    menu()
