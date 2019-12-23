'''
for item in files:
    with open(item) as f:
        for line in f:
            if line.startswith('Cisco IOS Software,'):
                ios = re.search(r'Cisco IOS Software, .+ (\S+), RELEASE',line).group(1)
            elif line.startswith('router uptime is'):
                uptime = re.search(r'router uptime is (.*)',line).group(1)
            elif line.startswith('System image file is '):
                image = re.search(r'System image file is (.*)',line).group(1).strip('"')
                res = (ios,uptime,image)
                print(res)
	
re.search(r'.+, Version (\d+.\d\S+), (.+\s){7}.+ uptime is(( \d+ \w+,){2} \d+ \w+)\s.+\s.+ file is "(\S+:\S+\.\w+)"',sh_ver_r1).groups()

r1,r2,r3 = '','',''
regex = (r'.+, Version (\d+.\d\S+), '
         r'(.+\s){7}.+ '
         r'uptime is(( \d+ \w+,){2} \d+ \w+)'
         r'\s.+\s.+ file is "(\S+:\S+\.\w+)"')

