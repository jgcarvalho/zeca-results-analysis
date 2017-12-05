from glob import glob 
import os

CSV_PATH = "csv_results/"

PATH_SEQ = "seq/"
PATH_ALL3 = "all3/"
PATH_DSSP = "dssp/"
PATH_STRIDE = "stride/"
PATH_KAKSI = "kaksi/"
PATH_PROSS = "pross/"
PATH_PRED = "fasta_pred/"

def get(fn):
    with open(fn) as f:
        f.readline()
        return f.readline()

def csv(path, fn):
    seq = get(PATH_SEQ + fn)
    all3 = get(PATH_ALL3 + fn)
    dssp = get(PATH_DSSP + fn)
    stride = get(PATH_STRIDE + fn)
    kaksi = get(PATH_KAKSI + fn)
    pross = get(PATH_PROSS + fn)
    psipred = get(PATH_PRED + fn)

    with open(path+fn, 'w') as f:
        f.write("NUM,SEQ,ALL3,DSSP,STRIDE,KAKSI,PROSS,PRED\n")
        for i in range(len(seq)):
            f.write("{},{},{},{},{},{},{},{}\n".format(i, seq[i],all3[i],dssp[i],stride[i],kaksi[i], pross[i],psipred[i]))


def main():
    for fn in glob("./seq/*"):
        id = os.path.basename(fn)
        print(id)
        csv(CSV_PATH, id)


if __name__ == '__main__':
    main()