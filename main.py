import time

def debounce(func, timeout=500):
    def wrapper(*args, **kwargs):
        def debounced():
            func(*args, **kwargs)
        return lambda: time.sleep(timeout) or debounced()
    return wrapper
