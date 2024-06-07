INSTRUCTIONS:

  Start the application by running the following command:

  docker-compose up

  -Postman collections are added (v2 and v2.1), it can be used to test the API.

  Request must be fetched from:
  
  http://localhost

Allowed currencies:
'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 
'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 
'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 
'CLF', 'CLP', 'CNY', 'CNH', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK',
'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 
'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 
'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 
'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 
'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL',
'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 
'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 
'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 
'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 
'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL',
'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 
'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VES', 'VND', 'VUV', 'WST', 'XAF', 
'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW',
'ZWL'

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Top 5 características de arquitectura del diseño actual del proyecto

Monolítico:
  La aplicación se ejecuta como una única unidad que incluye todas las funcionalidades y componentes necesarios. Esto facilita el desarrollo y despliegue inicial ya que no hay necesidad de coordinar múltiples servicios.

Acoplamiento estrecho: 
  Los componentes del sistema están fuertemente integrados entre sí, lo que puede hacer que los cambios en una parte del sistema requieran cambios en otras partes. Esto puede hacer que el desarrollo sea más rápido al principio, pero puede complicar el mantenimiento a largo plazo.

Base de datos única:
  Todos los datos se almacenan en una sola base de datos, lo que simplifica el acceso y la gestión de datos. Esto también puede resultar en un rendimiento eficiente para operaciones que requieren acceso a múltiples tablas y relaciones complejas.

Escalabilidad vertical:
  El enfoque principal para mejorar el rendimiento es mediante la adición de recursos (CPU, RAM) al servidor existente. Esto es más sencillo de implementar inicialmente, pero tiene un límite físico y puede volverse costoso.

Implementación y despliegue centralizado:
  Un solo artefacto de implementación contiene toda la lógica de la aplicación, lo que facilita el despliegue y la gestión de versiones. Esto simplifica el proceso de despliegue pero puede resultar en tiempos de inactividad más largos durante las actualizaciones.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Top 5 características de arquitectura en una migración a microservicios

Desacoplamiento:
  Los microservicios están diseñados para ser autónomos y tener un acoplamiento bajo, lo que permite desarrollar, desplegar y escalar servicios de manera independiente. Esto mejora la flexibilidad y reduce el impacto de los cambios en el sistema.

Base de datos descentralizada:
  Cada microservicio puede tener su propia base de datos, lo que permite una mayor flexibilidad en la elección de tecnologías y una mejor autonomía de los servicios. Esto también puede mejorar el rendimiento y la escalabilidad, aunque puede complicar la gestión de transacciones y consistencia de datos.

Escalabilidad horizontal: 
  Los microservicios pueden escalarse de manera independiente agregando más instancias del servicio específico que necesita más capacidad. Esto permite un uso más eficiente de los recursos y una mejor capacidad de respuesta a aumentos en la carga.

Implementación continua y despliegue continuo (CI/CD):
  Las prácticas de CI/CD son esenciales en una arquitectura de microservicios para manejar la frecuencia de cambios y despliegues. Esto permite una integración y entrega más rápidas, reduciendo el tiempo de lanzamiento de nuevas funcionalidades y correcciones.

Tolerancia a fallos y recuperación rápida:
  Los microservicios están diseñados para ser resistentes a fallos. Si un servicio falla, el resto del sistema puede continuar funcionando. Además, se pueden implementar estrategias de recuperación rápida y mecanismos de autoescalado para mejorar la disponibilidad y la resiliencia del sistema.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------