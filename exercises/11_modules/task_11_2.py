#!/usr/bin/env python3
from draw_network_graph import draw_topology

ff = ['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt']

res = {}

output_from_files = []

def create_network_map(filenames):
    for item in ff:
        with open(item) as f:
            sh = f.read().rstrip()
            output_from_files.append(sh.lstrip().split('\n'))

    for item in output_from_files:
        for i in item:
            if i.startswith('SW1>'):
                k = [i[0:3]]
            elif i.startswith('R1>'):
                k = [i[0:2]]
            elif i.startswith('R2>'):
                k = [i[0:2]]
            elif i.startswith('R3>'):
                k = [i[0:2]]
            elif 'Eth' in i:
                rem_dev,local_i,local_p,*rest,rem_i,rem_p = i.split()
                k.append(local_i+local_p)
                v = (rem_dev, rem_i + rem_p)
                if v not in res:                    #если нет значения в словаре, тогда добавляем вывод в словарь
                    res[tuple(k)]= (v)
                k.pop(-1)
    return res

draw_topology(res)
