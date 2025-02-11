from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://milvus:milvus@milvus.hmkzt.mongodb.net/?retryWrites=true&w=majority&appName=Milvus"
)

db = client.ds_hw_03_01

db.ds_hw_03_01.insert_many([
    {
        "name": 'Aboba',
        "age": 1,
        "features": ['точить кігті об диван', 'голосно мурчить', 'пʼє тільки воду з фільтру']
    },
    {
        "name": 'Bounty',
        "age": 2,
        "features": ['постійно спить', 'не реагує на людей', 'любить поїсти']
    },
    {
        "name": 'Couper',
        "age": 3,
        "features": ['чорний', 'ласкавий', 'ходить за хазяїном']
    },
    {
        "name": 'Dadley',
        "age": 4,
        "features": ['товстий', 'лінивий', 'пʼятнистий']
    },
    {
        "name": 'Eugen',
        "age": 5,
        "features": ['лисий', 'любить спати у коробці', 'їсть тільки з рук']
    },
])
