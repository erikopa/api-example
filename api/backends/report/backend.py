from abc import ABCMeta, abstractmethod


class ReportBackend(metaclass=ABCMeta):
    id: str = ''
    name: str = ''

    @abstractmethod
    async def get_report(self, data: str) -> str:
        pass
