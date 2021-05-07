#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Human:
    
    def __init__(self,name):
        self.name = name
    
    def nombre(self):
        return self.name
        
    def trabajador(self):
        return False

class Mayor(Human):
    
    def trabajador(self):
        return True


# In[7]:


Persona1 = Human('Victor')
Persona2 = Mayor('Felipe')

print(Persona1.nombre(), Persona1.trabajador())
print(Persona2.nombre(), Persona2.trabajador())


# In[23]:


class Animal():
    
    def __init__(self,patas,cola, ojos):
        self.patas = patas
        self.cola = cola
        self.ojos = ojos
    
    def tiene_patas(self): #Inheritance
        return self.patas
    
    def tiene_cola(self):
        return 'Este animal no tiene cola'
            
class Cat(Animal):
    
    def tiene_cola(self):
        return 'Este animal tiene cola'


# In[24]:


araña = Animal(8,False,8)
print(araña.tiene_cola())
print(araña.tiene_patas())

gato = Cat(4,True,2)
print(gato.tiene_cola())
print(gato.tiene_patas())


# In[ ]:


class Father:

    def __init__(self, name):
        self.father_name = name

class Mother:

    def __init__(self, name):
        self.mother_name = name

class Son(Father, Mother):

    def __init__(self, name, father_name, mother_name):
        self.name = name
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)

    def sexo(self, sexo):
        self.sexo = sexo

    def presentacion(self):
        if self.sexo == "M":
            return '{} es hijo de {} y {}'.format(son.name, son.father_name, son.mother_name)
        else:
            return '{} es hija de {} y {}'.format(son.name, son.father_name, son.mother_name)

son = Son('Amalia', 'Víctor', 'Estefa')
son.sexo('F')

print(son.presentacion())

