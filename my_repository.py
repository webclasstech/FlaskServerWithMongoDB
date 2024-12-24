import os
import certifi
from bson import ObjectId

from dotenv import load_dotenv
from pymongo import MongoClient
import utils

class MyMongoAgent:

    def __init__(self):
        load_dotenv()
        # print(f'mongo bd conn string: {os.getenv('MONGODB_CONNECT_STR')}')
        self.client = MongoClient(os.getenv('MONGODB_CONNECT_STR'), tlsCAFile=certifi.where())
        self.Database = self.client["wd9"]
        print(self.Database.name)
        self.dogs_collection = self.Database.Dogs


    def get_all_dogs(self):
        try :
            results = self.dogs_collection.find()
            # print(results) #this will print cursor, not useful for us
            # results = dogs_collection.find({"name":"Rexy"})
            # print(results)
            # print (utils.serialize_objectid(results))
            list_of_dogs = []
            for current in  results :
                list_of_dogs.append(utils.serialize_objectid(current))
            #print (list_of_dogs)
            # x = 4/0
            return list_of_dogs
        except Exception as e:
            raise


    def get_dog_by_id(self,id_str):
        results = self.dogs_collection.find({"_id": ObjectId(id_str)})
        # print(results)  # this will print cursor, not useful for us
        #print(utils.serialize_objectid(results))
        list_of_dogs = []
        for current in results:
            list_of_dogs.append(utils.serialize_objectid(current))
        #print(list_of_dogs)
        return list_of_dogs

    def insert_dog(self,new_dog_dict):
        #new_dog = {"name":"Flaffi","birthYear":2024, "breed":"Golden"}
        response = self.dogs_collection.insert_one(new_dog_dict)
        #print(response)
        return {"id":str(response.inserted_id)}

    # def update_dog0(self):
    #     updated_dog = {"birthYear": 2023, "breed": "Poodle"}
    #     response = self.dogs_collection.update_one({"name":"Flaffi"},{"$set" :updated_dog})
    #     print(response)

    def update_dog_by_id(self, id_str, updated_dog_dic):
        # updated_dog = {"birthYear": 2023, "breed": "Poodle 2"}
        # response = self.dogs_collection.update_one({"_id":ObjectId("676a85f023653a344c7af55a")},{"$set" :updated_dog})
        response = self.dogs_collection.update_one({"_id": ObjectId(id_str)}, {"$set": updated_dog_dic})
        #print(response)
        return response

    def delete_dog_by_id(self,id_str):
        response = self.dogs_collection.delete_one({"_id": ObjectId(id_str)})
        # print(response)
        return response

    # def delete_dog(self):
    #     response = self.dogs_collection.delete_one({"name":"Flaffi","birthYear":2023})
    #     print(response)



def test_dogs_mongo_db():
    my_mongo_agent = MyMongoAgent()

    # my_mongo_agent.get_all_dogs()
    #
    #  my_mongo_agent.insert_dog({"name":"Rocky","birthYear":2000, "breed":"German Shepherd"})
    print( my_mongo_agent.get_all_dogs())
    #  my_mongo_agent.update_dog_by_id("676a8aff56d052010dc657f0",{"name":"Miric"})
    # my_mongo_agent.update_dog0()
    # my_mongo_agent.get_all_dogs()
    #
    # my_mongo_agent.update_dog()
    # my_mongo_agent.get_all_dogs()

    # my_mongo_agent.delete_dog_by_id("676a672f529f6fcb7b0c0465")
    x = my_mongo_agent.get_all_dogs()
    print(x)
    x = my_mongo_agent.get_dog_by_id("676a666c529f6fcb7b0c0464")
    print(x)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_dogs_mongo_db()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
