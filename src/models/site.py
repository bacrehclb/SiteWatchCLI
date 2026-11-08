import datetime

from pydantic import HttpUrl, TypeAdapter, ValidationError

"""Site Model"""
class Site:
    site_count = 0
    
    def __init__(self, url: str, name: str):
        """URL check"""
        ta = TypeAdapter(HttpUrl)
        try:
            validated_url = ta.validate_python(url)
        except ValidationError:
            raise ValueError(f"Невалидный URL: {url}")
            
        Site.site_count += 1
        self.id = Site.site_count
        self.url = validated_url
        self.name = name
        self.date = datetime.UTC
        

        
