import datetime

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

file_path = 'logs.txt'

def get_log(path):
    def decorator(some_function):
      def new_function(*args, **kwargs):
          result = some_function(*args, **kwargs)
          with open('logs.txt', 'w', encoding='utf-8') as file:
            file.write(f'Текущая дата и время: {datetime.datetime.now()}\n'
                       f'Была вызвана функция: {some_function.__name__}\n'
                       f'Аргументы функции: {args, kwargs}\n'
                       f'Результат: {result}\n')
          return result
      return new_function
    return decorator

@get_log(file_path)
def new_function(*args, **kwargs):
    stats_items = stats.items()
    stats_list = list(stats_items)
    maximum = max(stats_list, key=lambda i: i[1])
    return(maximum[0])

if __name__ == '__main__':
  new_function(stats)