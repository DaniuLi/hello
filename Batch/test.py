import os,sys

print(__file__)

print(os.path.realpath(__file__))

print(os.path.dirname(os.path.realpath(__file__)))

print(os.path.split(os.path.realpath(__file__))[0])

print(os.path.abspath(__file__))

print(os.getcwd())

print(os.curdir)

print(sys.path[0])

print(sys.argv[0])