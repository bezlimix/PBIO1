import random
import re

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
    length = int(input("Podaj długość sekwencji: "))
    seq_id = input("Podaj ID sekwencji: ").strip()
    description = input("Podaj opis sekwencji: ").strip()
    name = input("Podaj imię: ").strip()

    # Generowanie i modyfikacja sekwencji
    dna = generate_dna_sequence(length)
    dna_with_name = insert_name(dna, name)

    # Zapis do pliku FASTA
    filename = f"{seq_id}.fasta"
    with open(filename, 'w') as fasta_file:
        fasta_file.write(f">{seq_id} {description}\n")
        fasta_file.write(dna_with_name + '\n')

    print(f"\nSekwencja została zapisana do pliku {filename}")
    calculate_statistics(dna_with_name, name)

if __name__ == "__main__":
    main()

