from pymongo import MongoClient

from bson.objectid import ObjectId
#
# def DB(id,username,score, position,delFlag):
#      if(delFlag==0):
#          Database(id,username,score, position)
#          Database1(id, username, score, position)
#      else:
#          delete_user(id,username,score, position)
#          delete_user1(id,username,score, position)
# def delete_user(id,username,score, position):
#      id=int(id)
#      # Connect to the MongoDB database
#      cluster = MongoClient("mongodb://amirrmamdouh:123@ac-l1zkv5z-shard-00-00.g8t8zzf.mongodb.net:27017,ac-l1zkv5z-shard-00-01.g8t8zzf.mongodb.net:27017,ac-l1zkv5z-shard-00-02.g8t8zzf.mongodb.net:27017/?ssl=true&replicaSet=atlas-xsrnrq-shard-0&authSource=admin&retryWrites=true&w=majority")
#      db = cluster['Clients']
#      collection = db['Records']
#
#      # Delete the user document based on the provided id
#      collection.delete_one({"name": username})
#      # collection.delete_one({"_id": id})
#      print(id,username,score, position,"User information deleted from the database.")
#
# def delete_user1(id,username,score, position):
#      id=int(id)
#      # Connect to the MongoDB database
#      cluster = MongoClient("mongodb://Mirna:123@ac-pdcgmvi-shard-00-00.z9x8y2q.mongodb.net:27017,ac-pdcgmvi-shard-00-01.z9x8y2q.mongodb.net:27017,ac-pdcgmvi-shard-00-02.z9x8y2q.mongodb.net:27017/?ssl=true&replicaSet=atlas-83vr9r-shard-0&authSource=admin&retryWrites=true&w=majority")
#      db = cluster['Clients']
#      collection = db['Records']
#
#      # Delete the user document based on the provided id
#      # collection.delete_one({"_id": id})
#      collection.delete_one({"name": username})
#      print(id,username,score, position,"User information deleted from the database1111111.")
# def Database(id,username,score, position):
#      # print("others=",others)
#      print(id,"id from database")
#      print(username,"username from databaseeeee")
#      print(score, "score from databaseeeee")
#      print(position, "position from databaseeeee")
#      cluster = MongoClient("mongodb://amirrmamdouh:123@ac-l1zkv5z-shard-00-00.g8t8zzf.mongodb.net:27017,ac-l1zkv5z-shard-00-01.g8t8zzf.mongodb.net:27017,ac-l1zkv5z-shard-00-02.g8t8zzf.mongodb.net:27017/?ssl=true&replicaSet=atlas-xsrnrq-shard-0&authSource=admin&retryWrites=true&w=majority")
#      db = cluster['Clients']
#      collection=db["Records"]
#      # for i in range(len(others)):
#
#
#      p1={"_id":id,"name":username,"score":score,"position":position}
#      collection.update_one(
#          {"_id":id},
#          {"$set": p1},
#          upsert=True
#      )
#      # if id in indices:
#      #     id=str(id)
#      #     p1 = {"_id": id, "name": username, "score": score, "position": position}
#      #     collection.insert_one(p1)
#      # else:
#      #     collection.update_one(
#      #         {"_id": id},
#      #         {"$set": p1},
#      #         upsert=True
#      #     )
#
# def Database1(id,username,score, position):
#
#      # print("others=",others)
#      print(id,"id from database11111")
#      print(username,"username from databaseeeee1111")
#      print(score, "score from databaseeeee11111")
#      print(position, "position from databaseeeee1111")
#      cluster = MongoClient("mongodb://Mirna:123@ac-pdcgmvi-shard-00-00.z9x8y2q.mongodb.net:27017,ac-pdcgmvi-shard-00-01.z9x8y2q.mongodb.net:27017,ac-pdcgmvi-shard-00-02.z9x8y2q.mongodb.net:27017/?ssl=true&replicaSet=atlas-83vr9r-shard-0&authSource=admin&retryWrites=true&w=majority")
#      db = cluster['Clients']
#      collection=db["Records"]
#      # for i in range(len(others)):
#
#
#      p1={"_id":id,"name":username,"score":score,"position":position}
#
#      collection.update_one(
#          {"_id":id},
#          {"$set": p1},
#          upsert=True
#      )
#      # if id in indices:
#      #     id = str(id)
#      #     p1 = {"_id": id, "name": username, "score": score, "position": position}
#      #     collection.insert_one(p1)
#      # else:
#      #     collection.update_one(
#      #         {"_id": id},
#      #         {"$set": p1},
#      #         upsert=True
#      #     )
#

