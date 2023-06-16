import asyncio


class AsyncPlayground:
    @staticmethod
    async def io_operation1():
        return "Hello"

    @staticmethod
    async def io_operation2():
        return "World"

    async def main(self):
        tasks: list = []
        for i in range(1, 3):
            tasks.append(asyncio.create_task(getattr(self, f"io_operation{i}")()))

        await asyncio.gather(*tasks)

        results: list = []
        for task in tasks:
            results.append(task.result())

        print(*results)  # Hello World


if __name__ == "__main__":
    asyncPlayground = AsyncPlayground()
    asyncio.run(asyncPlayground.main())
