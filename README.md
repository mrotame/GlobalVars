# GlobalVars
 A way to implement global vars between classes using the environment variable "os.environ"

## Importing
``` 
from globalVars import GlobalVars;
gv = GlobalVars()
```

## Methods
This class has five classes to be used:

* setVar
	* Description: Set a new variable
	* Params: Accepts a `Dictionary` with `'Name':Value` containing one or more vars to add 
* getVar
	* Description: Get a setted variable
	* Params: Accepts a `String` with `'Name'` containing the name of a var
* removeVar 
	* Description: Remove a variable
	* Params: accepts a `String`with `'Name'` or a `List` with "[Name1,Name2,...] containing one or more names of vars to remove
* updateVar
	* Description: Update a variable
	* Params: accepts a `Dictionary` with `{'Name':Value,...}` containing one or more vars to update
* setOrUpdateVar
	* Description: set a new variable or update it if already exists
	* Params: accepts a `Dictionary` with `{'Name':Value,...}` containing one or more vars to set or update


### Methods Examples

### setVar
```
GlobalVars.setVar({"foo":"bar","eggs":16}) # Will be setted two vars: "foo" with value "bar" and "eggs" with value 16
GlobalVars.setVar({"foo":"bar"}) # The "foo" var will be setted with a "bar" value
```

### getVar
```
result = GlobalVars.get("foo") # Result var will be the value in "foo"
result = GlobalVars.get(["foo","bars","eggs"]) # Result var will be a list containing the result of all the three vars
```

### removeVar
```
GlobalVars.removeVar("foo") # Var "foo" will be removed
GlobalVars.removeVar(["foo","bar","eggs"]) # All the three vars ("foo", "bar" and "eggs") will be removed
```

### updateVar
```
GlobalVars.updateVar({"foo":"bar"}) # Variable foo will be updated with the new value "bar"
GlobalVars.updateVar({"foo":"bar","eggs":16}) # The two variables ("foo" and "eggs") will be updated with new values
```

### setOrUpdateVar
```
GlobalVars.setOrUpdater({"foo":"bar"}) # The var "foo" will set if not exist, or will update with a new value if already exist a var with "foo" name
GlobalVars.setOrUpdateVar({"foo":"bar","eggs":16}) # Two vars will be setted (if not exist) or their values will be updated (if they already exist)

```
