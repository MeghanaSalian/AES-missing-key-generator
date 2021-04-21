import subprocess
import sys
import os

def cmdline(command):
    proc = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out+'\n'+err 

def assemble(t, s=''):
    if t:
        for c in t[0]:
            assemble(t[1:], s+c)
    else:
        combkey.append(s)
        
s = "BECBXXACXXDBAEDBEEACFCFBCADEFAFF"
all_lets = tuple(["A", "B", "C", "D", "E","F"] + [str(i) for i in range(0,10)])
print(all_lets)
only_lets = tuple(["A", "B", "C", "D", "E","F"])
p2 = [all_lets if c in "X" else (c,) for c in s]
combkey = list()
assemble(p2)

print("Brute Forcing...")

counter = 0
for i, key in enumerate(combkey):
    #print("Trying "+str(i/len(combkey)))
    cmd = "openssl aes-128-ecb -d -K "+key+" -in 9.aes"
    text = cmdline(cmd)
    #print(text)
    #plaintextfile.write(str(key) + str(text) + "\n")
    if b"bad decrypt\r\n" not in text:
        print("##################Found!###############")
        print(key)
        print(text)
        print()
        counter += 1
        print(counter)
print("Found {} keys".format(counter))