

def enzyme_cut(seq,cut):
    for i in seq.strip():
        if i not in ('A','T','C','G'): 
            print('The target sequence is incorrect')
            exit()
            
    for j in cut.strip():
        if j not in ('A','T','C','G'):
            print('The recognition sequence is incorrect')
            exit()
            
    position_list = []
    
    L = len(seq)
    for i in range(L-3):
        if seq[i:i+4] == cut:
            position_list.append(i)
    return position_list
            

a = str(input('Please enter the target sequence')).strip()
b = str(input('Please choose the four digit indentical sequence')).strip()

if enzyme_cut(a,b) is not None:
    print(f'The begining position of the recognition sequence is(are) {enzyme_cut(a,b)}')
else: 
    print('Error exists, please check again')

