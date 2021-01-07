import asyncio

async def do_job_1():
    while True :
        print('do_job_1')
        await asyncio.sleep(5)

async def do_job_2():
    while True :
        print('do_job_2')
        await asyncio.sleep(5)

async def main():
    await asyncio.gather(do_job_1(), do_job_2())

if __name__ == '__main__':
    asyncio.run(main())