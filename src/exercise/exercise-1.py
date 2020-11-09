import random
import asyncio
from datetime import datetime
import aiofiles as aiof
from fastapi import FastAPI

app = FastAPI()

@app.get('/async')
async def terasync():
	start_time = datetime.now()
	async with aiof.open("file.txt", "w") as out:
		await data_lines = ( '%i %f\n'%(seq_id, random.random()) 
			for seq_id in range(0, 10000000) )
		await out.write(''.join(data_lines))
		await out.flush()
	return {"time_lapse": (datetime.now()-start_time)}

@app.get('/sync')
def tersync():
	start_time = datetime.now()
	menunggu()
	return {"time_lapse": (datetime.now()-start_time)}

def menunggu():
	data_file = open('file.txt', 'w')
	data_lines = ( '%i %f\n'%(seq_id, random.random()) 
                            for seq_id in range(0, 10000000) )
	contents = ''.join(data_lines)
	data_file.write(contents)
