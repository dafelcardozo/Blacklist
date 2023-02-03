# trebu-blacklist
Este proyecto contiene el código fuente y las instrucciones de uso que constituyen mi solución a la prueba técnica .



El código fuente consiste en una aplicación Python y FastAPI, que implementan un API de micro-servicio de Blacklist.

Se implementan dos endpoints: 

curl -X POST -H "Content-Type: application/json" -d '{"email": "micorreo@sitio.com", "reason": "Fue grosero", "game_id": 435345}'  http://127.0.0.1:8000/blacklist/

curl /blacklist/check/

Arquitectura y despliegue

Esta micro-API está desplegada en la nube de AWS, en esta URL: 

A continuación, describo varios detalles de implementación:

- la base de datos es una PostgreSQL en RDS (Relational Database Service). Si bien durante la escritura inicial de la aplicación, esta se encontraba abierta hacia el público, 
ya no es el caso.

![image](https://user-images.githubusercontent.com/13710571/216707594-8d48c5fa-7e5c-42d4-8db6-0adc8e549afb.png)


Descripción de arquitectura en AWS

- el micro-API es una aplicación FastAPI y Python 9, y es desplegada en AWS como una función de Lambda.
- se utiliza un 'gestor de secretos' o Secrets Manager, para conservar de manera segura en AWS la cadena de conexión (host, usuario y contraseña de la BD).

![image](https://user-images.githubusercontent.com/13710571/216703102-1d29a5d3-ced3-4814-a9d9-95fbc8e4a69a.png)

- Documentación con Swagger y pruebas uniarias del API:


Descripción de red

![image](https://user-images.githubusercontent.com/13710571/216705239-fc0f79ac-be82-47e7-a65f-c557f93b40bd.png)



Se configuraron reglas de VPC para la comunicación segmentada y segura entre la Función Lambda y la base de datos en RDS.

![image](https://user-images.githubusercontent.com/13710571/216713041-ff705aba-c549-417a-8fb1-e4a6613abcba.png)

El micro servicio está sin embargo expuesto al público a tavés de un API Gateway

