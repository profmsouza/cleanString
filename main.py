from typing import Optional
import re
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/clean")
def clean(input_string: str):
    # Remove tudo entre parênteses
    cleaned_string = re.sub(r'\(.*?\)', '', input_string)  
    # Remove pontuação
    cleaned_string = re.sub(r'[^\w\s]', '', cleaned_string)
    # Remove múltiplos espaços em branco
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string).strip()
    
    return {"cleaned_string": cleaned_string}
