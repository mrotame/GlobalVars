import json, os
from globalVars import setVar, removeVar, load, save, updateVar, setOrUpdateVar

class GlobalVars():
    # Atributos declaradas
    allVars = None

    # Inicializador
    def __init__(self):  
        self.load()
        # Cria o variavel global se ela não existir
        if os.getenv('GlobalVars') == None:
            os.environ['GlobalVars'] = json.dumps({})
            self.load()

# ---------------- Public Methods ----------------
    def getAllVars(self):
        self.load()
        return self.allVars

    def clearAllVars(self):
        self.allVars = {}
        self.save(self.allVars)
        self.load()

    def setVar(self,toSet): # Adiciona uma variavel no dicionario
        self.load()
        self.save(setVar.SetVar(toSet).now())
        self.load()
        return True

    def removeVar(self,toDel): # Remove uma variavel do dicionario
        self.load()
        self.save(removeVar.RemoveVar(self.allVars,toDel).now())
        self.load()

    def updateVar(self,toUpdate):
        self.load()
        self.save(updateVar.UpdateVar(toUpdate).now())
        self.load()
        return True

    def setOrUpdateVar(self,toSet):
        self.load()
        self.save(setOrUpdateVar.SetOrUpdateVar(toSet).now())
        self.load()
    
    def getVar(self,item):
        self.load()
        return self.allVars[item]

    # ---------------- Private Methods ----------------
    def load(self): # Carrega a variavel do sistema
        self.allVars = load.Load().now()
        
    def save(self,toSave): # Salva a variavel no sistema 
        save.Save(toSave)

    # ---------------- Dunder Methods ----------------
    def __len__(self):
        self.load()
        return len(self.allVars)

    def __getitem__(self,item):
        self.load()
        return self.allVars[item]

    def __setitem__(self,key,item):
        self.load()
        self.allVars[key]=item
        self.save(self.allVars)
        self.load()

if __name__ == "__main__":

    a = GlobalVars()
    #print(a.allVars)
    toSave = {"oi":"oi",
            "teste":1522,
            "sim?":True}
    a.setVar(toSave)
    print(a.allVars)
    a.updateVar({"oi":"hello","teste":3032})

    a.setOrUpdateVar({"oi":"Falow vei","quitanda":"fornalha"})
    #a.setVar("teste")

    print(a.getVar("oi"))
    print(a.allVars)
    a.removeVar("teste")
    print(a.allVars)
    a.updateVar({"oi":"32"})
    print(a.allVars)
