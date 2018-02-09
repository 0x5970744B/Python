#! /usr/bin/python

#Author: Timothy Gan

#Description: My first python program, a ping sweep script, created during and for my PWK course. Yes, I know 1 line of bash can do this :)

import subprocess

# Define IP network to ping
ip_network = "10.11.1."

for i in range(1, 254):
    
    #Define current IP address to ping
    ip = ip_network + str(i)
    
    #Command 1: Define the actual ping command
    ping_command = subprocess.Popen(['ping', '-c', '1', ip], stdout=subprocess.PIPE)

    #Command 2: Translate to remove newlines (replace '\n' with ' ') from the ping output
    translate_command = subprocess.Popen(['tr', '\\n', ' '], stdin=ping_command.stdout, stdout=subprocess.PIPE)

    #Command 3: Perform pattern matching on the ping output to print only the IP address and only if the string "1 received" is found
    patternMatch_command = subprocess.Popen(['awk', '/1 received/ {print $2}'], stdin=translate_command.stdout, stdout=subprocess.PIPE)
    
    #Run the last command, which will start the command chain from stdin
    final_output = patternMatch_command.communicate()[0]

    #Do not print blank line if there is no output
    if len(final_output)!=0:
        #Print output (both awk and print commands contains newlines, so we strip the newline from the awk output to prevent duplicate newline)
        print final_output.rstrip('\n\r')
