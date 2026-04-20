import httpx


class WSFEClientManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._client = httpx.AsyncClient()
        return cls._instance

    def get_client(self):
        if self._client:
            return self._client
    
    @classmethod
    def reset_singleton(cls):
        cls._instance = None

    async def close(self) -> None:
        if self._client:
            await self._client.aclose()
            self.reset_singleton()
