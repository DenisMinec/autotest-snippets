class ErrorsCollector:
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self, value=None):
        self.__errors = [value] if value else [] 
    
    def get_errors(self):
        return self.__errors
    
    def add_error(self, value):
        self.__errors.append(value)
        
    errors = property(get_errors, add_error)
    

