# CodeLeap API

A RESTful API built with Django REST Framework for managing blog posts.

## Table of Contents
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
- [Endpoints](#endpoints)
  - [List Posts](#list-posts)
  - [Create a Post](#create-a-post)
  - [Get a Single Post](#get-a-single-post)
  - [Update a Post](#update-a-post)
  - [Delete a Post](#delete-a-post)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ErickBonruque/codeleap-challenge.git
cd codeleap/api
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

## Running the Project

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the API at [http://localhost:8000/api/](http://localhost:8000/api/)
3. View API documentation at [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

## API Documentation

The API is fully documented using Swagger and ReDoc:
- Swagger UI: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- ReDoc: [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)

## Endpoints

### List Posts

**Endpoint:** `GET /api/posts/`

**Description:** Retrieve a paginated list of all posts.

**Query Parameters:**
- `page`: Page number for pagination
- `username`: Filter posts by username
- `title`: Filter posts by title
- `search`: Search in title, content, and username
- `ordering`: Order results (e.g., `-created_datetime` for newest first)

**Example Response:**
```json
{
  "count": 10,
  "next": "http://localhost:8000/api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "johndoe",
      "created_datetime": "2023-05-15T10:30:00Z",
      "title": "Hello World",
      "content": "This is my first post!"
    },
    {
      "id": 2,
      "username": "alice",
      "created_datetime": "2023-05-15T11:45:00Z",
      "title": "Django REST Framework Tutorial",
      "content": "Learn how to build APIs with Django REST Framework..."
    }
  ]
}
```

### Create a Post

**Endpoint:** `POST /api/posts/`

**Description:** Create a new post.

**Request Body:**
```json
{
  "username": "johndoe",
  "title": "My New Post",
  "content": "This is the content of my new post."
}
```

**Example Response:**
```json
{
  "id": 3,
  "username": "johndoe",
  "created_datetime": "2023-05-15T14:22:10Z",
  "title": "My New Post",
  "content": "This is the content of my new post."
}
```

### Get a Single Post

**Endpoint:** `GET /api/posts/{id}/`

**Description:** Retrieve a specific post by ID.

**Example Response:**
```json
{
  "id": 1,
  "username": "johndoe",
  "created_datetime": "2023-05-15T10:30:00Z",
  "title": "Hello World",
  "content": "This is my first post!"
}
```

### Update a Post

**Endpoint:** `PATCH /api/posts/{id}/` or `PUT /api/posts/{id}/`

**Description:** Update an existing post. Use `PATCH` for partial updates and `PUT` for full updates.

**Request Body (PATCH example):**
```json
{
  "title": "Updated Title",
  "content": "This content has been updated"
}
```

**Example Response:**
```json
{
  "id": 1,
  "username": "johndoe",
  "created_datetime": "2023-05-15T10:30:00Z",
  "title": "Updated Title",
  "content": "This content has been updated"
}
```

### Delete a Post

**Endpoint:** `DELETE /api/posts/{id}/`

**Description:** Delete a specific post.

**Response:** HTTP 204 No Content (successful deletion)

## Error Handling

The API returns standard HTTP status codes:
- `200 OK`: Request succeeded
- `201 Created`: Resource created successfully
- `204 No Content`: Resource deleted successfully
- `400 Bad Request`: Invalid request or validation error
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error
