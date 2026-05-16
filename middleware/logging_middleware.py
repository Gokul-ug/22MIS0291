import time


class LoggerMiddleware:

    @staticmethod
    def log(message: str):

        current_time = time.strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{current_time}] {message}")