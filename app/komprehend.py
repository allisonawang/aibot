import paralleldots
import os

def getSentiment(input):
    paralleldots.set_api_key(os.environ.get("PARALLELDOTS_API_KEY"))
    
    return paralleldots.sentiment(input)