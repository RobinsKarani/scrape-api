from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from config import config
import asyncio
import logging

from scraper import WebScraper
from cache import cache

#configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Web Scraper API",
    description="Turn any website into a programmable API",
    version="1.0.0"
)

#initialize scraper
scraper = WebScraper("https://example.com")

class ScrapeRequest(BaseModel):
    urls: List[str]
    cache_ttl: Optional[int] = 300

class ScrapedData(BaseModel):
    data: List[dict]
    cached: bool

@app.get("/")
async def root():
    return {"message": "Web Scraper API is running!"}

@app.get("/api/scrape")
async def scrape_url(
    url: str = Query(..., description="URL to scrape"),
    cache_ttl: int = Query(300, description="Cache TTL in seconds")
):
    """Scrape a single URL with caching"""
    cache_key = f"scrape:{url}"
    
    # Check cache first
    cached_data = cache.get(cache_key)
    if cached_data:
        logger.info(f"Cache hit for {url}")
        return {"data": cached_data, "cached": True}
    
    # Scrape fresh data
    logger.info(f"Scraping {url}")
    try:
        data = scraper.scrape_product_data(url)
        cache.set(cache_key, data, cache_ttl)
        return {"data": data, "cached": False}
    except Exception as e:
        logger.error(f"Scraping failed for {url}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/scrape/batch")
async def scrape_batch(request: ScrapeRequest):
    """Scrape multiple URLs"""
    results = []
    for url in request.urls:
        cache_key = f"scrape:{url}"
        cached_data = cache.get(cache_key)
        
        if cached_data:
            results.append({"url": url, "data": cached_data, "cached": True})
        else:
            try:
                data = scraper.scrape_product_data(url)
                cache.set(cache_key, data, request.cache_ttl)
                results.append({"url": url, "data": data, "cached": False})
            except Exception as e:
                results.append({"url": url, "error": str(e), "cached": False})
    
    return {"results": results}

@app.get("/api/cache/stats")
async def cache_stats():
    """Get cache statistics"""
    return {
        "cache_size": len(cache.cache),
        "keys": list(cache.cache.keys())
    }

@app.delete("/api/cache/clear")
async def clear_cache():
    """Clear all cache"""
    cache_size = len(cache.cache)
    cache.cache.clear()
    cache.ttls.clear()
    return {"message": f"Cleared {cache_size} cached items"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)