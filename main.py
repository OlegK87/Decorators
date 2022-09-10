import logging
import datetime

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def stats2(stats):
  stats_items = stats.items()
  stats_list = list(stats_items)
  maximum = max(stats_list, key=lambda i: i[1])
  return(maximum[0])

def decorator(some_function):
  def new_function(a, b):
    logging.basicConfig(filename=f'{b}\myapp.log', level=logging.INFO)
    logging.info(f"Текущая дата и время: {datetime.datetime.now()}")
    logging.info(f"Была вызвана функция {some_function.__name__} с аргументами {a} и {b}")
    result = some_function(a)
    logging.info(f"результат {result}")
    return result
  return new_function


if __name__ == '__main__':
  new_function = decorator(stats2)
  new_function(stats, 'C:\Demo')


