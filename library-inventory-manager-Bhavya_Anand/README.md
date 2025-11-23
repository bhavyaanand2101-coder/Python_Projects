
# Library Inventory Manager (Single File Version)

This project implements a simple command-line interface (CLI) based library inventory management system. It allows users to add, issue, return, view, and search for books. The inventory data is persistently stored in a JSON file named `books.json` in the same directory as the script.

## Features

*   **Book Management:** Add new books with title, author, ISBN, and status.
*   **Status Tracking:** Books can be marked as 'available' or 'issued'.
*   **Search Functionality:** Search for books by title (partial match) or ISBN.
*   **Persistent Storage:** All book data is saved to and loaded from a `books.json` file.
*   **User-Friendly CLI:** An interactive menu guides the user through various operations.
*   **Error Handling & Logging:** Robust error handling for file operations and invalid user inputs, with detailed logging.

## Setup and Installation

1.  **Save the file:** Save the provided Python code as `library_manager.py` in a directory of your choice.
2.  **Open a terminal/command prompt** and navigate to that directory.

## Usage

To run the application:

```bash
python library_manager.py
