#!/usr/bin/python3
class VerboseList(list):
    def append(self, element):
        super().append(element) #super() Llama al método append de la clase base list, que agrega elemen a la lista.
        print(f"Added [{element}] to the list.")
    
    def extend(self, element):
        super().extend(element)
        print(f"Extended the list with [{len(element)}] items.")
    
    def remove(self, element):
        super().remove(element)
        print(f"Removed [{element}] from the list.")
    
    def pop(self, element=-1):
        a = self[element]
        super().pop(element)
        print(f"Popped [{a}] from the list.")
