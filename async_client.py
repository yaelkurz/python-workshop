import asyncio
import httpx
from time import time

async def hit_endpoint(client, url):
    resp = await client.get(url)
    return resp.status_code

async def run_benchmark(endpoint: str, num_requests: int):
    async with httpx.AsyncClient(timeout=None) as client:
        print(f"-----------START------------")
        tasks = [hit_endpoint(client, endpoint) for _ in range(num_requests)]

        start = time()
        await asyncio.gather(*tasks)
        duration = time() - start1

        print(f"{num_requests} requests to {endpoint} completed in {duration:.2f}s")
        print(f"-----------DONE------------")

if __name__ == "__main__":
    # 🔧 Configure here
    endpoint_1 = "perfect-ping"
    endpoint_2 = "good-ping"
    endpoint_3 = "terrible-ping"


    url = f"http://localhost:8000/{endpoint_1}"
    count = 1

    asyncio.run(run_benchmark(url, count))
    