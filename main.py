import urllib2
import json
import sys

URL = "http://api.fixer.io" 
cur_set = {"AUD","BGN","BRL","CAD","CHF","CNY","CZK","DKK","GBP","HKD","HRK","HUF","IDR","ILS","INR","JPY","KRW","MXN","MYR","NOK","NZD","PHP","PLN","RON","RUB","SEK","SGD","THB","TRY","USD","ZAR","EUR"}
cache_fname = "cache"

def check(binary, prompt):
	if(binary):
		sys.exit(prompt)

def cur_format(str_in):
    for cur in cur_set:
        if str_in == cur:
            return str_in
    return

def main(exfrom="AUD", exto="CNY", date="latest"):
    global URL
    exfrom = cur_format(exfrom)
    exto = cur_format(exto)
    check((not exfrom) or (not exto), "ERROR: Format currency")
    URL = URL+'/'+date+'?base='+exfrom
    raw = urllib2.urlopen(URL)
	json = raw.read()

main()
