# Real-Time Drawing Board - Backend

This repository contains the **backend code** for the **Real-Time Drawing Board**, a collaborative drawing platform. The backend is built with **Django** and **Django Channels** to enable real-time communication via WebSockets. It manages user interactions, drawing data, and synchronization across multiple clients.

---

## Features

- 🌐 **WebSocket Integration**: Real-time communication for seamless collaboration.
- 🚀 **Scalable Architecture**: Powered by Django Channels with Redis as the channel layer.
- 📡 **Efficient Messaging**: Handles high-frequency drawing data with low latency.
- 💾 **Stateless Backend**: Designed to handle multiple concurrent users efficiently.

---

## Technology Stack

- **Django**: A high-level Python web framework.
- **Django Channels**: Extends Django to handle asynchronous WebSocket connections.
- **Redis**: Used as the channel layer for WebSocket communication.
- **ASGI**: The asynchronous server gateway interface for handling WebSocket requests.

---

## Getting Started

### Prerequisites

- [Python 3.9+](https://www.python.org/)
- [Redis](https://redis.io/) (Ensure Redis is running on the system)

### Installation

Clone the repository:

```
git clone https://github.com/aringadre76/real-time-drawing-board-backend-deploy.git
cd real-time-drawing-board-backend-deploy
```

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install the dependencies:

```
pip install -r requirements.txt
```

---

### Configuration

Update the `settings.py` file with your Redis URL in the `CHANNEL_LAYERS` section:

```
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],  # Replace with your Redis server details
        },
    },
}
```

---

## Running the Development Server

Start the development server:

```
python manage.py runserver
```

If running WebSockets, you need to use the `ASGI` interface:

```
daphne -b 127.0.0.1 -p 8000 backend.asgi:application
```

---

## Deployment

### With [Docker](https://www.docker.com/)

1. Build the Docker image:

    ```
    docker build -t real-time-drawing-board-backend .
    ```

2. Run the container:

    ```
    docker run -p 8000:8000 real-time-drawing-board-backend
    ```

### Environment Variables

Ensure the following environment variables are set for production:
- `SECRET_KEY`: Your Django secret key.
- `DEBUG`: Set to `False` in production.
- `ALLOWED_HOSTS`: Add your domain or IP.
- Redis URL for `CHANNEL_LAYERS`.

---

## Repository Links

- **Backend Code**: [https://github.com/aringadre76/real-time-drawing-board-backend-deploy](https://github.com/aringadre76/real-time-drawing-board-backend-deploy)
- **Frontend Code**: [https://github.com/aringadre76/real-time-drawing-board-frontend](https://github.com/aringadre76/real-time-drawing-board-frontend)

---

## About the Creator

Developed by **Arin Gadre**.

- 🌐 **LinkedIn**: [https://www.linkedin.com/in/arin-gadre/](https://www.linkedin.com/in/arin-gadre/)
- 💻 **GitHub**: [https://github.com/aringadre76](https://github.com/aringadre76)
- 📧 **Email**: [aringadre@gmail.com](mailto:aringadre@gmail.com)
