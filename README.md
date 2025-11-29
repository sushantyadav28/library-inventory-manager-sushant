Name: Sushant

Roll No.: 2501350065

Course: B.Tech CSE (Full Stack Development)

Subject: Programming for Problem Solving using Python

Project Title: Library Inventory Manager


## Library Inventory Manager ##
A simple and modular Pyhton-based LIBRARY MANAGMENT SYSTEM that uses Object-Oriented-Programming (OOP) , JSON file handling , exception handling , and a menue driver to manage books in a library
## Project Overview ##
This project helps manage a small library book managment using a simple command-line interface.

It allows users to:

1. Add new books

2. Issue books

3. Return books

4. Search books by title or ISBN

5. View all books

6. Store and retrieve data using a JSON file
## Features ##
-> Book Management

Add new books with title, author, and ISBN

Store status as available or issued

-> Issue & Return System

Issue a book (if available)

Return a book (if issued)

-> Searching

Search by title

Search by ISBN

-> Persistent Storage

Books are stored in catalog.json

Automatically loads and saves changes

-> Logging

Logs all operations in library.log

-> Modular Design

/library_manager contains all core logic

main.py contains the user interface

-> Exception Handling

Handles missing/corrupted JSON files

Validates operations before issuing/returning books

