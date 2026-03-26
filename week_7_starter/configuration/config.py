from pydantic_settings import BaseSettings
from pydantic import BaseModel

class ServerSettings(BaseSettings):
    api_key:str = 'acf1888b49184eb39fd94ef3b9709bf5'
    endpoint:str = 'https://api-v3.mbta.com/'

class Message(BaseModel): #Create a message model for handling errors 
    message: str #A string to store the message
    