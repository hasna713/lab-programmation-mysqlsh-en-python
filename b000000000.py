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

def charge(fichier):
   with open(fichier) as f:
      return json.load(f)

def main():
  print(charge('b000000000.json'))
  session.close

if __name__ == "__main__":
    main()
