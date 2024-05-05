import json



def saveGameToFile(game, saveFolder, saveName):
    infos = game.getGameProperties()

    with open(saveFolder + '/' +  saveName  + ".sav" , 'w', encoding ='utf8') as json_file: 
        json.dump(infos, json_file, ensure_ascii = False) 


def loadGamePropertiesFromFile(saveFolder, saveName) -> dict:
    try:
        with open(saveFolder + "/" + saveName + ".sav") as f:
            return json.load(f)
            
    except:
        return None
        