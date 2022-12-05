

from flask_testing import TestCase
from testapp import *
import unittest
import os
import sqlite3


currentdirectory  = os.path.dirname(os.path.abspath(__file__))

class Test(unittest.TestCase):
        
    def test_user_profile(self):
        profile = getUserProfile(User.email)
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query1 = "SELECT email,countryCode,native_Lang,level, bio from USER_PROFILE WHERE email =  '{email}' ".format(email = User.email)
        cursor.execute(query1)
        result = cursor.fetchall()
        data  =result[0][0]
        self.assertEqual(User.email,data)
        self.assertEqual(profile.countryCode,result[0][1])
        self.assertEqual(profile.nativeLang,result[0][2])
        self.assertEqual(profile.level,result[0][3]) 
        connection.close()
        

    def test_user(self):
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query1 = "SELECT email,password from USER WHERE email = '{email}' ".format(email = User.email)
        cursor.execute(query1)
        result = cursor.fetchall()
        self.assertEqual(User.email,result[0][0])
        self.assertTrue(bcrypt.check_password_hash(result[0][1], User.password))
        connection.close()
        

    def test_profile(self):
        profile = getUserProfile('tien@gmail.com')
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query1 = "SELECT email,countryCode,native_Lang,level, bio from USER_PROFILE WHERE email = 'tien@gmail.com' "
        cursor.execute(query1)
        result = cursor.fetchall()
        self.assertEqual(profile.email,result[0][0])
        self.assertEqual(profile.countryCode,result[0][1])
        self.assertEqual(profile.nativeLang,result[0][2])
        self.assertEqual(profile.level,result[0][3])
        connection.close()

    def test_getUser(self):
        user = getUserByEmail(User.email)
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query1 = "SELECT name,email,password from USER WHERE email = '{email}' ".format(email = user.email)
        cursor.execute(query1)
        result = cursor.fetchall()
        self.assertEqual(user.name,result[0][0])
        self.assertEqual(user.email,result[0][1])
        self.assertEqual(user.password,result[0][2])
        connection.close()

    def test_day_Ava_Class(self):
        self.assertEqual(Ava.day1,"monday")
        self.assertEqual(Ava.day2,"tuesday")
        self.assertEqual(Ava.day3,"wednesday")
        self.assertEqual(Ava.day4,"thursday")
        self.assertEqual(Ava.day5,"friday")
        self.assertEqual(Ava.day6,"saturday")
        self.assertEqual(Ava.day7,"sunday")

    def test_update_Ava(self):
        
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query1 = "SELECT day,start_time,end_time from AVAILABILITY WHERE email ='{email}' ".format(email = User.email)
        cursor.execute(query1)
        result = cursor.fetchall()
        i=0
        if(result!=None):
            while i<8:
                j=0
                while j<len(result):
                    if(i==1):
                        if(Ava.day1 == result[j][0]):
                            self.assertEqual(Ava.day1,result[j][0])
                            self.assertEqual(Ava.s1,result[j][1])
                            self.assertEqual(Ava.e1,result[j][2])
                    elif(i==2):
                        
                        if(Ava.day2 == result[j][0]):
                            self.assertEqual(Ava.day2,result[j][0])
                            self.assertEqual(Ava.s2,result[j][1])
                            self.assertEqual(Ava.e2,result[j][2])
                    elif(i==3):
                        if(Ava.day3 == result[j][0]):
                            self.assertEqual(Ava.day3,result[j][0])
                            self.assertEqual(Ava.s3,result[j][1])
                            self.assertEqual(Ava.e3,result[j][2])
                    elif(i==4):
                        
                        if(Ava.day4 == result[j][0]):
                            self.assertEqual(Ava.day4,result[j][0])
                            self.assertEqual(Ava.s4,result[j][1])
                            self.assertEqual(Ava.e4,result[j][2])
                    elif(i==5):
                        if(Ava.day5 == result[j][0]):
                            self.assertEqual(Ava.day5,result[j][0])
                            self.assertEqual(Ava.s5,result[j][1])
                            self.assertEqual(Ava.e5,result[j][2])
                    elif(i==6):
                        
                        if(Ava.day6 == result[j][0]):
                            self.assertEqual(Ava.day6,result[j][0])
                            self.assertEqual(Ava.s6,result[j][1])
                            self.assertEqual(Ava.e6,result[j][2])
                    elif(i==7):
                        if(Ava.day7 == result[j][0]):
                            self.assertEqual(Ava.day7,result[j][0])
                            self.assertEqual(Ava.s7,result[j][1])
                            self.assertEqual(Ava.e7,result[j][2])
                    j+=1
                
                i+=1
        connection.close()

    
    def test_session(self):
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query1 = "SELECT email,duration,people,timeZone from SESSION WHERE email = '{email}' ".format(email = User.email)
        cursor.execute(query1)
        result = cursor.fetchall()
        self.assertEqual(Session.email,result[0][0])
        self.assertEqual(Session.duration,result[0][1])
        self.assertEqual(Session.people,result[0][2])
        self.assertEqual(Session.timeZone,result[0][3]) 
        connection.close()

    
    def test_user_learningLang(self):
        profile = getUserProfile(User.email)
        list2 = []
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query2 = "SELECT learning_lang from LEARNING_LANG WHERE email = '{email}' ORDER BY learning_lang".format(email = User.email)
        cursor.execute(query2)
        result2 = cursor.fetchall()
        i=0
        while i <len(result2):
            list2 += result2[i]
            i = i+1
        self.assertEqual(profile.learningLang,list2)
        connection.close()

    def test_user_interest(self):
        profile = getUserProfile(User.email)
        list3 = []
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query3 = "SELECT interest from INTERESTS WHERE email = '{email}' ORDER BY interest".format(email = User.email)
        cursor.execute(query3)
        result3 = cursor.fetchall()
        i=0
        while i <len(result3):
            list3 += result3[i]
            i = i+1
        self.assertEqual(profile.interests,list3)
        connection.close()



