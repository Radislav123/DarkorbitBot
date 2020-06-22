import time


def from_found(filename: str):
    return "..\\resources\\found\\" + filename


def to_found(filename: str):
    return from_found(filename)


def from_logs(filename: str):
    return "..\\logs\\" + filename


def to_logs(filename: str):
    return from_logs(filename)


def from_resources(filename: str):
    return "..\\resources\\" + filename


def to_resources(filename: str):
    return from_resources(filename)


def from_navigate(filename: str):
    return "..\\resources\\navigate\\" + filename


def to_navigate(filename: str):
    return from_navigate(filename)


def get_execution_time(function, *args, **kwargs):
    start = time.time()
    value = function(*args, **kwargs)
    end = time.time()
    return end - start, value


def print_execution_time(function, *args, **kwargs):
    execution_time, value = get_execution_time(function, args, kwargs)
    print(function.__name__ + " : execution_time : " + str(execution_time))
    return value
