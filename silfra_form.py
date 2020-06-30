#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:21:26 2020

@author: root
"""


from flask import Flask, render_template, request
from firebase import firebase
import configurations
import pyrebase


app = Flask(__name__)
email = "null"

firebsevar = pyrebase.initialize_app(config=configurations.config)
db = firebsevar.database()
msg = " "

@app.route('/')
def Base():
    return render_template('form.html',msg="")




@app.route('/sub_form', methods=['POST', 'GET'])
def sub_form():
    
    if request.method == 'POST':
      
      f = request.files['file']
      if request.files['file'].filename != '':
          return render_template('form.html', msg = "")
        
      if request.files['file'].filename == '':
            return render_template('form.html',msg="You cannot Submit Empty File")
            
            
     
    




if __name__ == '__main__':
    app.run()
