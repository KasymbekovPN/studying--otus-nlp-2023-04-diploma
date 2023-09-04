from queue import Queue
from src.resume import Entity


def handle_init_queue_name(init_name: str) -> tuple:
    if init_name is not None:
        split_name = init_name.split('__')
        if len(split_name) == 3 and split_name[0] == 'q':
            for e in Entity:
                if e.value[1] == split_name[1]:
                    return True, e, split_name[2]
    return False, None, None


class Conductor:
    def __init__(self,
                 input_queue: Queue,
                 controller_queue: Queue,
                 handler=handle_init_queue_name,
                 **kwargs):
        # key example, education_default_queue
        pass



# todo ????
# from queue import Queue
# from threading import Thread
# from telebot import TeleBot
#
# from src.hw_005_bot.model.model import Model
# from src.hw_005_bot.execution.task import Task
#
#
# def consume_pq_task(queue: Queue, model: Model, bot: TeleBot):
#     print('\nPQ TASK CONSUMER is started.')
#
#     while True:
#         task = queue.get()
#         if task.kind == Task.KIND_SHUTDOWN:
#             break
#         if task.kind == Task.KIND_PQ:
#             result = task.get()
#             exec_result = model.execute(result['question'], result['passage'])
#             bot.send_message(result['user_id'], exec_result)
#
#     print('\nPQ TASK CONSUMER is done.')
#
#
# def start_pq_task_consumer(queue: Queue, model: Model, bot: TeleBot):
#     consumer = Thread(target=consume_pq_task, args=(queue, model, bot))
#     consumer.start()
