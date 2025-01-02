# pip install cowsay \ in the commandline
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1]) # cow or trex

from sayings import hello # goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1]) 
#   goodbye