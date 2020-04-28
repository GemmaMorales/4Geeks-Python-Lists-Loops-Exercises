people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
#def deletePerson(person_name):
    #for x in people:
        #if x == person_name:
            #people.remove(x)
    #return people

def deletePerson(person_name):
    new_list = []
    for x in people:
        if x != person_name:
            new_list.append(x)
    return new_list
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))