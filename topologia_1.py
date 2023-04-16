from mininet.topo import Topo

from mininet.net import Mininet
from mininet.link import TCLink

class MyTopo( Topo ):
        def build( self ):
                # Add Hosts and Switches
                h1 = self.addHost( 'h1' )
                h2 = self.addHost( 'h2' )
                h3 = self.addHost( 'h3' )
                h4 = self.addHost( 'h4' )
                s1 = self.addSwitch( 's1' )
                s2 = self.addSwitch( 's2' )
                s3 = self.addSwitch( 's3' )
                s4 = self.addSwitch( 's4' )

                # Add links
                self.addLink( h1, s1 )
                self.addLink( h2, s1 )
                self.addLink( s1, s2 )
                self.addLink( h3, s3 )
                self.addLink( h4, s4 )
                self.addLink( s4, s3, bw=10, delay='30ms', loss=10, cls=TCLink )
                self.addLink( s3, s2, bw=10, delay='15ms', cls=TCLink )

topos = { 'mytopo': ( lambda: MyTopo() ) }
