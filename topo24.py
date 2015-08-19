"""Custom topology example"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.log import lg, setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

	#Add controller
	#c0 = self.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633)

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        h9 = self.addHost( 'h9' )
        h10 = self.addHost( 'h10' )
        h11 = self.addHost( 'h11' )
        h12 = self.addHost( 'h12' )
        h13 = self.addHost( 'h13' )
        h14 = self.addHost( 'h14' )
        h15 = self.addHost( 'h15' )
        h16 = self.addHost( 'h16' )
        h17 = self.addHost( 'h17' )
        h18 = self.addHost( 'h18' )
        h19 = self.addHost( 'h19' )
        h20 = self.addHost( 'h20' )
        h21 = self.addHost( 'h21' )
        h22 = self.addHost( 'h22' )
        h23 = self.addHost( 'h23' )
        h24 = self.addHost( 'h24' )
        
        s1 = [ self.addSwitch( 's1', dpid="0000000000000001")]
        s2 = [ self.addSwitch( 's2', dpid="0000000000000002")]
        s3 = [ self.addSwitch( 's3', dpid="0000000000000003")]
        s4 = [ self.addSwitch( 's4', dpid="0000000000000004")]
        s5 = [ self.addSwitch( 's5', dpid="0000000000000005")]
        s6 = [ self.addSwitch( 's6', dpid="0000000000000006")]
        s7 = [ self.addSwitch( 's7', dpid="0000000000000007")]
        s8 = [ self.addSwitch( 's8', dpid="0000000000000008")]
        s9 = [ self.addSwitch( 's9', dpid="0000000000000009")]
        s10 = [ self.addSwitch( 's10', dpid="0000000000000010")]
        s11 = [ self.addSwitch( 's11', dpid="0000000000000011")]
        s12 = [ self.addSwitch( 's12', dpid="0000000000000012")]
        s13 = [ self.addSwitch( 's13', dpid="0000000000000013")]
        s14 = [ self.addSwitch( 's14', dpid="0000000000000014")]
        s15 = [ self.addSwitch( 's15', dpid="0000000000000015")]
        s16 = [ self.addSwitch( 's16', dpid="0000000000000016")]
        s17 = [ self.addSwitch( 's17', dpid="0000000000000017")]
        s18 = [ self.addSwitch( 's18', dpid="0000000000000018")]
        s19 = [ self.addSwitch( 's19', dpid="0000000000000019")]
        s20 = [ self.addSwitch( 's20', dpid="0000000000000020")]
        s21 = [ self.addSwitch( 's21', dpid="0000000000000021")]
        s22 = [ self.addSwitch( 's22', dpid="0000000000000022")]
        s23 = [ self.addSwitch( 's23', dpid="0000000000000023")]
        s24 = [ self.addSwitch( 's24', dpid="0000000000000024")]



        # Add links
        
        self.addLink( 's1', 'h1', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's2', 'h2', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's3', 'h3', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's4', 'h4', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's5', 'h5', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's6', 'h6', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's7', 'h7', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's8', 'h8', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's9', 'h9', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's10', 'h10', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's11', 'h11', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's12', 'h12', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's13', 'h13', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's14', 'h14', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's15', 'h15', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's16', 'h16', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's17', 'h17', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's18', 'h18', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's19', 'h19', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's20', 'h20', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's21', 'h21', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's22', 'h22', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's23', 'h23', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's24', 'h24', bw=100, delay='5ms', max_queue_size=1000 )
        
        self.addLink( 's1', 's2', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's1', 's6', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's2', 's3', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's2', 's6', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's3', 's7', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's3', 's4', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's3', 's5', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's4', 's7', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's5', 's4', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's5', 's8', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's6', 's7', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's6', 's9', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's6', 's11', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's7', 's8', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's7', 's9', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's9', 's12', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's9', 's10', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's8', 's10', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's10', 's13', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's10', 's14', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's11', 's12', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's11', 's15', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's11', 's19', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's12', 's13', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's12', 's16', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's13', 's14', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's13', 's17', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's14', 's18', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's15', 's16', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's15', 's20', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's16', 's17', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's16', 's21', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's16', 's22', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's17', 's18', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's17', 's22', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's17', 's23', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's18', 's24', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's19', 's20', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's20', 's21', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's21', 's22', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's22', 's23', bw=100, delay='5ms', max_queue_size=1000 )
        self.addLink( 's23', 's24', bw=100, delay='5ms', max_queue_size=1000 )
        
	#self.start()

topos = { 'mytopo': ( lambda: MyTopo() ) }

