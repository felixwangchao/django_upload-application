# !/usr/bin/python
# Filename: base64_converter
# Auteur: Chao
import base64

print "base64: this is a script to" 
print "produce the url by using base64"
print 
print "please input the name of Editor:"
Editor = str(raw_input("name of Editor:"))

print
print
print

print "************************************"
print "please input the name of Publication:"
print "************************************"
Publication = str(raw_input("name of publicaiton:"))


message = Editor+'!'+Publication
print "the message before encoding is: ",message

safe_message = base64.urlsafe_b64encode(message)

print "the message after encoding is: ",safe_message


