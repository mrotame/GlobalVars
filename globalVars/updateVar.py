# ---------------- Imports ----------------
import os, json

# ---------------- Classe ----------------
# Descrição da classe
class UpdateVar():

    # Inicializador
    def __init__(self,toUpdate):
        self.toUpdate = toUpdate

    # ---------------- Public Methods ----------------
    # V
    def now(self):
        if not self.isDict ():
            raise ValueError('[GlobalVars] Error trying to update, %s is not a dictionary'
                                %(self.toUpdate))

        if self.alreadyExist()[0] == False:
            raise ValueError("[GlobalVars] Error trying to update, key(%s) doesn't exist"
                                %(self.alreadyExist()[1]))
        a = json.loads(os.getenv("GlobalVars"))
        a.update(self.toUpdate)
        return a


    # ---------------- Private Methods ----------------
    # Verifica se já existe uma variavel para atualizar
    def alreadyExist(self):
        for item in self.toUpdate:
            if item not in json.loads(os.getenv('GlobalVars')):
                return [False, item]
        return [True]
    
     # Verifica se a variavel recebida é um dicionario
    def isDict(self):
        if isinstance(self.toUpdate, dict):
            return True
        else:
            return False

# ---------------- Test ----------------
if (__name__ == '__main__'):
    os.environ['GlobalVars'] = json.dumps({'hey':'hey'})
    a = UpdateVar([{"hey":"teste"}]).now()