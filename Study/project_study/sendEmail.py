# -*- coding: utf-8 -*-
from Study.project_study.readConfig import ReadConfig as cg

email_server = cg().getEmailValue('host')
email_port = cg().getEmailValue('port')
username = cg().getEmailValue('username')
password = cg().getEmailValue('password')
sender = cg().getEmailValue('sender')
receiver = cg().getEmailValue('receiver')
msg = cg().getEmailValue('msg')

print(email_server)
print(email_port)
print(username)
print(password)
print(sender)
print(receiver)
print(msg)