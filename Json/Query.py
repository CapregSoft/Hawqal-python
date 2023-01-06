import json


def convertJson(cursor):
    jsonData = []
    rows = [item for item in cursor]
    cols = [item[0] for item in cursor.description]
    for row in rows:
        data = {}
        for index, value in zip(cols, row):
            data[index] = value
        jsonData.append(data)
    encodedData = json.dumps(jsonData, ensure_ascii=False)
    return encodedData
