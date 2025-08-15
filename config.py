import os
from typing import Optional

class Config:
    #API Settings
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"  #False fn
    
    #Cache Settings
    CACHE_TTL = int(os.getenv("CACHE_TTL", 300))
    CACHE_TYPE = os.getenv("CACHE_TYPE", "simple")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Scraper Settings
    DEFAULT_USER_AGENT = os.getenv(
        "USER_AGENT", 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))
    
    # Rate Limiting
    RATE_LIMIT = os.getenv("RATE_LIMIT", "10/minute")
    
    # Security
    API_KEY_REQUIRED = os.getenv("API_KEY_REQUIRED", "False").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")

# Global config instance
config = Config()