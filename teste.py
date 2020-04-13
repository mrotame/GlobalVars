from globalVars import GlobalVars

globalVars = GlobalVars()
globalVars.setVar({"teste":32,"açucar":22})
#globalVars.setVar("teste")
print(globalVars.getVar("teste"))
globalVars.updateVar({"teste":10})
print(globalVars.allVars)
globalVars.removeVar("teste")
print(globalVars.allVars)