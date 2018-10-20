import csv

def writeCsv(filename, res):
    outfile = open(filename, 'a', newline='')
    wCSV = csv.writer(outfile)
    wCSV.writerow(res)
    outfile.close()

def ansComp(ansFile, inFile):
    with open(ansFile) as f:
        ans_cor = f.read().splitlines()
    with open(inFile) as f:
        ans_stu = f.read().splitlines()

    res = []
    right = 0
    for i in range(0, len(ans_cor)):
        if ans_stu[i] == ans_cor[i]:
            res.append(1)
            right += 1
        else:
            res.append(0)
    print(right,'/',len(ans_cor))
    print(res)

    return res

res = ansComp('ans_2.txt', '8787.txt')
writeCsv('../result/result_1.csv', res)
