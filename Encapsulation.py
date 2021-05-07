#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Persona:

    def __init__(self, name, cellphone, id):
        self.name = name #Public data
        self._cellphone = cellphone #Protected data
        self.__id = id #Private data

    def print_name(self): #Public method
        return self.name

    def _print_cell(self): #protected method
        return self._cellphone

    def __print_id(self): #private method
        return self.__id

    def real_print(self): #public method
        return self.__print_id()

class OtraPersona(Persona):

    def __init__(self, name, cellphone, id):
        Persona.__init__(self, name, cellphone, id)


persona1 = Persona('Manuel', 3004504499, 1020446266)

print(persona1.print_name())
print(persona1._print_cell())

persona2 = OtraPersona('Felipe', 3214615186, 1020455465)

print(persona2.print_name())
print(persona2._print_cell())

print(persona1.real_print())
print(persona2.real_print())