# from pymongo import MongoClient


# def connect_to_mongodb(uri):
#     cluster = MongoClient(uri)
#     db = cluster['Clients']
#     collection = db['Records']
#     return collection












def delete_user(collection, username,id):

    if(id!=-1):
        collection.delete_many({"_id": id})
    else:
        collection.delete_many({"name": username})
    print(username, " User information deleted from the database.")

def delete_user1(collection, username,id):
    if (id != -1):
        collection.delete_many({"_id": id})
    else:
        collection.delete_many({"name": username})
    print(username, " User information deleted from the database1.")


def get_user(collection, username):
    user = collection.find_one({"name": username})
    return user


def update_user(collection, id, username, score, position):
    p1 = {"_id": id, "name": username, "score": score, "position": position}
    collection.update_one(
        {"_id": id},
        {"$set": p1},
        upsert=True
    )

    print(username, " User information updated from the database.")


def update_user1(collection, id, username, score, position):
    p1 = {"_id": id, "name": username, "score": score, "position": position}
    collection.update_one(
        {"_id": id},
        {"$set": p1},
        upsert=True
    )

    print(username, " User information deleted from the database1.")
# def DB(id, username, score, position, delFlag, quitted):
#     connection_options = {
#         'serverSelectionTimeoutMS': 600000,  # Timeout set to 60 seconds
#         # Add other connection options if needed
#     }
#
#     return True
def DB(id, username, score, position, delFlag,quitted):


    collection1 = MongoClient(
        "mongodb://amirrmamdouh:123@ac-l1zkv5z-shard-00-00.g8t8zzf.mongodb.net:27017,ac-l1zkv5z-shard-00-01.g8t8zzf.mongodb.net:27017,ac-l1zkv5z-shard-00-02.g8t8zzf.mongodb.net:27017/?ssl=true&replicaSet=atlas-xsrnrq-shard-0&authSource=admin&retryWrites=true&w=majority")
    collection2 = MongoClient(
        "mongodb://Mirna:123@ac-pdcgmvi-shard-00-00.z9x8y2q.mongodb.net:27017,ac-pdcgmvi-shard-00-01.z9x8y2q.mongodb.net:27017,ac-pdcgmvi-shard-00-02.z9x8y2q.mongodb.net:27017/?ssl=true&replicaSet=atlas-83vr9r-shard-0&authSource=admin&retryWrites=true&w=majority")

    cluster = collection1
    db = cluster['Clients']
    collection1 = db['Records']

    cluster1 = collection2
    db1 = cluster1['Clients']
    collection2 = db1['Records']

    if delFlag == 1:

        try:
            delete_user(collection1, username,-1)
        except:
            print("dbDelete0 failed")
        try:
            delete_user1(collection2, username,-1)
        except:
            print("dbDelete1 failed")

        # delete_user(collection1, username,-1)
        # delete_user1(collection2, username,-1)

    elif delFlag==0:
        try:
            update_user(collection1, id, username, score, position)
        except:
            print("db update0 failed")
        try:
            update_user1(collection2, id, username, score, position)
        except:
            print("db update1 failed")
        # update_user(collection1, id, username, score, position)
        # update_user1(collection2, id, username, score, position)
    if(quitted!=None and len(quitted)!=0):
        for i in range(len(quitted)):
            try:
                delete_user(collection1,None ,quitted[i])
            except:
                print("delete quitted failed db0")
            try:
                delete_user1(collection2,None ,quitted[i])
            except:
                print("delete quitted failed db1")

        # try:
        #     delete_user(collection1, username)
        # except:
        #     print("dbDelete0 failed")
        # try:
        #     delete_user1(collection2, username)
        # except:
        #     print("dbDelete1 failed")

    # else:
    #     try:
    #         update_user(collection1, id, username, score, position)
    #     except:
    #         print("db update0 failed")
    #     try:
    #         update_user1(collection2, id, username, score, position)
    #     except:
    #         print("db update1 failed")

