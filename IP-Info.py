#!/usr/bin/env python3

import socket
try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect(("google.com", 80))
	s.close()
except socket.gaierror:
	exit("No internet connection")

try:
	import colorama
	import httpx as requests
except Exception as err:
	exit(err)

colorama.init(autoreset=True)
LB = colorama.Fore.LIGHTBLUE_EX
LG = colorama.Fore.LIGHTGREEN_EX
LC = colorama.Fore.LIGHTCYAN_EX
LR = colorama.Fore.LIGHTRED_EX
LY = colorama.Fore.LIGHTYELLOW_EX
RESET = colorama.Fore.RESET


class IP_Info:
	def __init__(self, ip):
		self._ip = ip

	@staticmethod
	def banner():
		print("\033c")
		print(f"{LG}="*50)
		print(f"{LR}[{LY} IP-Info Coded By R0b327{LR}			 ]")
		print(f"{LR}<"+f"{LG}="*48+f"{LR}>")
		print(f"{LR}[ {LY}Github{LR}:{RESET} https://github.com/R0b327		 {LR}]\n{LR}[ {LY}Facebook{LR}:{RESET} https://facebook.com/R0b327{LR}		 ]")
		print(f"{LG}="*50)

	def set(self):
		UA = {
			'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) BC3 iOS/3.12.7 (build 538; iPhone 11 Pro Max; iOS 14.7.1)'
		}
		try:
			print(f"{LB}[{LG}+{LB}]{LY} Sending Request...")
			if self._ip == "":
				exit(f"{LB}[{LR}!{LB}]{LR} Invalid IP Address, Try again.")
			check_ip = requests.get(f"http://ip-api.com/json/{self._ip}?fields=status,query", headers=UA, timeout=30).json()
			if check_ip['status'] == "fail":
				exit(f"{LB}[{LR}!{LB}]{LR} Invalid IP Address, Try again.")
			else:
				resp = requests.get(f"http://ip-api.com/json/{self._ip}?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname", headers=UA, timeout=30).json()
		except requests.ConnectError:
			exit(f"{LB}[{LR}!{LB}]{LR} Internet Connection Error, Try again.")
		except requests.ConnectTimeout:
			exit(f"{LB}[{LR}!{LB}]{LR} Internet Connection Error, Try again.")
		return f"""
{LB}[{LG}+{LB}]{LG} IP Address{LR}:{LC} {resp['query']}
{LB}[{LG}+{LB}]{LG} Country{LR}:{LC} {resp['continent']} {resp['country']} ({resp['countryCode']})
{LB}[{LG}+{LB}]{LG} Region{LR}:{LC} {resp['region']} ({resp['regionName']})
{LB}[{LG}+{LB}]{LG} City{LR}:{LC} {resp['city']}
{LB}[{LG}+{LB}]{LG} Zipcode{LR}:{LC} {resp['zip']}
{LB}[{LG}+{LB}]{LG} Timezone{LR}:{LC} {resp['timezone']}

{LB}[{LG}+{LB}]{LG} ISP{LR}:{LC} {resp['isp']}
{LB}[{LG}+{LB}]{LG} ASN{LR}:{LC} {resp['as']} {resp['asname']}

{LB}[{LG}+{LB}]{LG} Mobile{LR}:{LC} {resp['mobile']}
{LB}[{LG}+{LB}]{LG} VPN{LR}:{LC} {resp['proxy']}

{LB}[{LG}+{LB}]{LG} Google Map{LR}:{LC} https://www.google.com/maps/place/{str(resp['lat'])},{str(resp['lon'])}
		"""

def main():
	IP_Info.banner()
	ip = str(input(f"{LB}[{LG}+{LB}]{LY} Enter IP Address{LR}:{RESET} "))
	print(IP_Info(ip).set())

if __name__ == "__main__":
	main()
