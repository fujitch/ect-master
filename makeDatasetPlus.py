# -*- coding: utf-8 -*-

import glob
import numpy as np
import random

dataset = {}

for coil in [1]:
    liftList = {}
    for lift in [1]:
        dataList = []
        for frequency in [400]:
            for width in ['0.001', '0.002', '0.005', '0.010', '0.020', '0.050', '0.100', '0.200', '0.500']:
                for depth in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if frequency == 25:
                        fpath = 'data/ID' + str(coil) + '/Sigs/sig_pz_d' + str(coil) + '_l' + str(lift) + '_f0' + str(frequency) + '_w' + width + '_d' + str(depth) + '_s*'
                    else:
                        fpath = 'data/ID' + str(coil) + '/Sigs/sig_pz_d' + str(coil) + '_l' + str(lift) + '_f' + str(frequency) + '_w' + width + '_d' + str(depth) + '_s*'
                    fnamelist = glob.glob(fpath)
                    for fname in fnamelist:
                        file = open(fname, 'rb')
                        data = np.zeros((99))
                        index = 6
                        for row in file:
                            row = str(row, encoding='utf-8', errors='replace')
                            strlist = row.split(" ")
                            for word in strlist:
                                if len(word) < 3:
                                    continue
                                data[index] = float(word)
                                index += 1
                        data[0] = float(width)
                        if depth == 1:
                            data[1] = float(0.2)
                        elif depth == 2:
                            data[1] = float(0.4)
                        elif depth == 3:
                            data[1] = float(0.6)
                        elif depth == 4:
                            data[1] = float(0.8)
                        elif depth == 5:
                            data[1] = float(1.0)
                        elif depth == 6:
                            data[1] = float(1.5)
                        elif depth == 7:
                            data[1] = float(2.0)
                        elif depth == 8:
                            data[1] = float(2.5)
                        elif depth == 9:
                            data[1] = float(3.0)
                        data[2] = float(coil)
                        data[3] = float(lift)
                        data[4] = float(frequency)
                        data[5] = float(fname[-5:])
                        dataList.append(data)
        liftList[lift] = dataList
    dataset[coil] = liftList
aaa = dataset[1][1]
for data in aaa:
    if data[0] == 0.001 and data[1] == 0.2 and data[5] == 0:
        for i in range(len(data)):
            if i > 6:
                data[i] = data[i] * (random.random() * 0.2 + 0.9)
        aaaa = np.reshape(data[6:], (31, 3))
        