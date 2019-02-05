import os
import md5

about = """
  Name            : Python Bruteforce
  Created By      : Sutriman
  Blog            : sutriman.com
"""
start_time = time.time()

def generate_stocklist():
	stock_list = 'abcdefghijklmnopqrstuvwxyz1234567890'
	stock_list_i = []
	for current in xrange(5):
	    a = [i for i in stock_list]
	    for y in xrange(current):
	        a = [x+i for i in stock_list for x in a]
	    stock_list_i = stock_list_i+a
	return stock_list_i

def bruteForce(new_stocklist, inputChiperText):
	for x in new_stocklist:
		hashed = md5.new(x).hexdigest() 
		if hashed == inputChiperText:
			return x
			break
	return False

def main():

    inputChiperText = raw_input("Input you chiper text: ")

    new_stocklist = generate_stocklist()
    process = bruteForce(new_stocklist, inputChiperText)
	
    if process != False:
    	print 'Result: '+process

    else:
    	print 'Not found'


if __name__ == '__main__':
    main()
