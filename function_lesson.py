def ratio(x, y):
    """ This is to take the ratio of x to y """
    return x/y

def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """Simpler programe that Deep Throught's, I bet."""
    return 42

def think_too_much():
    """ Express Caesar's skepticism about Cassius."""
    print("""sth""")

def complement_base(base, material= 'DNA'):
    """ compute reverse complement of a nucleic acid seq. """
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RuntimeError
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq, material= 'DNA'):
    """ return the complelement sequence. """
    # initilize empty string
    rev_com = ''
    for base in reversed(seq):
        rev_com += complement_base(base, material = material)
    return rev_com
