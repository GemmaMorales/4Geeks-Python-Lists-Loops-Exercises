people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #people.remove(person_name)
    #return people
    for x in people:
        if x == person_name:
            people.remove(x)
    return people
    
#print(deletePerson("daniella"))
#print(deletePerson("juan"))
print(deletePerson("emilio"))