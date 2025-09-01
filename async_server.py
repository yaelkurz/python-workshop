import asyncio
import time

from fastapi import FastAPI, APIRouter

router = APIRouter()
sleep_time = 25

@router.get("/terrible-ping")
async def terrible_ping():
    time.sleep(sleep_time)  # Blocks event loop — BAD
    return {"pong": True}

@router.get("/good-ping")
def good_ping():
    time.sleep(sleep_time)  # Runs in thread — OK
    return {"pong": True}

@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(sleep_time)  # Async non-blocking — BEST
    return {"pong": True}

@router.get("/health")
def health():
    return {"status": "ok"}

# FastAPI app
app = FastAPI()
app.include_router(router)

# Run with uvicorn if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("async_server:app", host="0.0.0.0", port=8000, reload=False)