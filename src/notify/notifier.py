from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    async def send_message(self, message):
        pass

    @abstractmethod
    async def receive_message(self)-> list[str]:
        pass
