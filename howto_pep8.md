# PEP-8

Немного документации: [english](https://www.python.org/dev/peps/pep-0008/), [russian](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html).

## Зачем?

* Так гораздо проще читать код (мне -- сейчас, вам -- через месяц, всем -- всегда);
* Я наверняка попрошу вас привести код в соответствие с pep-8, т.к. в красивом коде проще найти ошибки;
* Это просто стандарт и хороший тон разработчика.

## Как?

Устанавливаете пакет через pip:

`pip install pep8`

Запускаете:

`pep8 my_code.py`

Результат похож на:

```
source.py:289:9: E265 block comment should start with '# '
source.py:292:5: E303 too many blank lines (2)
source.py:296:5: E303 too many blank lines (2)
source.py:309:36: E225 missing whitespace around operator
source.py:327:33: E225 missing whitespace around operator
source.py:373:80: E501 line too long (82 > 79 characters)
source.py:377:80: E501 line too long (88 > 79 characters)
```

Ещё можно запустить его с флагом `--show-source`, так будет показываться конкретная ошибка:

```
$ pep8 --show-source my_code.py 
  '\n\n'
my_code.py:11:1: E302 expected 2 blank lines, found 1
class CurrencyLoader(ItemLoader):
^
my_code.py:14:1: E302 expected 2 blank lines, found 1
class WeeklySpider(CrawlSpider):
^
my_code.py:18:46: E261 at least two spaces before inline comment
    only_2018_april_regex = '/201804[0-9]{2}' # full history parsing takes ~4 hrs

. . .
```

## Частые ошибки

`E501 line too long` -- строки не должны превышать 80 символов.

Например, такой код не пройдёт:
```python
x = some_variable + another_variable * third_variable / (divisor_with_long_name + epsilon)
```
* Решение 1: ставить `\` в конце строки -- объединение сток, как в С++:
```python
x = some_variable + another_variable * third_variable \
    / (divisor_with_long_name + epsilon)
```
При этом **сразу** после `\` должен стоять перевод строки.

* Решение 2 (лучше): разбивать на строки, группируя из в скобки -- так тоже ок и парсер не сломается:
```python
x = (some_variable # в этом случае можно писать комментарии
    + another_variable * third_variable
    / (divisor_with_long_name + epsilon))
```

## Ещё

Всегда надо завершать файл пустой строкой.
