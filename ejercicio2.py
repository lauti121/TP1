


#reporte de rendimiento

def promedio_de_estudiantes(estudiantes):
    notas = estudiantes.get("notas", [])
    return sum(notas) / len(notas) if notas else 0

