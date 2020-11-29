# 1º Step
    $ sudo apt install -y tcl

# 2º Step
    $ wget https://download.redis.io/releases/redis-6.0.9.tar.gz

# 3º Step
    $ tar xzf redis-6.0.9.tar.gz

# 4º Step
    $ cd redis-6.0.9

# 5º Step
    $ make

# 6º Step
    $ make test

# 7º Step
    $ pip install -r requirements.txt

# 8º Step
Open the first terminal and run:

    $ src/redis-server

# 9º Step
Open the second terminal and run:

    $ celery -A app.cel worker --loglevel=info

# 10º Step
Open the third terminal and run:

    $ celery -A app.cel beat --loglevel=info

# 11º Step
Open the fourth terminal and run:

    $ python run.py