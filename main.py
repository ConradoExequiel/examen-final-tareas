from tarea import Tarea
from gestor import GestorTareas

# Crear instancia del gestor
gestor = GestorTareas()

# Crear tareas
t1 = Tarea("Estudiar para el examen", "2025-07-25")
t2 = Tarea("Entregar informe final", "2025-07-28")

# Agregar tareas al gestor
gestor.agregar_tarea(t1)
gestor.agregar_tarea(t2)

# Listar todas las tareas
gestor.listar_todas_tareas()

# Marcar una tarea como completada
t1.marcar_completada()

# Verificar estado
print(f"¿Está pendiente t1? {t1.esta_pendiente()}")
