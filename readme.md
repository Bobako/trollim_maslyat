1. В файлике результы парсинга инстаграмма. Для каждого из постов вычленить словарь вида {
     id,
     urls(список ссылок  поста), (меня интересует не одна фотка в разном качестве, а все из поста. если она там одна - похуй, клади одну в массив)
     caption(текст поста),
     likes (число лайков),
     comments(число комментов),
     timestamp(дата и время снимка в секундах от начала эпохи) (вот эту хуйню лучше преобразовать в человекочитаемый формат. Подробнее - https://pythonworld.ru/moduli/modul-datetime.html)
     }
     
Результаты записать в файлы в форматах:
    а) Json (https://python-scripts.com/json)
    б) csv (https://docs.python.org/3/library/csv.html#writer-objects - юзай DictWriter)
    в) Табличку в эксель (https://openpyxl.readthedocs.io/en/stable/ )
