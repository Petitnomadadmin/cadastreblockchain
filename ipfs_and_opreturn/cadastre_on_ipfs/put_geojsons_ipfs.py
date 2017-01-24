import argparse
import ipfsapi
parser = argparse.ArgumentParser(description='ADD folder to IPFS')
parser.add_argument("folder", help="folder to add to ipfs")
args = parser.parse_args()
print(args.folder)
api = ipfsapi.connect('127.0.0.1', 5001)

api.add(args.folder)

