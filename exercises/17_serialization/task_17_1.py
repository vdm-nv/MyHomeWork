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
	
	.* \(.*\), Version (\d+.\d\S+\w{2}), .+ uptime is (\d+ \w+, \d+ \w+, \d+ \w+).* file is (\S+:\S+\.\w+).*
	
	 .+ +uptime is (\d+ \w+, \d+ \w+, \d+ \w+)
	 
	 re.search(r'.* \(.*\), Version (\d+.\d\S+\w{2}), .*\s.+\s.+\s.+\s.+',sh_version_r1).group()
	 
	 
	 r1 = re.findall(r'.* \(.*\), Version (\d+.\d\S+\w{2}), .*\s.+\s.+\s.+\s.+\s.+\s.*\s.+ uptime is (\d+ \w+, \d+ \w+, \d+ \w
     ...: +)\s.+\s.+ file is "(\S+:\S+\.\w+)',sh_version_r1)
    '''
