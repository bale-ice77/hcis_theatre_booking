import time
import socket
import psutil
import os 
import fileinput

def ip_clients_get():

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ip_connect = []

    tcp_connections = psutil.net_connections(kind='tcp')

    for conn in tcp_connections:

        if conn.status == 'ESTABLISHED':

            remote_ip = conn.raddr.ip

            if remote_ip != ip_address:

                if (remote_ip in ip_connect) == 0:

                    if (':' in remote_ip) == 1:

                      continue

                    else:

                        ip_connect.append(remote_ip)

                else:

                    continue

    print(ip_connect)
    return ip_connect

def ip_con_clients_get():

    code = []
    con_clients = open('accessed_ip.json', mode = 'r')

    con_ips = con_clients.readlines()
    con_ips = [x.strip() for x in con_ips]

    for i in con_ips:

        con_ips[con_ips.index(i)] = i.split(' ')[0]

        if (len(i) == 2):

            code.append(i.split(' ')[0] + i.split(' ')[1])

    con_clients.close()

    ip_compare(con_ips, code)

def ip_compare(cur_ip, codes):

    ips = ip_clients_get()

    for i in ips:

        if (i in cur_ip) == True:

            continue

        else:

            ips.pop(ips.index(i))

            con_clients = open('accessed_ip.json', mode = 'w')

            for i in ips:

                if (i in codes) == True: 

                    index = codes.index(i)
                    con_clients.write(i + ' ' + codes[int(index)+1] + '\n')

                else:

                    continue

            con_clients.close()
            return 'null'


def loop():

    loop = True

    while (loop == True):

        ip_con_clients_get()
        time.sleep(5)

loop()