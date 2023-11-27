import paralleldots

def getSentiment(input):
    paralleldots.set_api_key("h8K0KZSPxILzM9tHTFrQ0LjhxdIHH8MH3MJL6uXbCWo")
    
    return paralleldots.sentiment(input)