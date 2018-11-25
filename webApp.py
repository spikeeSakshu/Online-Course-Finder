# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:33:05 2018

@author: Spikee
"""



from CourseEra import CourseEra
from edx import edx
import threading

import time
from online_stanford import online_stanford

from flask import Flask, render_template, request
app = Flask(__name__)
files=[]



res=dict()
def parallel(query):
    files.extend([CourseEra(query),online_stanford(query),edx(query)])
    threads=[threading.Thread(target=process_url,args=(fun,)) for fun in files]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
        
def call(fun):
    res.update(fun)
    
def merge(re1,re2,re3):
    res.update(re1)
    res.update(re2)
    res.update(re3)
    
@app.route('/')
def getQuery():
   return render_template('Index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      query = request.form["query"]
      
      #parallel(query)
      t1=time.time()
      re1=CourseEra(query)
      re2=online_stanford(query)
      re3=edx(query)
      t2=time.time()
      merge(re1,re2,re3)
      
      print("Total Time",t2-t1)
      print(res)
      return render_template("result.html",result = res)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=80)
    

 #re2=edx(query)
 #re3=online_stanford(query)