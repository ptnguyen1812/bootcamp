#Exc 1.1
#a) ls -F
# ls -G: label the folder
# ls -l: show the files with info of the files
# ls -lh:show the files with memory required to save the file
# ls -lS: show the files with ???
# ls -FGLh: show the folder with /

#c) ls / show some system file than can't be seen w/ ls

#Exc1.3

def reverse_comp1 (seq):
    """ return reverse complement of a sequence with a for loop, no reversed"""
    rev_com1 = ''
    for base in seq[::-1]:
        if base in 'Aa':
            rev_com1 += 'T'
        elif base in 'Tt':
            rev_com1 += 'A'
        elif base in 'Gg':
            rev_com1 += 'C'
        else:
            rev_com1 += 'G'
    return rev_com1

def reverse_comp2 (seq):
    """ return reverse complement with no loop. """

    rev_seq = seq[::-1].upper()
    rev_seq = seq.replace('A', 't')
    rev_seq = seq.replace('T', 'a')
    rev_seq = seq.replace('G', 'c')
    rev_seq = seq.replace('C', 'g')

    return (rev_seq.upper())

#Exc1.4.
def longest_common_str(str1, str2):
    """ Takes two sequences and returns the longest common substring."""
    common = []
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i: i+j] in str2:
                common.append(str1[i: i+j])
    return max(common, key = len)

#Exc1.5
def check_hair_pin(seq):
    """ take a RNA seq and check for hairpin. """
    if seq.count('(') == seq.count(')') and seq.count('...') >= 1:
        return True
    else:
        return False

def dotparen_to_bp(seq):
    """ converts the dot-parens notation to a tuple of 2-tuples representing the
    base pairs. """

    seq = list(seq)


    #pairs = []
    #for i in range(int(len(seq)/2)):
    #    if (seq[i] + seq[len(seq)-i-1]) is 'GC' or 'CG' or 'AU' or 'UA' or 'UG' or 'GU':
    #        pairs.append((seq[i], seq[len(seq)-i-1]))
    #    else:

    #print(tuple(pairs))
