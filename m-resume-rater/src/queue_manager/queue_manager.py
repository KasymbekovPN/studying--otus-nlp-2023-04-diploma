from queue import Queue

from src.conversation.shutdown_request import ShutdownRequest


class QueueManager:
    def __init__(self) -> None:
        self._queues = []

    def create(self, max_size: int) -> Queue:
        q = Queue(max_size)
        self._queues.append(q)
        return q

    def stop(self) -> None:
        for q in self._queues:
            q.put(ShutdownRequest())
