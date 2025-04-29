from fastapi import FastAPI
import uuid

app = FastAPI()

@app.get("/generate-code/")
def get_random_uuid_code():
    """
    Generate a random UUID code.
    """
    random_uuid = str(uuid.uuid4())
    return {"code": random_uuid}
