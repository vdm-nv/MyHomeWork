#!/usr/bin/env python3

with open('ospf.txt') as f:
         for line in f:
             l = line.rstrip().replace(',','')
             li = l.replace('[', '')
             lin = li.replace(']', '')
             lino = lin.replace('O','OSPF')
             linov = lino.replace('via', '')
             linovo = linov.split()
             d_keys = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:','Outbound Interface:']
             print('{:<25}{:<20}'.format(d_keys[0],linovo[0]),
             '\n'+'{:<25}{:<20}'.format(d_keys[1],linovo[1]),
             '\n'+'{:<25}{:<20}'.format(d_keys[2],linovo[2]),
             '\n'+'{:<25}{:<20}'.format(d_keys[3],linovo[3]),
             '\n'+'{:<25}{:<20}'.format(d_keys[4],linovo[4]),
             '\n'+'{:<25}{:<20}'.format(d_keys[-1],linovo[-1]),
             '\n'+'-'*40)
