import random
import time

list_of_cats = ['Мэри Шелли', 'Фламбуша', 'Петра', 'Родезия', 'Цукерка', 'Арракис', 'Комбат']

def happy_cat():
  happy_cat_today = random.choice(list_of_cats)
  mes = f'Сегодня лучшее угощение получает {happy_cat_today}'
import random
import time

list_of_cats = ['Мэри Шелли', 'Фламбуша', 'Петра', 'Родезия', 'Цукерка', 'Арракис', 'Комбат']

def happy_cat():
  happy_cat_today = random.choice(list_of_cats)
  mes = f'Сегодня лучшее угощение получает {happy_cat_today}'

def choice_action():
   feed_cat = input('Хотите угостить кота? --> (да/нет')

if feed_cat == 'да' or 'Да':
  happy_cat()

elif feed_cat == 'нет' or 'Нет':
  print('Ах вы жадина!!!')
  choice_action()
else:
  print('До свидания')
  time.sleep(1)

def choice_action():
   feed_cat = input('Хотите угостить кота? --> (да/нет')

if feed_cat == 'да' or 'Да':
  happy_cat()
  
elif feed_cat == 'нет' or 'Нет':
  print('Ах вы жадина!!!')
  choice_action()
else:
  print('До свидания')
  time.sleep(1)
