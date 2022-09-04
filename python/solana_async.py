# https://explorer.solana.com/address/8kaAbZYLHUDadjgpRXkZE63E2AvsZDtJRddAMXtLB4ev/tokens
# https://public-api.solscan.io/docs/#/Account/get_account__account_
# https://public-api.solscan.io/account/8kaAbZYLHUDadjgpRXkZE63E2AvsZDtJRddAMXtLB4ev

# https://github.com/michaelhly/solana-py/
# from solana.rpc.api import Client
# http_client = Client("https://api.devnet.solana.com")

# https://github.com/michaelhly/solana-py/
# Async API Client
import asyncio
from solana.rpc.async_api import AsyncClient

async def main():
    async with AsyncClient("https://api.devnet.solana.com") as client:
        res = await client.is_connected()
    print(res)  # True

    # Alternatively, close the client explicitly instead of using a context manager:
    client = AsyncClient("https://api.devnet.solana.com")
    res = await client.is_connected()
    print(res)  # True
    await client.close()

asyncio.run(main())


# Websockets Client
import asyncio
from asyncstdlib import enumerate
from solana.rpc.websocket_api import connect

async def main():
    async with connect("wss://api.devnet.solana.com") as websocket:
        await websocket.logs_subscribe()
        first_resp = await websocket.recv()
        subscription_id = first_resp.result
        next_resp = await websocket.recv()
        print(next_resp)
        await websocket.logs_unsubscribe(subscription_id)

    # Alternatively, use the client as an infinite asynchronous iterator:
    async with connect("wss://api.devnet.solana.com") as websocket:
        await websocket.logs_subscribe()
        first_resp = await websocket.recv()
        subscription_id = first_resp.result
        async for idx, msg in enumerate(websocket):
            if idx == 3:
                break
            print(msg)
        await websocket.logs_unsubscribe(subscription_id)

asyncio.run(main())
