import uvicorn
from config import config

if __name__ == "__main__":
    uvicorn.run(
        "main:app",                    
        host=config.API_HOST,          
        port=config.API_PORT,          
        reload=config.DEBUG,           
        workers=1                      
    )