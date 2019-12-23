'''
regex = (r'\s(\S+\d)>.+\s{2}.+\s.+\s{2}.+\s'
         r'(\w\d) +(\w{3} \d\/\d) .+ (\w{3} \d\/\d)\s'
         r'(\w\d) +(\w{3} \d\/\d) .+ (\w{3} \d\/\d)\s'
         r'(\w\d) +(\w{3} \d\/\d) .+ (\w{3} \d\/\d)\s'
         r'(\w\d) +(\w{3} \d\/\d) .+ (\w{3} \d\/\d)\s')

res = re.search(regex, sh_cdp)
