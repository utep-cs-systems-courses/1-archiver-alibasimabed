import os, tarfile, sys

if sys.argv[1] == 'c':
    
    print(sys.argv[1])


    tar = tarfile.open(sys.argv[4] + "compressed", "w:gz")
    
    tar.add(sys.argv[2])
    tar.add(sys.argv[3])

    tar.close()


elif sys.argv[1] == 'x':

    with tarfile.open(sys.argv[2], "r") as tar:
        print("Opened tarfile")
        tar.extractall(path=sys.argv[3])
        print("All files extracted")
    
    
else:
    print("First system argument is not c or x. Try again.")