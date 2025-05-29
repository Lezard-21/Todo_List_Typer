# Gestor de Tareas CLI

Un script Python para gestionar tareas desde la terminal usando Typer y Rich.

## Funcionalidades

- ✅ **Crear** nuevas tareas
- 📝 **Listar** todas las tareas en formato tabla
- ✔️ **Marcar/desmarcar** tareas como completadas  
- ❌ **Eliminar** tareas existentes
- 🔄 **Resetear** toda la lista (con confirmación)

## Instalación

```bash
pip install typer rich
```

## Ejemplo de uso
#### Crear tareas
```bash
python script.py create
```

#### Listar tareas
```bash
python script.py list
```

#### Marcar/desmarcar tarea
```bash
python script.py check
```

#### Eliminar tarea
```bash
python script.py delete
```

#### Resetear lista
```bash
python script.py reset
```


## Estructura de Datos

Las tareas se guardan en todo.md como JSON, una por línea:
```json
{"index": 1, "task": "Ejemplo", "state": false}
```

## Características
1.Índices automáticos
2.Persistencia en archivo
3.Interfaz con colores y emojis
4.Confirmaciones para acciones críticas

##### Nota: El script crea automáticamente el archivo todo.md si no existe
