#!/usr/bin/python

from topo24 import MyTopo
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.util import pmonitor
from signal import SIGINT
from random import randint
from subprocess import Popen, PIPE
from async_subprocess import AsyncPopen, PIPE
from circus.process import *
import os
import time
import datetime
import subprocess
import psutil
import select
import urllib2

def master():
	print ">>>"
	# distribution-karaf-0.2.3-Helium-SR3/bin/karaf server >> karaf_run.out 2>&1 &
	cntrl = subprocess.Popen(['/home/mininet/distribution-karaf-0.2.3-Helium-SR3/bin/karaf', 'server'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

	while True:
		try:
			webCode = urllib2.urlopen("http://localhost:8181/dlux/index.html").getcode()
			if webCode == 200:
				break
			else:
				time.sleep(1)
		except urllib2.HTTPError, e:
			#print(e.code)
			time.sleep(1)
		except urllib2.URLError, e:
			#print(e.args)
			time.sleep(1)

	print "Controller PID: ", cntrl.pid, "\n\n\nMininet:\n"
	
        topo = MyTopo()
	net = Mininet(topo=topo,controller=lambda name: RemoteController( name, ip='127.0.0.1' ), listenPort=6633, link=TCLink, cleanup = True)
	f = createFolder('')
	net.start()

	print "\n\nOpen Wireshark\n\n"
	time.sleep(20)
	print ">>>\n\n"

        hosts = net.hosts
	
        server = hosts[ 0 ]
	hostsAux = list(hosts)
        popens = {}
	CLI(net)

        for h in hosts:
		createFolder( h.name )
		target = randint(0, len(hostsAux) - 1 )
                popens[ h ] = h.popen(['python', 'slave.py', h.name, h.MAC(), hostsAux[ target ].MAC(), str(cntrl.pid), "30"], shell=True, stdin=PIPE, stdout=PIPE)
		del hostsAux[ target ]
	
	#timeOutCntrl = time.time() + 
	
	lineNum = 0
	while cntrl.poll() == None:
		lineNum = lineNum + 1
		time.sleep(0.005)
		countHosts = 0
		for h in hosts:
			if popens[h].poll() != None:
				countHosts = countHosts + 1
		
		f.write("%s; %s; %s; %s;\n" % (str(lineNum), str(psutil.Process(cntrl.pid).get_memory_info()[0]), str(psutil.Process(cntrl.pid).get_memory_info()[1]), str(psutil.Process(cntrl.pid).cpu_percent(0.1))))
		#print "%s; %s; %s;\n" % (str(psutil.Process(cntrl.pid).get_memory_info()[0]), str(psutil.Process(cntrl.pid).get_memory_info()[1]), str(psutil.Process(cntrl.pid).cpu_percent(0.1)))
		if countHosts == 24:
			print "Stopping controller..."
			stop = subprocess.Popen('/home/mininet/distribution-karaf-0.2.3-Helium-SR3/bin/stop', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
			break

	"""
	while cntrl.poll() == None:
		time.sleep(5)
		if time.time() >= timeOutCntrl:
			for h in hosts:
				print h.name
				print popens[ h ].poll()
				popens[ h ].stdin.write('1\n')
				popens[ h ].stdin.flush()
			for h, line in pmonitor( popens, timeoutms=100 ):
				if h:
					print '2_%s: %s' % ( h.name, line ),
			break
		
		if ( lastRssMem*1.1 >= psutil.Process(cntrl.pid).get_memory_info()[0] ) and ( lastVmsMem*1.1 >= psutil.Process(cntrl.pid).get_memory_info()[1] ) and ( lastCpuPercent >= psutil.Process(cntrl.pid).cpu_percent(0.1) ):
			i = i + 500
			for h in hosts:
				#popens[ h ].stdin.write('%d\n' % (i))
				print h.name
				print popens[ h ].poll()
				popens[ h ].stdin.write('1000\n')
				popens[ h ].stdin.flush()


		lastRssMem = psutil.Process(cntrl.pid).get_memory_info()[0]
		lastVmsMem = psutil.Process(cntrl.pid).get_memory_info()[1]
		lastCpuPercent = psutil.Process(cntrl.pid).cpu_percent(0.1)
		for h, line in pmonitor( popens, timeoutms=100 ):
			if h:
				print '1_%s: %s' % ( h.name, line ),
		
	"""
	
        net.stop()



def createFolder( host ):

	mylist = []
	today = datetime.date.today()
	mylist.append(today)

	if not host:
		if not os.path.exists(os.path.dirname(os.path.abspath(__file__))+'/Runs'):
	    		os.makedirs(os.path.dirname(os.path.abspath(__file__))+'/Runs')

		if not os.path.exists(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])):
	    		os.makedirs(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0]))

		dirName = [d for d in os.listdir(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])) if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0]), d))]	

		os.makedirs(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])+'/Test_'+"{:0>5d}".format(len(dirName)+1))
		f = open(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])+'/Test_'+"{:0>5d}".format(len(dirName)+1)+"/history.txt", 'a')
		return f
	else:
		dirName = [d for d in os.listdir(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])) if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0]), d))]	

		if not os.path.exists(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])+'/Test_'+"{:0>5d}".format(len(dirName))+"/"+host):
	    		os.makedirs(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])+'/Test_'+"{:0>5d}".format(len(dirName))+"/"+host)

		



if __name__ == '__main__':
    setLogLevel( 'info' )
    master()
