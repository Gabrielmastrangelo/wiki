# Wikipedia-like Encyclopedia

## Overview

This project is a Django-based encyclopedia application that allows users to view, search, create, and edit entries. Entries are stored in Markdown format and rendered as HTML.

## Features

- **View Entries**: Display Markdown content converted to HTML.
- **Index Page**: List and navigate all entries.
- **Search**: Find entries by title or keyword.
- **Create/Edit**: Add and modify entries using Markdown.
- **Random Page**: Access a random entry.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:8000`.

## Requirements

- Python 3.x
- Django
- markdown2 (for Markdown to HTML conversion)
