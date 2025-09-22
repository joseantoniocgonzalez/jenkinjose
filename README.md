Este repositorio contiene un pipeline completo de Integración y Entrega Continua (CI/CD) implementado con Jenkins para una aplicación web desarrollada en Flask (Python).

El flujo de trabajo automatizado incluye las siguientes fases:

Clonado del repositorio desde GitHub mediante Jenkins.

Instalación de dependencias dentro de un contenedor ligero basado en Python 3.9 Alpine.

Ejecución de pruebas automatizadas con pytest para validar el correcto funcionamiento de la aplicación.

Construcción de la imagen Docker de la aplicación Flask a partir del Dockerfile.

Publicación de la imagen en Docker Hub, asegurando su disponibilidad para despliegues posteriores.

Conexión segura al VPS Linux mediante credenciales SSH gestionadas en Jenkins.

Despliegue remoto en el servidor utilizando docker-compose, con levantado automático del contenedor y reinicio controlado de la aplicación.

Notificación por correo electrónico al finalizar el pipeline con el estado de la ejecución.

Este proyecto demuestra un escenario real de automatización DevOps, integrando pruebas, construcción, distribución y despliegue en un solo flujo, y aplicando buenas prácticas de seguridad en la gestión de credenciales y despliegues.
