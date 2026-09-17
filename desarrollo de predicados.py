
#universo

maestros = {
    "Juan": {
        "imparte": ["matematicas"], 
        "correo":"juan@gmail.com", 
        "telefono": "6461862823"
    },
    "Pepe": {
        "imparte": ["biologia"], 
        "correo": "pepe@gmail.com", 
        "telefono": "6461852823"
    },
    "Luis": {
        "imparte": ["fisica","programacion"], 
        "correo": "luis@gmail.com", 
        "telefono":"6461852828"
    }
}


materias = ["matematicas", "programacion", "biologia", "fisica"]

alumnos = {
    "Miguel": {
        "carrera": "ingenieria", 
        "calificacion":5, 
        "materia":"matematicas", 
        "num_control": 853782
    },
    "Angel": {
        "carrera": "administracion", 
        "calificacion": 6, 
        "materia": "programacion", 
        "num_control": 815589
    },
    "Andres": {
        "carrera": "psicologia", 
        "calificacion": 9, 
        "materia": "biologia", 
        "num_control": 716792
    },
    "Felipe": {
        "carrera": "ingenieria", 
        "calificacion": 8, 
        "materia": "fisica", 
        "num_control": 731799
    }
}


numeros_control = [853782, 815589, 716792, 731799]
correos = ["juan@gmail.com", "pepe@gmail.com","luis@gmail.com"]
telefonos = ["6461862823", "6461852823","6461852828"]
calificaciones = [5, 6, 7, 8, 9, 10]
carreras = ["ingenieria", "psicologia", "administracion"]


#predicados

def Alumno(x):
    return x in alumnos

def Carrera(x):
    return x in carreras

def Materia(x):
    return x in materias

def Maestro(x):
    return x in maestros

def Calificacion(x):
    return x in calificaciones

def Cursa(x,y):
    if x in alumnos and y in materias:
        return alumnos[x]["materia"] == y

    return False

def NumControlDe(x,y):
    if x in numeros_control and y in alumnos:
        return alumnos[y]["num_control"] == x

    return False


#consultas

print("miguel es un alumno:", Alumno("Miguel"))
print("Pepe es un alumno:", Alumno("Pepe"))

print("ingenieria es una carrera:", Carrera("ingenieria"))
print("programacion es una carrera:", Carrera("programacion"))


print("Pepe es un maestro:", Maestro("Pepe"))
print("Andres es un maestro:", Maestro("Andres"))

print("programacion es una materia:",Materia("programacion"))
print("administracion es una materia:",Materia("administracion"))


print("6 es una calificacion:",Calificacion(6))
print("11 es una calificacion:",Calificacion(11))

print("andres cursa biologia: ",Cursa("Andres", "biologia"))
print("Pepe cursa biologia: ",Cursa("Pepe", "biologia"))


print("716792 es el numero de control de andres:",NumControlDe(716792, "Andres"))
print("716792 es el numero de control de Pepe:",NumControlDe(716792, "Pepe"))