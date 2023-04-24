import os
import sys

ip = sys.argv[1]

def ip_get(ip):

	fp = open('../buffer_login/accessed_ip.json', mode = 'r')
	ip_store = fp.readlines()
	fp.close()

	for i in range(0, len(ip_store)):

		ip_store[i] = ip_store[i].rstrip('\n')

	for i in ip_store:

		ip_store[ip_store.index(i)] = ip_store[ip_store.index(i)].split(' ')

	ip_check(ip, ip_store)

def ip_check(ip, ip_store):

	ip_state = False

	for i in ip_store:

		if (ip in i) == True:

			ip_state = True
			position = ip_store.index(i)

		else:

			continue

	if ip_state == True:

		fp = open('../buffer_login/accessed_ip.json', mode = 'r')
		ip_store = fp.readlines()
		fp.close()

		for i in range(0, len(ip_store)):

			ip_store[i] = ip_store[i].rstrip('\n')

		for i in ip_store:

			ip_store[ip_store.index(i)] = ip_store[ip_store.index(i)].split(' ')

		broadcast(ip_store[position][1])

	else:

		broadcast(False)

def broadcast(outcome):

	if outcome == False:

		print('failed')

	else:

		print(outcome)

ip_get(ip)