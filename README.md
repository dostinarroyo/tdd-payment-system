Sistema de Procesamiento de Pagos usando TDD
Descripción

Este proyecto implementa un sistema básico de procesamiento de pagos aplicando la metodología Test Driven Development (TDD).

Funcionalidades
Cálculo de impuestos.
Validación de montos negativos.
Restricción de límite diario de pagos.
Herramientas utilizadas
Python 3
Pytest
Visual Studio Code
GitHub
Ciclo TDD aplicado
Fase Roja

Se implementaron pruebas que inicialmente fallaron debido a la ausencia de funcionalidad.

Fase Verde

Se desarrolló el código mínimo necesario para aprobar las pruebas.

Refactorización

Se mejoró la estructura del código mediante constantes y validaciones, manteniendo todas las pruebas exitosas.

Ejecución
pip install -r requirements.txt
pytest -v
