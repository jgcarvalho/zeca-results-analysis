from glob import glob 
import os

CSV_PATH = "csv_results/"

PATH_SEQ = "cba2_times_mcc/rose_special_charged/run_10000/seq/"
PATH_ALL3 = "cba2_times_mcc/rose_special_charged/run_10000/all3/"
PATH_DSSP = "cba2_times_mcc/rose_special_charged/run_10000/dssp/"
PATH_STRIDE = "cba2_times_mcc/rose_special_charged/run_10000/stride/"
PATH_KAKSI = "cba2_times_mcc/rose_special_charged/run_10000/kaksi/"
PATH_PROSS = "cba2_times_mcc/rose_special_charged/run_10000/pross/"
PATH_PSIPRED = "psipred/"

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
    psipred = get(PATH_PSIPRED + fn)

    with open(path+fn, 'w') as f:
        f.write("NUM,SEQ,ALL3,DSSP,STRIDE,KAKSI,PROSS,PSIPRED\n")
        for i in range(len(seq)):
            f.write("{},{},{},{},{},{},{},{}\n".format(i, seq[i],all3[i],dssp[i],stride[i],kaksi[i], pross[i],psipred[i]))


def main():
    for fn in glob("cba2_times_mcc/rose_special_charged/run_10000/seq/*"):
        id = os.path.basename(fn)
        print(id)
        csv(CSV_PATH, id)


if __name__ == '__main__':
    main()