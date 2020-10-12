from datetime import datetime

def timer(func):

    def wrapper():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        duration = end_time - start_time
        print(f" duration : {duration.seconds // 3600}:{duration.seconds // 60}:"
              f"{duration.seconds % 60}")

    return wrapper

