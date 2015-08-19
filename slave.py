#!/usr/bin/python

from subprocess import call
from signal import SIGINT
from socket import socket, AF_PACKET, SOCK_RAW

import os
import time
import datetime
import sys
import dpkt
import random
import subprocess
import select
import math
import psutil

def slave(thisHost, srcMAC, dstMAC, cntrlPid, t):

	#srcMAC = "1e:52:70:67:70:24"
	#h1dstMAC = "46:54:f1:81:a8:74"

	f = createPCAP(thisHost)
	pcap = dpkt.pcap.Reader(f)
	log = createLog(thisHost)
	#print "value of t:"
	#print t

	mylist = []
	today = datetime.date.today()
	mylist.append(today)
	dirName = [d for d in os.listdir(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])) if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0]), d))]
	#f2 = open(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])+'/Test_'+"{:0>5d}".format(len(dirName))+"/"+thisHost+'/history.txt', 'a')

	s = socket(AF_PACKET, SOCK_RAW)	
	interface = str(thisHost+"-eth0")
	s.bind((interface, 0))
	upperLimit = 500
	timeLimit = time.time() + t
	#doLoop = True
	#totalTransf = 0
	count = 0
	thrpt = 0
	#line = 0
	lastRssMem = psutil.Process(cntrlPid).get_memory_info()[0]
	lastVmsMem = psutil.Process(cntrlPid).get_memory_info()[1]
	lastCpuPercent = psutil.Process(cntrlPid).cpu_percent(0.1)
	#print "t1"
	while time.time() <= timeLimit:
		#print time.time()," < ",timeLimit
		for ts, buf in pcap:
			#print "t2"
			startTime = time.clock()
			pktSize = len(buf)
			count = count + 1
			try:
				eth = dpkt.ethernet.Ethernet(buf)
				eth.dst = ''.join(x.decode("hex") for x in dstMAC.split(":"))
				eth.src = ''.join(x.decode("hex") for x in srcMAC.split(":"))
			except:
				pass
			s.send(str(eth))

			endTime = time.clock()
		
			thrpt = ((pktSize)/((endTime-startTime)) + thrpt)/count
			
			if ( thrpt > upperLimit ) and ( ( ( ( pktSize )/( upperLimit ) ) - ( endTime-startTime ) ) > 0 ):
				time.sleep( ( ( ( pktSize )/( upperLimit ) ) - ( endTime-startTime ) ) )
				if time.time() <= timeLimit:
					break

		if ( lastRssMem*1.1 >= psutil.Process(cntrlPid).get_memory_info()[0] ) and ( lastVmsMem*1.1 >= psutil.Process(cntrlPid).get_memory_info()[1] ): # and ( lastCpuPercent >= psutil.Process(cntrlPid).cpu_percent(0.1) ):
			upperLimit = upperLimit + 500

		lastRssMem = psutil.Process(cntrlPid).get_memory_info()[0]
		lastVmsMem = psutil.Process(cntrlPid).get_memory_info()[1]
		lastCpuPercent = psutil.Process(cntrlPid).cpu_percent(0.1)

		

	#f2.close()
	log.close()
	f.close()

def createLog( thisHost ):

	mylist = []
	today = datetime.date.today()
	mylist.append(today)

	dirName = [d for d in os.listdir(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])) if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0]), d))]	

	f = open(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])+'/Test_'+"{:0>5d}".format(len(dirName))+"/"+thisHost+"/log.txt", 'a')
	return f

def createPCAP(thisHost):

	mylist = []
	today = datetime.date.today()
	mylist.append(today)

	dirName = [d for d in os.listdir(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])) if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0]), d))]	
	fileName = os.path.dirname(os.path.abspath(__file__))+'/Runs/'+str(mylist[0])+'/Test_'+"{:0>5d}".format(len(dirName))+"/"+thisHost+"/eth_"+thisHost+".pcap"
#######
	#fileName = os.path.dirname(os.path.abspath(__file__))+"/Runs/2015-06-01/Test_00001/h1/eth_h1.pcap"
#######
	call(["randpkt", "-b" , "1518", "-c", "50", "-t", "eth", fileName])
	f = open(fileName)	
	return f

def MACstrTobytes(str):
   return ''.join( [ "%c" % int(x) for x in str.split(":") ] )

if __name__ == '__main__':
	print str(sys.argv)
	slave(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]))
	
