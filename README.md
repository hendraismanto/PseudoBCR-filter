# MIXCR Output to Repertoire Builder Input

Get the filtered full length BCR sequence.
Sequences are filtered by 100% CDRs similarity.

## Getting Started

### Dependencies

```
Pyhton 3.7 and above
- biopython=1.78
- cd-hit=4.8.1
- python=3.7.3
- abnumber=0.2.3
- hmmer=3.3.2
```

### Usage

* Install miniconda3
    * `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh`
    * `sh Miniconda3-latest-MacOSX-x86_64.sh`
* Install conda dependencies
    * Install: `conda env create -f dependencies.miniconda3.yml`
    * Switch to environment: `conda activate pseudo-filter`

```
python pseudo-cdr-sim-filter_BCR.py [-h] [-hc INPUT_H] [-lc INPUT_L]

optional arguments:
  -h, --help  show this help message and exit
  -hc INPUT_H Inputfile for heavy chain (in FASTA format)
  -lc INPUT_L Inputfile for light chain (in FASTA format)
  ```
  
  ## Author
  
  * **Hendra Saputra Ismanto** 
# PseudoBCR-filter
