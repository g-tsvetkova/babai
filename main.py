from fastapi import FastAPI, Form
from utils import send_message
from dotenv import load_dotenv
from .pipeline import runner


app = FastAPI()
whatsapp_number = load_dotenv("CLIENT_NUMBER")
whatsapp_number = "+923481158655"


@app.get("/status")
async def index():
    return {"msg": "up & running"}


@app.post("/message")
async def reply(Body: str = Form()) -> str:
    """
    Endpoint to handle incoming messages, process them using the runner function,
    and send a response back via WhatsApp.
    """
    # Process the incoming message using runner
    response = runner(Body)
    
    # Send the response using Twilio
    send_message(whatsapp_number, response)
    return response