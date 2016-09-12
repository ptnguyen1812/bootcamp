codon = 'UAG'
stop_codon_ls = ['UAA', 'UAG', 'UGA']
stop_codon_tp = tuple(stop_codon_ls)
if codon == 'AUC':
    print ('This is the start codon')
elif codon in stop_codon_tp:
    print ('This is a stop codon')
else:
    print('This is just an amino acid codon')
