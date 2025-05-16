import random
import re
import textwrap

def generate_dna_sequence(length):
    return ''.join(random.choices('ACGT', k=length))

def insert_name(sequence, name):
    position = random.randint(0, len(sequence))
    return sequence[:position] + name + sequence[position:]

def calculate_statistics(sequence, name):
    # Usuń imię z sekwencji (niezależnie od pozycji i liczby wystąpień)
    clean_sequence = sequence.replace(name, "")
    length = len(clean_sequence)

    stats = {nuc: clean_sequence.count(nuc) for nuc in 'ACGT'}

    print("\nStatystyki sekwencji:")
    for nuc in 'ACGT':
        percentage = (stats[nuc] / length) * 100
        print(f"{nuc}: {percentage:.1f}%")

    cg = stats['C'] + stats['G']
    at = stats['A'] + stats['T']
    cg_percent = (cg / length) * 100
    print(f"%CG: {cg_percent:.1f}")

def main():
    # Interakcja z użytkownikiem
    # Modyfikacja 1 – dodano walidację długości
    # ORIGINAL:
    # length = int(input("Podaj długość sekwencji: "))
    # MODIFIED (dodano obsługę błędnych danych oraz wymuszenie liczby > 0):
    while True:
        try:
            length = int(input("Podaj długość sekwencji: "))
            if length <= 0:
                print("Długość musi być większa od zera.")
                continue
            break
        except ValueError:
            print("Wprowadź poprawną liczbę całkowitą.")
    seq_id = input("Podaj ID sekwencji: ").strip()
    description = input("Podaj opis sekwencji: ").strip()
    #Modyfikacja 2 - walidacja imia
    # ORIGINAL:
    # name = input("Podaj imię: ").strip()
    # MODIFIED (dodano walidację, aby imię zawierało tylko litery):
    while True:
        name = input("Podaj imię: ").strip()
        if not name.isalpha():
            print("Imię może zawierać tylko litery. Spróbuj ponownie.")
        else:
            break

    # Generowanie i modyfikacja sekwencji
    dna = generate_dna_sequence(length)
    dna_with_name = insert_name(dna, name)

    # Zapis do pliku FASTA
    filename = f"{seq_id}.fasta"
    with open(filename, 'w') as fasta_file:
        fasta_file.write(f">{seq_id} {description}\n")
        # Modyfikacja 3 – formatowanie FASTA co 60 znaków
        # ORIGINAL:
        # fasta_file.write(dna_with_name + '\n')
        # MODIFIED (zapis sekwencji co 60 znaków, zgodnie ze standardem FASTA):
        wrapped_sequence = textwrap.fill(dna_with_name, width=60)
        fasta_file.write(wrapped_sequence + '\n')

    print(f"\nSekwencja została zapisana do pliku {filename}")
    calculate_statistics(dna_with_name, name)

if __name__ == "__main__":
    main()

