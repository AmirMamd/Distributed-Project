from pymongo import MongoClient



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
    print("username found ",user)
    return user

def get_user1(collection, username):
    user = collection.find_one({"name": username})
    print("username found ", user)
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


def DB(id, username, score, position, delFlag,quitted,LostConnection):

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


    elif delFlag==0:
        try:

            update_user(collection1, id, username, score, position)
            print("db update0 successful")
        except:
            print("db update0 failed")
        try:

            update_user1(collection2, id, username, score, position)
            print("db update1 successful")
        except:
            print("db update1 failed")
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
    if(LostConnection==1):
        print("bengyb el old user aho")
        try:
            return get_user(collection1,str(username))
        except:
            print("except of getting user")
        try:
            return get_user1(collection2,str(username))
        except:
            print("except of getting user")

