import requests
from bs4 import BeautifulSoup
import time
from typing import Dict, List, Optional

class WebScraper:
    def __init__(self, base_url: str, headers: Optional[Dict] = None):
        self.base_url = base_url
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def scrape_product_data(self, url: str) -> Dict:
        """Example: scrape product information"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            #example parsing logic, customize for your target site
            title = soup.find('h1')
            price = soup.find('span', class_='price')
            description = soup.find('div', class_='description')
            
            return {
                'title': title.get_text().strip() if title else 'N/A',
                'price': price.get_text().strip() if price else 'N/A',
                'description': description.get_text().strip() if description else 'N/A',
                'timestamp': time.time(),
                'url': url
            }
        except Exception as e:
            return {'error': str(e), 'url': url}