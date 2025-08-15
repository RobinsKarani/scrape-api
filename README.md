# ScrapeAPI - Web Scraping as a Service

Transform any website into a live JSON API with built-in caching and rate limiting.

## Features
- Real-time web scraping via HTTP endpoints
- Configurable caching (in-memory or Redis)
- Rate limiting protection
- Batch scraping support
- Docker-ready deployment
- RESTful API design

## Quick Start

### Using Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/RobinsKarani/scraper-api.git
cd scrapeapi

# Build and run with Docker
docker build -t scrapeapi .
docker run -p 8000:8000 scrapeapi

# Or use docker-compose
docker-compose up --build
```

### Using Python Directly
```bash
# Clone the repository
git clone https://github.com/yourusername/scrapeapi.git
cd scrapeapi

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
python run.py
```

## Usage Examples

**Scrape a Single URL**
```bash
curl "http://localhost:8000/api/scrape?url=https://httpbin.org/html"
```

**Batch Scraping**
```bash
curl -X POST "http://localhost:8000/api/scrape/batch" \
     -H "Content-Type: application/json" \
     -d '{"urls": ["https://httpbin.org/html", "https://httpbin.org/json"]}'
```

**With Custom Cache TTL**
```bash
curl "http://localhost:8000/api/scrape?url=https://example.com&cache_ttl=600"
```

## API Endpoints

| Method | Endpoint              | Description                      |
|--------|-----------------------|----------------------------------|
| GET    | `/`                   | Health check                     |
| GET    | `/api/scrape`         | Scrape a single URL              |
| POST   | `/api/scrape/batch`   | Scrape multiple URLs             |
| GET    | `/api/cache/stats`    | View cache statistics            |
| DELETE | `/api/cache/clear`    | Clear cache                      |
| GET    | `/docs`               | Interactive API documentation    |
| GET    | `/redoc`              | Alternative API documentation    |

## Configuration

Set these environment variables to configure ScrapeAPI:

| Variable         | Default               | Description                      |
|------------------|-----------------------|----------------------------------|
| `API_HOST`       | `0.0.0.0`             | Host to bind to                  |
| `API_PORT`       | `8000`                | Port to listen on                |
| `DEBUG`          | `False`               | Enable debug mode                |
| `CACHE_TTL`      | `300`                 | Cache time in seconds            |
| `CACHE_TYPE`     | `simple`              | Cache type (`simple`/`redis`)    |
| `REDIS_URL`      | `redis://localhost:6379` | Redis connection URL           |
| `REQUEST_TIMEOUT`| `10`                  | HTTP request timeout in seconds  |