import re

IP_REG = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
IP_REG_COMP = re.compile(IP_REG)


""" Yes I know I could match everything from the regexp but I find it totally unnatural 
"""
def checkio(text):
	"""
		find all IPs
	"""
	good_ips = []
	for text_split in text.split(" "):
		for ip_match in re.finditer(IP_REG_COMP, text_split):
			valid = True
			for x in range(1,5):
				if not (0 <= int(ip_match.group(x)) <= 255):
					valid = False
			if valid:
				good_ips.append(ip_match.group(0))
	return good_ips	


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("192.168.1.1 and 10.0.0.1 or 127.0.0.1") == \
		["192.168.1.1", "10.0.0.1", "127.0.0.1"], "All correct"
	assert checkio("10.0.0.1.1 but 127.0.0.256 1.1.1.1") == \
		["1.1.1.1"], "Only 1.1.1.1"
	assert checkio("167.11.0.0 1.2.3.255 192,168,1,1") == \
		["167.11.0.0", "1.2.3.255"], "0 and 255"
	assert checkio("267.11.0.0 1.2.3.4/16 192:168:1:1") == \
		[], "I don't see IP"
	assert checkio("00250.00001.0000002.1 251.1.2.1") == \
		["251.1.2.1"], "Be careful with zeros"
