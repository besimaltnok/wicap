#!/usr/bin/env python

from scapy.all import *
import termcolor
import colorema
import sys

def wicap(pkt):
   pass
   

sniff(offline="pcap_file", prn=wicap)
