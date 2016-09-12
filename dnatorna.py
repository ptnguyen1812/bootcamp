"""
convert DNA to RNA.
"""

def rna(seq):
    """
    convert DNA to RNA.
    """
    # convert to upper case
    seq = seq.upper()

    return seq.replace('T', 'U')
    
