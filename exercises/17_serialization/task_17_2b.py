'''
for item in files:
    with open(item) as f:
        for line in f:
            m = re.search(regex,line)
            if m:
                loc_d = m.group(1)
            m01 = re.search(regex01,line)
            if m01:
                rem_d,loc_p,rem_p = m01.groups()
                v=(rem_d,rem_p)
                if v not in d:
                    d[loc_d,loc_p]=v
with open('topology.yaml','w') as f:
    temp = yaml.dump(d,f)
    '''
