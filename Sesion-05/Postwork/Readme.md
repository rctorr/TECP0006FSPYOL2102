
## Postwork 5

### OBJETIVO

- Reforzar los aprendizajes de la sesión 5 y  aplicarlos al proyecto final. Herencia, polimorfismo, decoradores y control de excepciones.
#### REQUISITOS

1. Python 3

#### DESARROLLO

1. Crea la clase `Tarjeta_de_servicios` en un nuevo módulo con lo siguiente:
   1. Heredará desde `Tarjeta`: Una tarjeta de servicios es un tipo especial de tarjeta
   2. Solamente permite realizar pagos totales de la deuda
   3. No aplica una tasa de interes sobre saldos remanentes ya que son cero
   4. Sobrecarga los métodos necesarios para solo permitir pagos totales
   5. Usa try y except para evitar que un usuario introduzca argumentos no validos en el método crea_tarjeta

Ejemplo de operaciones realizadas con una Tarjeta de servicios:
```
python pago-tarjeta.py 
Nombre de la tarjeta: Comer
Escribe el monto de la deuda actual de la tarjeta: 1000.0
Escribe el monto del pago a realizar (sólo se hacepta un pago igual a la deuda): 0
Escribe el monto total de los nuevos cargos: 150.0


----------------------------------------
--------- Tarjeta de servicios ---------
----------------------------------------
Tarjeta:   Comer
----------------------------------------
Deuda actual:             1000.00
Monto del pago:              0.00
----------------------------------------
Deuda recalculada:        1000.00
Nuevos cargos del mes:     150.00
----------------------------------------
Nueva deuda del mes:      1150.00

Escribe la cantidad del pago: 0
Sólo es posible realizar un pago igual a la deuda actual!

Escribe la cantidad del pago: 1000.0


----------------------------------------
--------- Tarjeta de servicios ---------
----------------------------------------
Tarjeta:   Comer
----------------------------------------
Deuda actual:             1000.00
Monto del pago:           1000.00
----------------------------------------
Deuda recalculada:           0.00
Nuevos cargos del mes:     150.00
----------------------------------------
Nueva deuda del mes:       150.00

```



