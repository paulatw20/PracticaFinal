from enum import auto
from strenum import StrEnum
class EnumDep(StrEnum):
    TESORERIA = auto()
    FINANCIERO = auto()
    COMPRAS = auto()
    VENTAS = auto()
    DISEÑO = auto()

class clasePersona():
    def __init__(self, nombre, edad):
        self.Nombre = nombre
        self.Edad = edad

    def getVals(self):
        return (str(self.Nombre + " " + str(self.Edad)))

class claseTrabajador():
    def __init__(self, codigo, salario):
        self.Codigo = codigo
        self.Salario = salario

    def getVals(self):
        return (str(self.Codigo + " " + str(self.Salario)))
class persYTra(clasePersona, claseTrabajador):
    def __init__(self, nombre, edad, codigo, salario, dep):
        self.Persona = clasePersona(nombre, edad)
        self.Trabajador = claseTrabajador(codigo, salario)
        self.Dep = EnumDep(dep)
    def getVals2(self):
        # return(str(self.Nombre + " " + str(self.Edad)+ " " + self.Codigo + " " + str(self.Salario)))
        return self.Persona.getVals() + self.Trabajador.getVals() + " " + self.Dep