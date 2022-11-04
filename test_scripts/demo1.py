from pyjavaproperties import Properties

#create object of Properties class
pfile=Properties()
#open the property file
pfile.load(open("../config.properties"))
v=pfile['city']
print(v)