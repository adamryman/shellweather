import sys

if __name__ =='__main__':
  if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    sys.exit(1)
  zipcode = sys.argv[1]