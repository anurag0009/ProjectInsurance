import pymongo
import pandas as pd
import json # mongo db store data in json\

client = pymongo.MongoClient("mongodb+srv://anurag1162:7754890302anu@practiseineuron.zonel7u.mongodb.net/?retryWrites=true&w=majority")
DATA_FILE_PATH = "/Users/anuragsingh/Desktop/Project/insurance/ProjectInsurance/insurance.csv"

DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"ROWS AND COLUMNS : {df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)