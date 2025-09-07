# Calculadora - Proyecto de Prueba para GitHub Actions

Este es un proyecto de prueba para practicar con GitHub Actions (examen GH-200). Contiene una calculadora simple en Python con tests unitarios.

## Estructura del Proyecto

```
├── calculadora.py          # Clase principal de la calculadora
├── test_calculadora.py     # Tests unitarios con unittest
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Este archivo
```

## Funcionalidades

La calculadora incluye las siguientes operaciones:
- ✅ Suma
- ✅ Resta
- ✅ Multiplicación
- ✅ División (con control de división por cero)
- ✅ Potencia
- ✅ Raíz cuadrada (con control de números negativos)

## Uso

### Ejecutar la calculadora
```bash
python calculadora.py
```

### Ejecutar los tests
```bash
python -m unittest test_calculadora.py
```

### Ejecutar tests con pytest (si está instalado)
```bash
pytest test_calculadora.py -v
```

### Ejecutar tests con cobertura
```bash
pytest test_calculadora.py --cov=calculadora --cov-report=html
```

## GitHub Actions

Este proyecto está diseñado para practicar diferentes workflows de GitHub Actions:

- 🔄 CI/CD básico
- 🧪 Ejecución de tests automáticos
- 📊 Reportes de cobertura
- 🔍 Linting y formateo de código
- 🚀 Despliegue automático
- 📦 Creación de releases
- 🔒 Análisis de seguridad

## Instalación

1. Clona el repositorio
2. Instala las dependencias (opcional):
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta los tests para verificar que todo funciona:
   ```bash
   python -m unittest test_calculadora.py
   ```

## Contribución

Este es un proyecto de práctica para GitHub Actions. Siéntete libre de:
- Agregar más operaciones matemáticas
- Mejorar los tests existentes
- Experimentar con diferentes workflows de GitHub Actions