from pymongo import MongoClient, errors

client = MongoClient(
    "mongodb+srv://milvus:milvus@milvus.hmkzt.mongodb.net/?retryWrites=true&w=majority&appName=Milvus"
)

db = client["ds_hw_03_01"]


def find_all(): # Виведення всіх документів колекції
    try:
        result = db['ds_hw_03_01'].find({})
        for el in result:
            print(el)

    except errors.ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except errors.InvalidName:
        print("Invalid database or collection name.")
    except Exception as e:
        print(f"An error occurred: {e}.")


def find_by_name(name): # Пошук документа за значенням ключа "name"
    try:
       result = db['ds_hw_03_01'].find_one({"name": name})
       if result:
           print(result)
       else:
           print(f"Document with name {name} not found.")

    except errors.ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except errors.InvalidName:
        print("Invalid database or collection name.")
    except Exception as e:
        print(f"An error occurred: {e}.")


def upd_age_by_name(name, new_age): # Оновлення значення ключа "age" для знайденого документа за значенням ключа "name"
    try:
        result = db['ds_hw_03_01'].update_one(filter={"name": name}, update={"$set": {"age": new_age}})
        if result:
            print(result)
        else:
            print(f"Document with name {name} not found.")

    except errors.ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except errors.InvalidName:
        print("Invalid database or collection name.")
    except Exception as e:
        print(f"An error occurred: {e}.")



def add_feature_by_name(name, new_feature): # Додавання значення ключу "features" для знайденого документа за значенням ключа "name"
    try:
        result = db['ds_hw_03_01'].update_one(filter={"name": name}, update={"$push": {"features": new_feature}})
        if result:
            print(result)
        else:
            print(f"Document with name {name} not found.")

    except errors.ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except errors.InvalidName:
        print("Invalid database or collection name.")
    except Exception as e:
        print(f"An error occurred: {e}.")


def delete_by_name(name): # Видалення документа за ключем "name"
    try:
        result = db['ds_hw_03_01'].delete_one(filter={"name": name})
        if result:
            print(result)
        else:
            print(f"Document with name {name} not found.")

    except errors.ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except errors.InvalidName:
        print("Invalid database or collection name.")
    except Exception as e:
        print(f"An error occurred: {e}.")



def delete_all_docs(): # Видалення всіх документів колекції
    try:
        db['ds_hw_03_01'].delete_many({})

    except errors.ConnectionFailure:
        print("Failed to connect to MongoDB.")
    except errors.InvalidName:
        print("Invalid database or collection name.")
    except Exception as e:
        print(f"An error occurred: {e}.")




find_all()