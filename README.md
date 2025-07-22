# 📌 Examen Final – Sistema de Gestión de Tareas

Este repositorio contiene la resolución del examen final de la materia **Base de Datos e Introducción a la Programación**. El caso de estudio plantea el desarrollo de un **sistema de gestión de tareas personales** en Python.

---

## ✅ Funcionalidades Implementadas

- ✅ Crear nuevas tareas con descripción y fecha límite.
- ✅ Marcar tareas como completadas.
- ✅ Listar todas las tareas.
- ✅ Control de estado de cada tarea (pendiente o completada).
- ✅ Gestión centralizada de tareas con `GestorTareas`.

---

## 🧩 Estructura del Proyecto

```bash
📁 Examen_Final_Gestor_Tareas
├── tarea.py       # Clase Tarea (modelo de una tarea individual)
├── gestor.py      # Clase GestorTareas (administrador de tareas)
├── main.py        # Código de prueba para crear, listar y completar tareas
├── README.txt     # Justificación breve según lo solicitado en el examen
└── README.md      # Este archivo: presentación del repositorio en GitHub
```

---

## 🛠️ Tecnologías Utilizadas

- Lenguaje: **Python 3**
- Estructuras de datos: **Listas**
- Programación orientada a objetos (POO)

---

## 📋 Justificación Técnica

1. **ID único por tarea:** Se usó un contador de clase para evitar que todas las tareas tengan el mismo ID.
2. **Encapsulamiento:** Se protegió el atributo `estado` para que no sea modificable directamente.
3. **Gestor de tareas:** Se implementó una clase gestora para centralizar la lógica de manejo.
4. **Persistencia opcional:** Se utilizó una lista (estructura en memoria) en lugar de una base de datos, tal como lo solicitaba el examen.



