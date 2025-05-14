
from Bio.Align import substitution_matrices
from Bio.SeqIO import read

def read_sequence(filename):
    # read the sequence in each file
    with open(filename) as f:
        return str(read(f, "fasta").seq)

def calculate_alignment(seq1, seq2):
    
    # obtain BLOSUM62 matrixform BioPython
    matrix = substitution_matrices.load("BLOSUM62")
    
    total_score = 0
    identical = 0 # initialize the score and indentical percent
    
    for aa1, aa2 in zip(seq1, seq2):
        score = matrix.get((aa1, aa2), -4)  # unfault value 4 for absence
        total_score += score
        if aa1 == aa2:
            identical += 1
    
    percent_identity = (identical / len(seq1)) * 100
    return total_score, percent_identity

def main():
    # read the sequence
    human = read_sequence("human.fasta")
    mouse = read_sequence("mouse.fasta")
    random = read_sequence("random.fasta")
    
    # compare two sequences
    comparisons = [
        ("Human", "Mouse", human, mouse),
        ("Human", "Random", human, random),
        ("Mouse", "Random", mouse, random)
    ]
    
    for name1, name2, seq1, seq2 in comparisons:
            
        score, identity = calculate_alignment(seq1, seq2)
        print(f"{name1} vs {name2}:")
        print(f"BLOSUM62 Score: {score}")
        print(f"Percent Identity: {identity:.1f}%")

if __name__ == "__main__":
    main()