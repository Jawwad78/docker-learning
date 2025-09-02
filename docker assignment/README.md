# 🐳 Flask + Redis + NGINX : Multi Container Project

This project is a production style multicontainer system built with Flask, Redis, and Nginx.  

It demonstrates core DevOps concepts in action: containerization, scaling, and load balancing; all orchestrated with Docker Compose.

---

## 🖼️ Demo
![Demo](demo.gif)
- `/` → Welcome page  
- `/count` → Visitor counter (stored in Redis)

---

## 🧭 Architecture
- **NGINX** → listens on port `5002` and load balances traffic  
- **Flask** → 3 replicas behind NGINX  
- **Redis** → key-value store for visit counts, persisted with a Docker volume  

---

## 🚀 Features
- Flask app with `/` and `/count` routes  
- Redis persistence with volumes  
- Environment variables for host/port  
- Multi stage Dockerfile for slimmer images  
- NGINX reverse proxy + load balancing across replicas  

---

## ⚡ Struggles & Debugging
- At first I was trying to use `dotenv` for environment variables, but then I realised Docker Compose already passes them in, so it wasn’t needed.
- Broke Nginx multiple times with misplaced `{}` braces before understanding the config structure.  
- Learned how to scale multiple Flask containers properly with `docker compose up --scale web=3` so Nginx could load balance across them.  
- Got mixed up between `docker stop`, `docker compose down`, and `docker compose down -v`, but figured out how each one affects containers, networks, and volumes (and when Redis data gets wiped).   

---

## 📚 What I Learned
- Things like env vars, persistence, scaling, and load balancing don’t just happen automatically, you have to set them up yourself.  
- I realised fixing and debugging configs is just as important as writing them.  
- I’m starting to think more in terms of separate services instead of one big app, which is the DevOps way of working.  
 
