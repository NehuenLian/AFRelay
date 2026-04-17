
import httpx


class WSFEClientManager:
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self.__class__._client is None:
            self.__class__._client = httpx.AsyncClient()

    def get_client(self): 
        return self.__class__._client
    
    @classmethod
    def reset_singleton(cls):
        cls._instance = None
        cls._client = None

    async def close(self) -> None:
        if self.__class__._client:
            await self.__class__._client.aclose()
            self.__class__._instance = None
            self.__class__._client = None
