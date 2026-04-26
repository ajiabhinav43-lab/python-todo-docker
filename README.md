\# 📝 Flask To-Do App with Docker



\## 📌 Project Overview



This project is a simple \*\*To-Do List Web Application\*\* built using \*\*Flask (Python)\*\* and containerized using \*\*Docker\*\*.

It allows users to add, mark, and delete tasks through a web interface.



\---



\## 🚀 Features



\* ➕ Add new tasks

\* ✅ Mark tasks as complete / incomplete

\* ❌ Delete tasks

\* 🌐 Accessible via browser

\* 🐳 Fully containerized using Docker



\---



\## 🛠️ Technologies Used



\* Python

\* Flask

\* Docker

\* Docker Compose



\---



\## 📂 Project Structure



```

.

├── app.py

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

└── README.md

```



\---



\## ⚙️ Setup \& Installation



\### 🔹 1. Clone the Repository



```

git clone https://github.com/ajiabhinav43-lab/python-todo-docker.git

cd python-todo-docker

```



\---



\### 🔹 2. Run the Application using Docker



```

docker compose up --build

```



\---



\### 🔹 3. Access the Application



Open your browser and go to:



```

http://localhost:5000

```



\---



\## 🧪 How to Use



1\. Enter a task in the input box

2\. Click \*\*Add\*\*

3\. Use:



&#x20;  \* \*\*Toggle Complete\*\* to mark done/undone

&#x20;  \* \*\*Delete\*\* to remove a task



\---



\## ⚠️ Notes



\* This app uses Flask's development server (not for production use)

\* Data is stored temporarily (resets when container restarts)



\---



\## 📦 Future Improvements



\* Add database (SQLite / MySQL)

\* Improve UI with HTML/CSS

\* Add user authentication

\* Deploy to cloud



\---



\## 👨‍💻 Author



\*\*Abhinav Aji\*\*



\---



\## 📄 License



This project is for educational purposes.



