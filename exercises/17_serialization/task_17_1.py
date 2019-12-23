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
         r'uptime is((?: \d+ \w+,){2} \d+ \w+)'
         r'\s.+\s.+ file is "(\S+:\S+\.\w+)"')


def write_inventory_to_csv(data_filenames):
    r1,r2,r3 = '','',''
    for item in data_filenames:
        if r1 in item:
            r1 = 'r1'
            with open(item) as f:
                sh_ver_r1 = f.read()

        elif r2 in item:
            r2 = 'r2'
            with open(item) as f:
                sh_ver_r2 = f.read()

        else:
            r3 = 'r3'
            with open(item) as f:
                sh_ver_r3 = f.read()
