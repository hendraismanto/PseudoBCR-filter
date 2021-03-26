from Bio import SeqIO
from abnumber import Chain
import subprocess
import sys
import os
import time
import argparse
import logging

def filter_data(input_H, filename_only_H, input_L, filename_only_L, sim, memory, core):
    # make fasta file of pseudo cdrs from heavy chain
    # dict for heavy chain full length
    print('---------- Making pseudo CDRs ----------')
    
    full_H = {}
    with open(filename_only_H + '_pseudo-cdr.fa', 'w') as f:
        for seq_record in SeqIO.parse(input_H, 'fasta'):
            seq = str(seq_record.seq)
            name = str(seq_record.name)
            full_H[name] = seq
            chain = Chain(seq, scheme='imgt')
            cdr = str(chain.cdr1_seq) + str(chain.cdr2_seq) + str(chain.cdr3_seq)

            f.write('>' + name + '\n' + cdr + '\n')

    # dict for light chain full length
    full_L = {}
    for seq_record in SeqIO.parse(input_L, 'fasta'):
            seq = str(seq_record.seq)
            name = str(seq_record.name)
            full_L[name] = seq
            
    print('----------- Running CD-hit ----------')

    # run cd-hit
    subprocess.call(['cd-hit', '-i', filename_only_H + '_pseudo-cdr.fa',  '-o', filename_only_H,  '-c', sim, '-M', memory, '-T', core, '-bak', '1', '-d', '100'])

    print('----------- Making full length FASTA ---------- ')
    # get full sequences of cd-hit cluster
    with open(filename_only_H + 'H_cdhit-filtered.fa', 'w') as f:
        for seq_record in SeqIO.parse(filename_only_H, 'fasta'):
                name = str(seq_record.name)
                f.write('>' + name + '\n' + full_H[name] + '\n')

    with open(filename_only_L + 'L_cdhit-filtered.fa', 'w') as f:
        for seq_record in SeqIO.parse(filename_only_H, 'fasta'):
                name = str(seq_record.name)
                f.write('>' + name + '\n' + full_L[name] + '\n')
            
def main():

    parser = argparse.ArgumentParser(description = 'Filter pseudo(cdr) BCR sequences using cd-hit and output filtered full length BCR sequences in FASTA')

    parser.add_argument('-hc', dest = 'input_H', help = 'Heavy chain (fasta)')
    parser.add_argument('-lc', dest = 'input_L', help = 'Light chain (fasta)')
    #parser.add_argument('-o', dest = 'out_dir', help = 'directory of output')
    args = parser.parse_args()
    
    #os.makedirs(args.out_dir, exist_ok=True)

    filename_H = os.path.abspath(args.input_H)
    filename_H_ = os.path.basename(filename_H)
    filename_only_H, file_extension_H = os.path.splitext(filename_H_)
    
    filename_L = os.path.abspath(args.input_L)
    filename_L_ = os.path.basename(filename_L)
    filename_only_L, file_extension_L = os.path.splitext(filename_L_)
    

    #logging.basicConfig(filename=os.path.join(args.out_dir, "out.log"), level=logging.INFO)
    #logger = logging.getLogger()
    #sh = logging.StreamHandler()
    #logger.addHandler(sh)
    
    #logging.info("heavy chain: {}".format(args.input_H))
    #logging.info('light chain: {}'.format(args.input_L))
    #logging.info("out_dir: {}".format(os.path.abspath(args.out_dir)))
    
    filter_data(args.input_H, filename_only_H, args.input_L, filename_only_L, '1', '4000', '4')
    
if __name__ == '__main__':
    start_time = time.time()
    main()

    print(("Done. Total run time: %s seconds" %(time.time() - start_time)))
