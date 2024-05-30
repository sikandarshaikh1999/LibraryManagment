# LibraryManagment
Description
The Library Management System is a Python-based application designed to manage the operations of a library. It allows users to add books and members, borrow and return books, and view the current inventory of books, members, and borrow records. The system uses a MySQL database to store and manage data

sql:
#create database
CREATE DATABASE library_db;

#in that database create table books

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    year_published INT
);
