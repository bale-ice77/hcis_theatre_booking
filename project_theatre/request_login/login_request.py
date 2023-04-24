import sys
import time
import os
import fileinput
import random

alphebet = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
ID = sys.argv[1]
ip = sys.argv[2]

def request(ID):

	code_store = open('../database/codes.json')
	code_valid = code_store.readlines()
	code_valid = [x.strip() for x in code_valid]
	code_store.close()

	localtime = time.asctime(time.localtime(time.time()))

	fp = open('../database/loginhis.json', mode = 'r')
	loginhis = fp.read()
	fp.close()

	fp = open('../database/loginhis.json', mode = 'w')
	fp.write(loginhis)

	ID = decypher(ID)
	fp.write(localtime + '\n' + 'IP address:' + ip + '\nID entered:' + ID + '\n')

	if (ID in code_valid) == True:

		fp.write('Access granted' + '\n \n')
		fp.close()

		ip_buffer(ip, True)
		print('granted')

	else:

		fp.write('Access denied' + '\n \n')
		fp.close()

		ip_buffer(ip, False)
		print('denied')

def decypher(ID):

	text = []

	raw_text = ID
	raw_text = ' '.join(raw_text)
	raw_text = raw_text.split(' ')
	spins = 7

	while (len(raw_text)>0):

		letter = raw_text.pop(0)
		index = alphebet.index(letter)
		index = index + spins

		while index > 35:

			index = index-36

		letter = alphebet[index]
		text.append(letter)
		spins = spins*2

	ID = ''.join(text)
	return ID

def ip_buffer(ip, permitted):


	if permitted == True:

		record_ip(True)

	else:

		record_ip(False)

def record_ip(permitted):

	ip_his_split = []
	ip_state = False

	ip_his = open('ip_his.json', mode = 'r')
	ip_stock_backup = ip_his.read()
	ip_stock = ip_stock_backup.split('\n')
	ip_his.close()

	if permitted == True:

		for i in ip_stock:

			ip_his_split.append(i.split(' '))

		for i in ip_his_split:

			if (ip in i) == True:

				ip_state = True
				position = ip_his_split.index(i)

			else:

				continue

		ip_buffer = open('../buffer_login/accessed_ip.json', mode = 'r')
		accessed_ip = ip_buffer.readlines()

		for i in range(0, len(accessed_ip)):

			accessed_ip[i] = accessed_ip[i].rstrip('\n')

		if ip_state == True:

			if int(ip_his_split[position][1]) <= 10:

				alter(ip_his_split, True, position)

			else: 

				print('banned')
				quit()

			alter(ip_his_split, True, position)

			if ((ip + ' ' + ID) in accessed_ip) == True:
			
				ip_buffer.close()
				ip_his.close()

			else:

				ip_buffer.close()
				ip_buffer = open('../buffer_login/accessed_ip.json',mode = 'a')
				
				ip_buffer.write(ip + ' ' + ID + '\n')

				ip_buffer.close()
				ip_his.close()

		else:
			
			if (ip in accessed_ip) == True:
			
				ip_buffer.close()
				ip_his.close()

			else:
			
				ip_buffer.close()
				ip_buffer = open('../buffer_login/accessed_ip.json', mode = 'a')
				ip_his = open('ip_his.json', mode='w')

				ip_his.write(ip_stock_backup + ip + ' 0\n')

				ip_buffer.write(ip + ' ' + ID + '\n')

				ip_buffer.close()
				ip_his.close()

	if permitted == False:

		for i in ip_stock:

			ip_his_split.append(i.split(' '))

		for i in ip_his_split:

			if i in ip_his_split:

				if (ip in i) == True:

					ip_state = True
					position = ip_his_split.index(i)

				else:

					continue

		if ip_state == True:

			if int(ip_his_split[position][1]) <= 10:

				alter(ip_his_split, False, position)

			else: 

				print('banned')
				quit()

		else: 

			ip_his = open('ip_his.json', mode='w')
			ip_his.write(ip_stock_backup + ip + ' 1\n')

			ip_his.close()

def alter(ip_his_split, permitted, position):

	if permitted == True:

		c = str((random.randint(0,999999))) + '.json'

		with open('ip_his.json', "r", encoding="utf-8") as f1,open("%s.bak" % c, "w", encoding="utf-8") as f2:

			for line in f1:

				if (ip_his_split[position][0] + ' ' + ip_his_split[position][1]) in line:

					line = line.replace((ip_his_split[position][0] + ' ' + ip_his_split[position][1]), ip_his_split[position][0] + ' ' + '0')

				f2.write(line)

		os.remove('ip_his.json')
		os.rename("%s.bak" % c, 'ip_his.json')

	if permitted == False:
	
		c = str((random.randint(0,999999))) + '.json'

		with open('ip_his.json', "r", encoding="utf-8") as f1,open("%s.bak" % c, "w", encoding="utf-8") as f2:

			for line in f1:

				if (ip_his_split[position][0] + ' ' + ip_his_split[position][1]) in line:

					line = line.replace((ip_his_split[position][0] + ' ' + ip_his_split[position][1]), ip_his_split[position][0] + ' ' + str(int(ip_his_split[position][1])+1))

				f2.write(line)

		os.remove('ip_his.json')
		os.rename("%s.bak" % c, 'ip_his.json')

request(ID)