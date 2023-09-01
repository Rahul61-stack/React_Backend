def generateMongoConnectionString(username: str, password: str, url: str, db: str):
    try:
        connectionString = (
            "mongodb+srv://" + username + ":" + password + "@" + url + "/" + db
        )
    except Exception as e:
        connectionString = None
        print("DB CONNECTION STRING GENERATTION FAILED: ", e)

    return connectionString
