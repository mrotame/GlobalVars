# GlobalVars
 A way to implement global vars between classes using the environment variable `"os.environ"`
 
### Last updates
* Added a function to clear all setted vars `clearAllVars` and `getAllVars`. See the new functionalities in methods and methods exemples
* Last update now adds dunders `setitem`, `getitem` and `len` making the class work as a dictionary.
see the funcionalities in methods exemples `setOrUpdateVar`, `getVar`, and `getAllVars`

## Importing
``` 
from globalVars import GlobalVars;
gv = GlobalVars()
```

## Methods
This class has five classes to be used:

* getAllVars
	* Description: return all vars setted in the environment
	* Params: no params needed
* clearAllVars
	* Description: Delete all vars already setted
	* Params: no params needed
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
*Remember that you imported `GlobalVars` as `"gv"`
### getAllVars()
```
# Store all already setted vars in a local variable
myVars = gv.getAllVars()

# Print all the environment setted vars
print(gv.getAllVars())

# If you want to now how many vars are setted you can use len()
len(gv)
```
### clearAllVars()
```
# Set a new var
gv.setVar({"test":"hello"})

# Clear all the vars setted
gv.clearAllVars()

# It will return an empty dictionary "{}"
gv.getAllVars()
```

#### setVar()
```
# Will be setted two vars: "foo" with value "bar" and "eggs" with value 16
gv.setVar({"foo":"bar","eggs":16}) 

# The "foo" var will be setted with a "bar" value
gv.setVar({"foo":"bar"}) 
```

#### getVar()
```
# Result var will be the value in "foo"
result = gv.get("foo") 

# Result var will be a list containing the result of all the three vars
result = gv.get(["foo","bars","eggs"]) 

# You can simply use gv as a dict to get the var
result = gv["foo"]
```

#### removeVar()
```
# Var "foo" will be removed
gv.removeVar("foo") 

# All the three vars ("foo", "bar" and "eggs") will be removed
gv.removeVar(["foo","bar","eggs"]) 
```

#### updateVar()
```
# Variable foo will be updated with the new value "bar"
gv.updateVar({"foo":"bar"}) 

# The two variables ("foo" and "eggs") will be updated with new values
gv.updateVar({"foo":"bar","eggs":16}) 
```

#### setOrUpdateVar()
```
# The var "foo" will set if not exist, or will update with a new value if already exist a var with "foo" name
gv.setOrUpdater({"foo":"bar"}) 

# Two vars will be setted (if not exist) or their values will be updated (if they already exist)
gv.setOrUpdateVar({"foo":"bar","eggs":16}) 

# You can use gv as a dict to add a new or update an existing var
gv["test"] = "Hello" 	      # setted a new one
gv["test"] "Oh, hey there"    # Update an existing one
```

