#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property  # Getter: Permite encapsular completamente el atributo protegido/privado
    def nombre(self):
        return self._nombre

    @nombre.setter  # Setter: No es necesario poner el atributo en under or dunder, solo el nombre del atributo
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalles(self):
        print(f'la Persona: {self._nombre} {self._apellido}, tiene {self._edad} años')

        
if __name__ == '__main__': #Permite que imprima esto solo cuando el objeto sea ejecutado desde el módulo principal
    persona1 = Persona('Victor', 'Agudelo', 30)
    print(persona1.nombre)  # No será necesario get_nombre() porque el decorador permite utilizarlo sin parentésis
    persona1.mostrar_detalles()

    persona1.nombre = 'Andrés'
    print(persona1.nombre) # Al igual que en el getter, no es necesario utilizar () por el decorador que utilizamos en el método
    persona1.mostrar_detalles()

    persona1.apellido = 'Bustamante' #Permite setear un nuevo nombre de manera indirecta
    print(persona1.apellido)
    persona1.mostrar_detalles()

    persona1.edad = 26
    print(persona1.edad)
    persona1.mostrar_detalles()


# In[ ]:




