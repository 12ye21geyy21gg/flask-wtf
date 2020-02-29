from data import db_session
from data import users
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    user = users.User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    session = db_session.create_session()
    session.add(user)
    session.commit()
    user = users.User()
    user.surname = "Wrong"
    user.name = "Lacku"
    user.age = 22
    user.position = "voyager"
    user.speciality = "just engineer"
    user.address = "module_2"
    user.email = "wronger@mars.org"
    session.add(user)
    session.commit()
    user = users.User()
    user.surname = "Lisicium"
    user.name = "Hocku"
    user.age = 20
    user.position = "swimmer"
    user.speciality = "just resercher"
    user.address = "module_3"
    user.email = "Hoscku@mars.org"
    session.add(user)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()
