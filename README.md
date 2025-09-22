# 🚀 Pipeline CI/CD con Jenkins, Docker y Flask

Este repositorio contiene un **pipeline completo de Integración y Entrega Continua (CI/CD)** implementado en **Jenkins** para una aplicación web desarrollada con **Flask (Python)**.  

---

## 🛠️ Tecnologías
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins)
![Linux](https://img.shields.io/badge/Linux-VPS-FCC624?logo=linux)

---

## 🔄 Flujo del pipeline
1. 📥 **Clonado del repositorio** desde GitHub mediante Jenkins.  
2. 📦 **Instalación de dependencias** en contenedor *Python 3.9 Alpine*.  
3. ✅ **Ejecución de pruebas automatizadas** con *pytest*.  
4. 🐳 **Construcción de la imagen Docker** de la aplicación Flask.  
5. 📤 **Publicación en Docker Hub** para distribución.  
6. 🔐 **Conexión SSH segura al VPS Linux**.  
7. 🌐 **Despliegue remoto** con *docker-compose* y reinicio controlado.  
8. 📧 **Notificación por correo** al finalizar la ejecución.  

---

## ▶️ Ejecución local

```bash
git clone https://github.com/joseantoniocgonzalez/jenkinjose
cd jenkinjose
docker-compose up --build -d

