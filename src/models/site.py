from pydantic import HttpUrl, TypeAdapter, ValidationError

"""Site Model"""
class Site:
    site_count = 0
    
    def __init__(self, url, name):
        Site.site_count += 1
        self.id = Site.site_count
        self.url = url
        self.name = name
        
    """URL check"""
    def check_url(self) -> bool:
            ta = TypeAdapter(HttpUrl)
            try:
                ta.validate_python(self.url)
                return True
            except ValidationError:
                return False
        
        
