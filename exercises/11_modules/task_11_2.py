ff = ['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt']#, 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']
for i in ff:
     ...:     with open(i) as f:
     ...:         sh = f.read().rstrip()
     ...:         shh.append(sh.lstrip().split('\n'))
     
res = {}

for item in shh:
    for i in item:
        if i.startswith('SW1>'):
            k = [i[0:3]]
        elif i.startswith('R1>'):
            k = [i[0:2]]
        elif 'Eth' in i:
            rem_dev,local_i,local_p,*rest,rem_i,rem_p = i.split()
            k.append(local_i+local_p)
            v = (rem_dev, rem_i + rem_p)
            res[tuple(k)]= (v)
            k.pop(-1)
