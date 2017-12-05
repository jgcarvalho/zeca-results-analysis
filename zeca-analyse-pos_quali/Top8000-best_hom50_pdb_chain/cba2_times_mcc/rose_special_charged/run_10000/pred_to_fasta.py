from glob import glob
import os

OUT_PATH = "./fasta_pred/"

def get_fasta(fn):
    ss = ""
    with open(fn) as f:
        f.readline()
        for line in f.readlines():
            ss += line[2]
    # print(ss)
    return ss

def save_fasta(ss, fn):
    with open(fn, 'w') as f:
        f.write(">{} [ZECA]\n".format(os.path.basename(fn)))
        f.write(ss)

def main():
    for fn in glob("./outres/*"):
        print(fn)
        ss = get_fasta(fn)
        id = os.path.basename(fn)
        save_fasta(ss, OUT_PATH + id)

if __name__ == '__main__':
    main()