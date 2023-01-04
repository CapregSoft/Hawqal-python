def convertJson(cursor):
    data_json = []
    header = [i[0] for i in cursor.description]
    data = cursor.fetchall()
    for i in data:
        data_json.append(dict(zip(header, i)))
    return data_json
