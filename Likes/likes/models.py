from django.db import models

class Quote(models.Model):
    id = models.IntegerField(unique=True, primary_key=True),
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

class QuoteUser(models.Model):
    user_id = models.IntegerField(blank=True)
    quote_id = models.IntegerField(blank=True, unique=True)
    
    def __str__(self):
        return f"User id {str(self.user_id)} Product id {str(self.quote_id)}"
    
    