import os
import re
import requests
import wget
import sys,argparse

"""
		------------------------ HELP --------------------------------------
		> python pydownloadfb.py -h #for help

"""
class Fbdownloader() :
	def __init__(self,url,path) :
		self.url = url
		self.path = path
	def downloader(self):
		p = self.path
		u = self.url
		def check_url(url):
				try:
					req = requests.get(url)
					return True
				except Exception as E :
					return False
		def check_path(path):
			if os.path.exists(path) == True :
				return True
			if os.path.exists(path) == False :
				return False
		if check_url(u) == True and check_path(p) == True :
			choose_reslution = input("Choose Normal/HD resolution : ")
			req = requests.get(u)
			if choose_reslution == "Normal" :
				try :
					search = re.search('sd_src:".+?"',req.text)
					sd_url01 = re.sub('sd_src:','',search.group())
					sd_url = re.sub('"','',sd_url01)
					wget.download(sd_url,p)
				except Exception as Err :
				    pass
			if choose_reslution == "HD" :
				try :
				    search02 = re.search('hd_src:".+?"',req.text)
				    hd_url01 = re.sub('hd_src:','',search02.group())
				    hd_url = re.sub('"','',hd_url01)
				    wget.download(hd_url,p)
				except Exception as Err02 :
					search = re.search('sd_src:".+?"',req.text)
					sd_url01 = re.sub('sd_src:','',search.group())
					sd_url = re.sub('"','',sd_url01)
					wget.download(sd_url,p)
		if check_url(u) == False and check_path(p) == False or check_url(u) == False and check_path(p) == True or check_url(u) == True and check_path(p) == False :
			print('''You have Problem Check this Thinks : - Conection\n\t\t- URL\n\t\t- Saving Path\n\t\t- Check if The URL Video is Privet or Not''')

if len(sys.argv) > 1 :
	argument_parser = argparse.ArgumentParser(description="Download Facebook Video")
	argument_parser.add_argument('-u','--URL',type=str,metavar='URL',help='Video URL From Facebook')
	argument_parser.add_argument( '-p','--Path',type=str,metavar='PATH',
								  help='Destination Path Remove it to use default Path',
								  default=os.popen(r"echo C:\Users\%username%\Downloads").read().strip()
								)
	args = argument_parser.parse_args()
	url = args.URL
	path = args.Path
	downloader = Fbdownloader(url,path)
	downloader.downloader()

else :
	print("Please use -h for help")
