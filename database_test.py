from pymongo import MongoClient

def Database(id,username,score, position):

    # print("others=",others)
    print(id,"id from database")
    print(username,"username from databaseeeee")
    print(score, "score from databaseeeee")
    print(position, "position from databaseeeee")
    cluster = MongoClient("mongodb://amirrmamdouh:123@ac-l1zkv5z-shard-00-00.g8t8zzf.mongodb.net:27017,ac-l1zkv5z-shard-00-01.g8t8zzf.mongodb.net:27017,ac-l1zkv5z-shard-00-02.g8t8zzf.mongodb.net:27017/?ssl=true&replicaSet=atlas-xsrnrq-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = cluster['Clients']
    collection=db["Records"]
    # for i in range(len(others)):


    p1={"_id":id,"name":username,"score":score,"position":position}

    collection.update_one(
        {"_id": id},
        {"$set": p1},
        upsert=True
    )