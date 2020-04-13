import os, json
class SetVar(object):
    # Atributos Declarados
    toSet = None

    #Inicializador
    def __init__(self, toSet):
         self.toSet = toSet

    # ---------------- Public Methods ----------------
    def now(self):
        if self.isValid(self.toSet):   
            return self.toSet
        else:
            raise ValueError('[GlobalVars] Unknow error as isValid if')

    # ---------------- Private Methods ----------------

    def isValid(self,toCheck):
        if not self.isDict(toCheck):
            raise ValueError('[GlobalVars] Received not a dictionary')
        if self.alreadyExist(toCheck):
            raise ValueError('[GlobalVars] Received key already exists ')
        return True

    # Checa se o parametro recebido é um dicionario
    def isDict(self,toCheck):
        if isinstance(toCheck,dict):
            return True
        else:
            return False
    # Checa se o parametro já foi usado
    def alreadyExist(self,toCheck):
        if json.loads(os.getenv('GlobalVars')) != None:
            for item in toCheck:
                if item in json.loads(os.getenv('GlobalVars')):
                    return True
                else:
                    return False
        else:
            return False

if __name__ == "__main__":
    os.environ["GlobalVars"] = json.dumps({"hey":"hey"})
    a = SetVar({"oi":"oi"}).set()
    print(a)