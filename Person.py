class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name 
        self._age = age

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
if __name__ == "__main__":
    id_test = 10
    name_test = "10"
    age_test = 10
    person = Person(id_test, name_test, age_test)
    if person.getId() != id_test:
        print("Error: the ID you got is " + str(person.getId()) + " but it should be " + str(id_test))
    if person.getName() != name_test:
        print("Error: the Name you got is " + str(person.getName()) + " but it should be " + str(name_test))
    if person.getAge() != age_test:
        print("Error: the Age you got is " + str(person.getAge()) + " but it should be " + str(age_test))