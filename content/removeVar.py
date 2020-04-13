import json, os

class RemoveVar():
    def __init__(self,vars,toDel):
        self.vars = vars
        self.toDel = toDel
        self.type = None

    def now(self):
        if self.isValid()[0] == False:
            raise ValueError("[GlobalVars] Error trying to delete, key(%s) is not a list or a string"
                                %(self.toDel))
        if self.alreadyExist()[0] == False:
            raise ValueError("[GlobalVars] Error trying to delete, key(%s) doesn't exist"
                                %(self.alreadyExist()[1]))
        print("Recebeu o tipo",self.type)
        if self.type=="list": return self.deleteList()
        if self.type=="str" : return self.deleteString()
        

    def deleteList(self):
        for item in self.toDel:
            del self.vars[item]
        return self.vars

    def deleteString(self):
        del self.vars[self.toDel]
        return self.vars

    def isValid(self):
        if isinstance(self.toDel, str):
            self.type = "str"
            return [True,"str"]
        if isinstance(self.toDel,list):
            self.type = "list"
            return [True,"list"]
        return [False, None]

    def alreadyExist(self):
        if self.type == "list":
            for item in self.toDel:
                if item not in json.loads(os.getenv('GlobalVars')):
                    return [False, item]
        if self.type == "str":
            if self.toDel not in json.loads(os.getenv('GlobalVars')):
                return [False, item]
        return [True]
                
        

if __name__ == '__main__':
    myDict = {"teste":10,"oi":"hi"}
    os.environ["GlobalVars"] = json.dumps(myDict)

    a = RemoveVar(myDict,"oi")
    myDict = a.now()
    print(myDict)