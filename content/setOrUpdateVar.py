# ---------------- Imports ----------------

import os, json

# ---------------- Classe ----------------
# Descrição da classe
class SetOrUpdateVar():

    # Inicializador
    def __init__(self, toSet):
        self.toSet = toSet

    # ---------------- Public Methods ----------------
    # Seta ou atualiza a variavel
    def now(self):
        if not self.isDict():
            raise ValueError("[GlobalVars] Error trying to 'set or update', key(%s) is not a dictionary"
                                %(self.toSet))

        a = json.loads(os.getenv("GlobalVars"))
        a.update(self.toSet)
        return a


    # Descrição
    # ---------------- Private Methods ----------------
    def isDict(self):
        if isinstance(self.toSet, dict):
            return True
        return False



# ---------------- Test ----------------
if (__name__ == '__main__'):
     a = SetOrUpdateVar({"teste":"oi"})
     a.now()