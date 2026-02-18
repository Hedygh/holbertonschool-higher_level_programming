# RESTful API — Consuming and Processing Data with Python

## 📌 Project Overview

This project focuses on consuming data from a public REST API using Python and processing the retrieved data.

The objective is to understand how to:
- Send HTTP requests using the `requests` library
- Handle HTTP responses and status codes
- Parse JSON data into Python objects
- Transform structured data
- Export processed data into CSV format

The public API used for experimentation is:

https://jsonplaceholder.typicode.com/

---

## 🎯 Objectives

By completing this project, we learn how to:

- Use `requests.get()` to perform HTTP GET requests
- Check and interpret HTTP status codes
- Convert JSON responses into Python data structures
- Iterate over lists of dictionaries
- Extract specific fields from structured data
- Write structured data into a CSV file using Python’s `csv` module

---

## 🧩 Project Tasks

### 1️⃣ Fetch and Print Posts

- Send a GET request to `/posts`
- Print the response status code
- If the request is successful (`200`):
  - Parse the JSON response
  - Print the title of each post

---

### 2️⃣ Fetch and Save Posts to CSV

- Send a GET request to `/posts`
- If the request is successful:
  - Extract `id`, `title`, and `body` from each post
  - Store the selected data in a list of dictionaries
  - Write the data into a `posts.csv` file
  - Include a header row (`id,title,body`)

---

## 🛠 Technologies Used

- Python 3
- requests library
- csv module (built-in)
- JSONPlaceholder (test API)

---

## 🧠 Key Concepts

- HTTP requests and responses
- Status codes (200 OK)
- JSON parsing
- Python lists and dictionaries
- Data transformation
- CSV file generation

---

## 🚀 Outcome

At the end of this project, we are able to:

- Consume data from an external API using Python
- Safely process HTTP responses
- Convert JSON data into usable Python structures
- Export structured data into a CSV format

This project serves as a foundation for building and testing backend APIs in future applications.
