import json


def get_database_location():
    home = str(pathilib.Path.home())
    return home

def get_User_config_path():
    home = get_database_location()
    datapath = os.path.join(home , '.textify')
    config_path = os.path.join(datapath, "user.json")
    return config_path

def get_database_path():
    home = get_database_path()
    datapath = os.path.join(home, '.textify')
    database_path = os.path.join(datapath, "database.json")
    return database_path

def Get_ID():
    with open(get_User_config_path()) as f:
        data = json.load(f)
        print(data)

def SetID(config):
    Checkfolder()
    with open(get_User_config_path(), 'w') as json_file:
        json.dump(config, json_file)

def GetDatabase():
    Checkfolder()
    with open(get_database_path()) as f:
        data = json.load(f)
        print(data)

def SetDatabase(User_data):
    Checkfolder()
    with open(get_database_path(), 'w') as json_file:
        json.dump(User_data, json_file)

    
def Checkfolder():
    check = os.path.isFile(get_database_location())
    if check == False:
        os.mkdir(get_database_location())