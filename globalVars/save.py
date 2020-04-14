import os, json

class Save(object):
    # ---------------- Inicializador Methods ----------------
    def __init__(self,toSave):
        os.environ['GlobalVars'] = json.dumps(toSave)