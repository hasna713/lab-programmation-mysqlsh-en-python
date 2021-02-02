# -*- coding: utf-8 -*-
"""

@author: CollegeBoreal
"""

import json
import mysqlx

session = mysqlx.get_session({
  "host": "localhost",
  "port": 33060,
  "user": "root",
  "password": "password"
})

db = session.get_schema("wold_x")

def lecture(fichier):
      nomColl = "temp"
      maColl = db.create_collection(nomColl)
      json = charge(fishier)
      maColl.add(json).execute()
      docs = maColl.find().execute()
      db.drop_collection(nomColl)
      return(docs)

def charge(fichier):
   with open(fichier) as f:
      return json.load(f)

def former_des_chefs(docs):
  nomColl = 'chefs_de_governement'
  maColl = db.create_collection(nomColl)


for doc in docs.fetch_all():
  for country in doc.countries:
    maColl.add(country['governement']).execute)

docs = maColl.find().execute()
db.drop_collection(nomColl)

def main():
  docs = lecture('b000000000.json')
  chefs = former_des_chefs(docs)
  print(len(chefs.fetch_all()))
  session.close

return(docs)