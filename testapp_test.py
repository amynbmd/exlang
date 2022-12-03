import json
from flask_testing import TestCase
from testapp import *
import unittest
from flask import jsonify
import os
import sqlite3


currentdirectory  = os.path.dirname(os.path.abspath(__file__))

class Test(unittest.TestCase):
        
    def test_user_profile(self):
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query1 = "SELECT email,countryCode,native_Lang,level, bio from USER_PROFILE WHERE email = 'tien@gmail.com' "
        cursor.execute(query1)
        result = cursor.fetchall()
        data  =result[0][0]
        self.assertEqual('tien@gmail.com',data)
        self.assertEqual('VN',result[0][1])
        self.assertEqual('vi',result[0][2])
        self.assertEqual('Beginner',result[0][3])
        connection.commit()
        

    def test_user(self):
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query1 = "SELECT name,email from USER WHERE email = 'tien@gmail.com' "
        cursor.execute(query1)
        result = cursor.fetchall()
        self.assertEqual('tien',result[0][0])
        self.assertEqual('tien@gmail.com',result[0][1])

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
        connection.commit()

    def test_getUser(self):
        user = getUserByEmail('tien@gmail.com')
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        query1 = "SELECT name,email,password from USER WHERE email = 'tien@gmail.com' "
        cursor.execute(query1)
        result = cursor.fetchall()
        self.assertEqual(user.name,result[0][0])
        self.assertEqual(user.email,result[0][1])
        self.assertEqual(user.password,result[0][2])




