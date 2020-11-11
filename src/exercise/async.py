from fastapi import FastAPI
import aiohttp
import asyncio
import json
import time
import requests
from aiohttp import ClientSession

app = FastAPI()


async def get_json(client: ClientSession, url: str) -> bytes:
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()

async def get_reddit_top(subreddit: str, client: ClientSession, data: dict):
    data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data1.decode('utf-8'))
    subreddit_data = []
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')
        subreddit_data.append(str(score) + ': ' + title + ' (' + link + ')')
    data[subreddit] = subreddit_data
    print('DONE:', subreddit + '\n')


@app.get("/async")
async def get_reddit_data_api() -> dict:
    start_time: float = time.time()
    client: ClientSession = aiohttp.ClientSession()
    data: dict = {}

    await asyncio.gather(
        get_reddit_top('python', client, data),
        get_reddit_top('programming', client, data),
        get_reddit_top('compsci', client, data),
    )
    await client.close()

    print("Got reddit data in ---" + str(time.time() - start_time) + "seconds ---")
    return {"time": f"{str(time.time() - start_time)} seconds", "data": data}


def get_reddit_top_sync(subreddit: str, data: dict):
	data1 = requests.get('https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5', headers={'User-agent': 'fastapi 0.1'})
	result = data1.json()
	subreddit_data = []
	for i in result['data']['children']:
		score = i['data']['score']
		title = i['data']['title']
		link = i['data']['url']
		print(str(score) + ': ' + title + ' (' + link + ')')
		subreddit_data.append(str(score) + ': ' + title + ' (' + link + ')')
		data[subreddit] = subreddit_data
	print('DONE:', subreddit + '\n')


@app.get("/sync")
def get_reddit_data() -> dict:
    start_time: float = time.time()
    data: dict = {}

    get_reddit_top_sync("python", data)
    get_reddit_top_sync("programming", data)
    get_reddit_top_sync("indonesia", data)
    return {"time": f"{str(time.time() - start_time)}seconds" ,"data": data}
