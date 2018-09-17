
#!/usr/bin/env python  
import os 
import sys

def main():

#docker run -d --net myNetwork --ip 172.20.0.82 --name cpe82 cpesim ./flaskSvr
    for ipnum in range(1,3):
        for cpenum in range(1, 9):
            os.system('docker run -d --net ingress --ip 172.20.' + bytes(ipnum) + '.' + bytes(cpenum) + ' --name cpe' + bytes(ipnum) + bytes(cpenum) + ' centos python -m SimpleHTTPServer 5400')  
            print (ipnum, '.', cpenum)

if __name__ == '__main__':  
    main()  


docker run -d --net myNetwork --ip 172.20.1.1 --name cpe11 centos python -m SimpleHTTPServer 5400

docker run -d --net my-net --ip 10.0.9.123 10.42.123.13:5000/centos python -m SimpleHTTPServer 5400
docker exec -it 2702 /bin/bash

docker run -d --net my-net --ip 10.0.9.99 10.42.123.13:5000/centos python -m SimpleHTTPServer 5400
docker exec -it 629d /bin/bash


	yum install dos2unix
	yum install zip
	yum install unzip
	yum install mlocate
	yum install psmisc
	yum install net-tools
	yum install tcpdump
	yum install expect
	yum install httpd
	yum install mod_ssl
	yum install vsftpd
	yum install openssh
	yum install compat-libstdc
	yum install glibc
	yum install perl
	yum install mysql
    /bin/systemctl restart sshd.service
    echo "Execute CNV4WG_config ......"
    ./CNV4WG/CNV4WG_config
    echo "Copy installagent lib ......"
    \cp -fr ./other/installagent_lib/* /usr/lib
    echo "Copy sqlite3 ......"
    \rm -fr /usr/bin/sqlite3
    \cp -fr ./other/sqlite3 /usr/bin
    echo "Copy http.conf ......"
    \cp -fr ./other/httpd.conf /etc/httpd/conf
    echo "Copy sysctl.conf ......"
    \cp -fr ./other/sysctl.conf /etc
    echo "Stop firewalld ......"
    systemctl stop firewalld.service
    systemctl disable firewalld.service
    echo "Restart httpd ......"
    systemctl restart httpd.service
    echo "Restart vsftpd ......"
    systemctl restart vsftpd.service


