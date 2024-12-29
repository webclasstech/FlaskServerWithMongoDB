add .env file with following data, defines mongo db connection str, DB, collection (= table name):

    MONGODB_CONNECT_STR =
    DB_NAME =
    COLLECTION_NAME =

to install proj libraries:
    
    pip install "pymongo[srv]"
    pip install certifi 
    pip install bson 
    pip install python-dotenv
    pip install flask 
    pip install flask_cors

    
