# _*_ coding:utf-8 _*_
import os
import time
from multiprocessing import Pool
from rapidfuzz import fuzz

str2 = []
with open('data.txt', 'r', encoding="utf-8") as f:##資料庫的品名
    for line in f:
        str2.append(line.strip('\n'))

def myFunc(j):

    #print(j)
    x = []
    x.append(max(str2, key=lambda a: fuzz.ratio(a, j)))##需要改的品名去比對資料庫品名 看哪個相似度最高
    print(x)
    return x#返回list最像的資料庫的品名



if __name__ == '__main__':
    arr = []
    with open('品名.txt', 'r', encoding="utf-8") as f:#將需要改的品名
        for line in f:
            arr.append(line.strip('\n'))
    pool = Pool(os.cpu_count()-1)#使用CPU最大數-1
    stat = time.time()
    results = pool.map(myFunc, arr)#傳入需要改的品名去跟資料庫裡的品名做比對
    print(time.time()-stat)
    print(results)

    pool.close()
    pool.join()