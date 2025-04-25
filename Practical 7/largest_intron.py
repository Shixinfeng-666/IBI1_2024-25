# define the sequence to be detected
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
# obatain the basic condition of length
len = len(seq)

largest_L = 0   # define the variable: the length of the largest intron
for i in range(len):
    if seq[i] == 'G' and seq[i+1] == 'T': # find every splice-donor GT dinucleotide
        for j in range(i+2,len-2):
            if seq[j] == 'A' and seq[j+1] == 'G': # find every splice-acceptor AG nucleotide
                now_L = j-i+2 # calculate the value of largest length
                if now_L > largest_L: 
                    largest_L = now_L  # keep the largest value as the result only, replace the smaller one
# output the result
print(f'The length of largest intron in the provided sequence is {largest_L}') 
                
              