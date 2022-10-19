#Child Branch Data

import pymongo
try:
  
  with pymongo.MongoClient("mongodb://localhost:27017/") as client:
  #with pymongo.MongoClient(db_config['HOST']) as client:
      db = client[ "GVSKT"]
      myquery = { "address": "Bhumika Heights" , "address": "Apple" }
      #item = db["JSON"].find_one({'id':1})
      item = db["JSON"].find(myquery)
      print([i for i in item])

except Exception as ex:
   print(str(ex))

'''
try:
  import pymongo

  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  mydb = myclient["GVSKT"]
  mycol = mydb["JSON"]

  myquery = { "address": "Bhumika Heights" }
  mydoc = mycol.find(myquery)
  for x in mydoc:
    print(x)

  myclient.close()
  
  #mydb = myclient["GVSKT"]
  mycol = mydb["JSON"]
  myquery = { "address": "Bhumika Heights" }
  mydoc = mycol.find(myquery)
  for x in mydoc:
    print("\nAfter Closing Connection : " , x)

except Exception as ex:
   print(str(ex))
'''


#-----------------------------------------------------------------
'''

myquery = { "name": "kt" }

mydoc = mycol.find(myquery)
print("\nmydoc : ",mydoc)

for x in mydoc:
  print(x)



mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)




mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_one(mydict)

print(x.inserted_id)



#mydict = { "name": "kt", "address": "Bhumika Heights" }
#x = mycol.insert_one(mydict)
'''
