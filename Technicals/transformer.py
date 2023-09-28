import requests

import csv

import json

def transform():
    with open("output.json", "w") as o:
        with open("fake_or_real_news 2.csv") as csvfile:
            filelist = csv.reader(csvfile)
            for row in filelist:
                r = {}
                r["title"] = row[1]
                r["article"] = row[2]
                r["authors"] = None
                r["date"] = None
                r["domain"] = None
                r["ind30k"] = row[0]
                r["url"] = None
                if row[3] == "REAL":
                    r["label"] = "human"
                else:
                    r["label"] = "machine"        
                r["orig_split"] = None
                r["split"] = "test"
                r["random_score"] = None 

                print(json.dumps(r), file=o)
if __name__ == "__main__":
    transform()
