fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh: 
    line = line.rstrip()
    newfile = line.upper()
    print newfile
    