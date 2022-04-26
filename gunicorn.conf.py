import multiprocessing

reload = True
workers = multiprocessing.cpu_count() * 2 + 1
bind = "unix:/run/gunicorn.sock"
