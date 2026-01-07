


# 📇 Contact Book Application

**Industry-style beginner Python project using OOP & File Handling**

This project demonstrates how a real-world **Contact Management System** can be designed using **clean architecture**, **separation of concerns**, and **persistent storage**.

---

## 🏷️ Project Overview

The Contact Book application allows users to:

- Store contacts permanently
- Retrieve saved contacts
- Search contacts by name
- Delete existing contacts

All data is stored in a file, making the application **stateful across multiple executions**.

This project follows **industry-relevant coding practices**, making it suitable for beginners transitioning toward **professional backend development**.

---

## ✨ Key Features

- Object-Oriented Design (Single Responsibility Principle)
- Persistent storage using file handling
- Menu-driven CLI interface
- Clean and modular folder structure
- GitHub-ready documentation

---

## 🧩 Technologies Used

- **Language:** Python 3  
- **Concepts:** OOP, File Handling, CLI  
- **Storage:** Text file (`.txt`)

---

## 📁 Folder Structure (Industry-Style)

contact_book/
│
├── main.py # Application entry point
├── contact.py # Contact entity/model
├── contact_book.py # Business logic layer
├── file_manager.py # File handling & persistence
├── contacts.txt # Data storage
└── README.md # Project documentation


---

## 🧠 Architecture Explanation

This project follows a **layered architecture**, commonly used in real-world backend systems:

- **Model Layer** → `contact.py`  
  Handles data structure and entity representation.

- **Service / Logic Layer** → `contact_book.py`  
  Contains application business rules.

- **Persistence Layer** → `file_manager.py`  
  Manages file read/write operations.

- **Presentation Layer** → `main.py`  
  Handles user interaction via CLI.

This separation improves **maintainability, readability, and scalability**.

---

## ▶️ How to Run

```bash
python main.py


## 🎓 Learning Outcomes

- How to structure Python projects professionally
- Practical OOP implementation
- File-based persistence
- Clean separation of concerns

## 🚀 Possible Enhancements

- Replace text file with JSON
- Add update contact feature
- Implement input validation
- logging module

## 👤 Author

**Mamun Bepari**  
Aspiring Software Engineer  
Python Backend Developer -->