Сборка и запуск<br>
В корне проекта создать файл .env с переменными окружения:<br>
POSTGRES_DB = 'your_db'<br>
POSTGRES_USER = 'your_user'<br>
POSTGRES_PASSWORD = 'your password'<br>
DB_HOST = 'your_host'<br>
CART_ID = 'cart'<br>
STRIPE_SECRET_KEY = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc' - тестовый секретный ключ для stripe<br>
STRIPE_PUBLIC_KEY = 'pk_test_TYooMQauvdEDq54NiTphI7jx'- тестовый публичный ключ для stripe<br>
<br>
sudo docker-compose build<br>
sudo docker-compose up<br>
<br>
docker exec -it container_id strip/python manage.py createsuperuser<br>
<br>
Зайти в админ-панель, создать несколько товаров, возможно создать несколько скидок, <br>
которые будут отображаться в форме заказа <br>
<br>
- [x] Добавлен запуск, используя Docker<br>
- [x] Добавлено виртуальное окружение<br>
- [x] Добавлен django-admin<br>
- [x] Добавлена модель Order и корзина покупателя с возможностью удаления товара<br>
- [x] Добавлена модель Discount с возможностью выбора скидки при заполнении формы заказа<br>
- [x] Добавлен выбор валюты, доллар или евро<br>


