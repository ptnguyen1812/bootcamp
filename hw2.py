#Ex2.3
def divide_block(seq, block_size):
    """
    take a block of seq and compute gc content.
    """
    seq = seq.lower()
    blocks = []
    i = 0
    # generate blocks
    for i in range(0, len(seq), block_size):
        blocks.append(seq[i : i + block_size])
    return blocks

def gc_blocks(seq, block_size):
    # compute GC content for each block
    blocks = divide_block(seq, block_size)
    gc_cont = []
    for sub in blocks:
        gc_perc = (sub.count('g') + sub.count('c'))/len(sub)
        gc_cont.append(gc_perc)

    return tuple(gc_cont)

def gc_map(seq, block_size, gc_thresh):
    """
    compare gc_cont each block to gc_threshold, highligh block above threshold.
    """
    blocks = divide_block(seq, block_size)
    gc_cont = gc_blocks(seq, block_size)
    above_thres = []
    for i in range(len(gc_cont)):
        if gc_cont[i] > gc_thresh:
            above_thres.append(blocks[i].upper())
        else:
            above_thres.append(blocks[i])
    return ''.join(above_thres)


    # Open file
    f = open('data/salmonella_spi1_region.fna', 'r')

    # Get all the lines
    lines = f.readlines()

    seq_gc = ''

    # Put the ATOM lines from chain A in new file
    for line in lines:
        if line[0] is '>':
            seq_gc += ''
        else:
            seq_gc += line.rstrip().lower()
    return seq_gc

    f_out = open('data/gc_samonella_spi1', 'w')
# Get all the lines
    f.seek(0)
    #line = f.readline()
    f_out.write(line)
    f_out.write(seq_gc)

    f.close()

# Ex. 2.4

def longest_orf (seq):
    """
    Find the longest orf.
    """
    #Compute the start codon indices
    start = []
    for i in range(len(seq)):
        if seq[i:i+3] == 'ATG':
            start.append(i)
    print (start)
    #return start

    # Compute the stop codon indices
    stop = []
    stop_codon = ('TAA', 'TGA', 'TAG')
    for j in range(len(seq)):
        if seq[j: j+3] in stop_codon:
            stop.append(j)
    print (stop)
    #return stop

    # the longest string
    orf_ls = []
    orf_len = []
    for i,numi in enumerate(start):
        for j, numj in enumerate(stop):
            if (numj - numi) % 3 == 0:
                orf_ls.append((numi,numj)
                orf_len.append(numj - numi)
    print(orf_ls)

    for i 
    return seq[]
