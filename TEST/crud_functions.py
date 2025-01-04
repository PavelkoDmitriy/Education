import sqlite3
img_url = [
    "https://yandex-images.clstorage.net/KJl5O2200/5340fezQXd_/ue9LZoNX6MHt6T7LbjlVz66kAV4kmY5qBlJYueRmDvsolvIwX002UzkswXc8Nt6cbQijnzGLRCHy9qyjM8eib-38X_RUxijAqPv8WGi6Ucr9o1GbdB_Pa9ARWGIqr1Mm8xy--tbRPZU5OxSgOzCMGDSS5wGuVEa_cWBg6-Ta_bG6rshuS8giye209YOjO5VAuKJLlnlSUe7FjgIoZ26XJPZf8fFT3zBRczhZp_gljB23WXzKL5cP8DEhKmosV7qz9-EAasPBYsWqeXHKKf5fRHWtyNUyUF1uy83ALu9j2Cu1HjfzVBs7Xj31EOC2ooJb9h41BmdWRDGyriHq4pAxs7IuwqCFAKsOpL96yG52Hw125khfe91TaArIQe5r5hemstJ28ZwQNB_wO5GgPe2L2f9fc88m1E_-MWtuIuQT9Tk05EFhzklhgWOxeMJgPh0E_GJBmLpXmSPDSA0taCoZYnrVOjqdkDLXsHGfoj9nQFfwH3uD6h0A-DIrpeaiGfE_ui9I4UvJYQnicnSOpPgYBXBrghd0WVohysaC4GMrXWy1XP91W9C3nfDxVK18pYTQNpQzBiRahzx6LqKkqpz8cHCpi-7JD6vMLfSzC2c1lk-86kkQPl_frUcNRqbk5Z_v9xe7uZ9Zt155PFwqv6lNGXDYPQppFUU8euMpYO1fdrM9LAjpQ0fuzum2O8Iss18NdO0E3zNVU-oERAIpZysRY3jWtDrX0XuQeTIQpzenzVl6GHqIqBEB_XCjaK5k3ry-NGgAKwJIqsFivDPI53udgrMjgZA_nxrshEdMaKxsUi9-nzR7lZ07k7X72yN14ktUehw0CG6Wi7Y34yAsYtS3_jRkwe5PSuLEYXExzm_7Egi1agBQu1YbqseLTqCvbJ6q-t__M1xSMpcydJQlfufFVHdZek0uG8A_O-sg6Gqbsb7_6c0vTMFvzG12ckkmvNIB_63JW3VR3SnCiwKrYM",
    "https://sun9-29.userapi.com/impf/lJ9xaQSBNEpPKvu23EHGwigj1f9z8irFwtmkdw/2pfvzDssAFk.jpg?size=1920x768&quality=95&crop=0,28,1000,399&sign=037d2726c0a0416d96dab821581cc296&type=cover_group",
    "https://cdn1.ozone.ru/multimedia/1019411644.jpg",
    "https://detsadyar.ru/upload/iblock/d59/d596b5a0b9011c41f8c9b5cad70d7fe4.jpeg"
]

def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL,
    img TEXT
    )
    ''')

    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price, img) VALUES (?, ?, ?, ?)", (f'Product {i}', f'Описание {i}', (i*100), img_url[i-1]))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    res = cursor.fetchall()
    connection.close()
    return res
