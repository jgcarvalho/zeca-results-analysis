from glob import glob
from os.path import basename
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns


ROOT_DIR = "/home/jgcarvalho/zeca-analyse-pos_quali/Top8000-best_hom50_pdb_chain/"
SEQ_DIR = ROOT_DIR + "data/seq/"

OUTSTATS_DIR = "/rose_special_charged/run_10000/outstats/"
# CBA_DIR = ROOT_DIR + "cba/rose_special_charged/run_10000/outstats/"
# MCC_DIR = ROOT_DIR + "mcc/rose_special_charged/run_10000/outstats/"
# CE_DIR = ROOT_DIR + "cross_entropy/rose_special_charged/run_10000/outstats/"
# CBA_MCC_DIR = ROOT_DIR + "cba_plus_mcc/rose_special_charged/run_10000/outstats/"
# CBAxMCC_DIR = ROOT_DIR + "cba_times_mcc/rose_special_charged/run_10000/outstats/"
# CBA2xMCC_DIR = ROOT_DIR + "cba2_times_mcc/rose_special_charged/run_10000/outstats/"

def get_q3(fn, func_fit):
    with open(ROOT_DIR+func_fit+OUTSTATS_DIR+fn) as f:
        for l in f.readlines():
            if l[:2] == "Qe":
                return float(l[4:])


def box_plot(q3_cba, q3_mcc, q3_ce):
    m = ['CBA','MCC','CE']
    x = np.array(list(m))
    plt.figure(1)
    plt.subplot()
    sns.boxplot(data=[np.array(q3_cba),np.array(q3_mcc),np.array(q3_ce)], palette="muted", showfliers=False)
    plt.ylim(ymin=0, ymax=100)
    # plt.xticks(x, labels)
    # plt.savefig("atribuicao_len_ss_H.svg")
    plt.show()

def only(list_name):
    q3_cba = []
    q3_mcc = []
    q3_ce = []
    q3_cew = []
    q3_cba_mcc = []
    q3_cbaxmcc = []
    q3_cba2xmcc = []

    with open(list_name) as f:
        for fn in f.readlines():
            fn = fn.strip()
            q3_cba.append(get_q3(fn,'cba'))
            q3_mcc.append(get_q3(fn,'mcc'))
            q3_ce.append(get_q3(fn,'cross_entropy'))
            q3_cew.append(get_q3(fn,'cross_entropy_weighted'))
            q3_cba_mcc.append(get_q3(fn,'cba_plus_mcc'))
            q3_cbaxmcc.append(get_q3(fn,'cba_times_mcc'))
            q3_cba2xmcc.append(get_q3(fn,'cba2_times_mcc'))
    print(q3_cba)
    box_plot(q3_cba, q3_mcc, q3_ce)
    box_plot(q3_cba, q3_ce, q3_cew)
    box_plot(q3_cba_mcc, q3_cbaxmcc, q3_cba2xmcc)

def all():
    q3_cba = []
    q3_mcc = []
    q3_ce = []
    q3_cew = []
    q3_cba_mcc = []
    q3_cbaxmcc = []
    q3_cba2xmcc = []
    for fn in glob(SEQ_DIR+"*"):
        fn = basename(fn)
        print(fn)
        q3_cba.append(get_q3(fn,'cba'))
        q3_mcc.append(get_q3(fn,'mcc'))
        q3_ce.append(get_q3(fn,'cross_entropy'))
        q3_cew.append(get_q3(fn,'cross_entropy_weighted'))
        q3_cba_mcc.append(get_q3(fn,'cba_plus_mcc'))
        q3_cbaxmcc.append(get_q3(fn,'cba_times_mcc'))
        q3_cba2xmcc.append(get_q3(fn,'cba2_times_mcc'))
    print(q3_cba)
    box_plot(q3_cba, q3_mcc, q3_ce)
    box_plot(q3_cba, q3_ce, q3_cew)
    box_plot(q3_cba_mcc, q3_cbaxmcc, q3_cba2xmcc)

def main():
    # all()
    only("./list_seq_first_5000")
    only("./list_seq_last_1700")


if __name__ == '__main__':
    main()