
from pymongo import MongoClient
client = MongoClient ("mongodb+srv://mehmet:mehmet@mehmetbankkonto.8ktnn.mongodb.net/bank_simulation?retryWrites=true&w=majority")
db = client['bank_simulation']
collection= db ['bankData']
# print(collection)
pdata= {'_id': 14, 'name': 'Mehmet'}
# collection.insert_one(pdata)

# collection.delete_one({'_id': 11})
# collection.update_one({'_id': 10}, {'$set':{'name': 'Mike'}})

# result= collection.find_one({'_id': 10})
# result1=collection.find_one
# print(result)
result= collection.find_one({'_id': 0})['counter']
print(result)
