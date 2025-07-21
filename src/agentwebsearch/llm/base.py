from abc import ABC, abstractmethod


class BaseChatModel(ABC):
    @abstractmethod
    def submit(self, messages: list[dict]) -> str: pass
