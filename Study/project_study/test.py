# -*- coding: utf-8 -*-
import smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.exmail.qq.com', '465')
smtp.login('guochunhua@chemi.ren', 'Gwx123456')
smtp.sendmail('guochunhua@chemi.ren', '371118530@qq.com', "接口自动化测试")
smtp.quit()