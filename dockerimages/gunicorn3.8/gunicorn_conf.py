import multiprocessing
import os
host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "80")
loglevel = os.getenv("LOG_LEVEL", "info")
workers_per_core = 2
workers = workers_per_core * multiprocessing.cpu_count()
bind = "{host}:{port}".format(host=host, port=port)
keepalive = 120
errorlog = "-"
timeout=3600
print("loglevel={loglevel} workers={workers} bind={bind} bind={bind}".format(loglevel=loglevel, workers=workers, bind=bind, bind=bind))
