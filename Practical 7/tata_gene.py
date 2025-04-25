import re

def find_tata_genes(input_file, output_file):

    # input_file: the rout to input FASTA
    # output_file: the rout to output FASTA
    
    # introduce the regular expression
    tata_pattern = re.compile(r'TATA[AT]A[AT]')
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        
        current_name = None
        current_sequence = []
        
        for line in infile:
            line = line.strip()
            
            if line.startswith('>'):
                # deal with the current gene, detecting if there is a TATA box in it
                if current_name is not None:
                    full_sequence = ''.join(current_sequence) # merge the sequence as one str
                    if tata_pattern.search(full_sequence): # search TATA box in the whole sequence (str)
                       
                        gene_name = current_name.split()[0] # write down the selected gene name 
                        outfile.write(f"{gene_name}\n") # add the name of this gene included TATA box 
                        
                        # output in the from of FASTA file (80 words per line)
                        for i in range(0, len(full_sequence), 80):  # traverse the beginning of each line
                            outfile.write(f"{full_sequence[i:i+79]}\n") # add the sequence of selected gene in lines
                
                
                # begin to record a new gene
                current_name = line [0:8] # start the progress of a new gene in infile 
                current_sequence = []
            else:
                current_sequence.append(line) # keep appending lines to perform the whole sequence
        
        
if __name__ == "__main__":
    # bring in the real file names
    input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_fasta = "tata_genes.fa"
    
    # execute the function and out put the result
    find_tata_genes(input_fasta, output_fasta)
    print(f"Finish selection: {output_fasta}")