import multiprocessing
import os
#from dotenv import load_dotenv
#load_dotenv()

name = "root@jdp-datafarm-tagsvc"

accesslog = "/home/JobDesk_API/gunicorn-access.log"
errorlog = "/home/JobDesk_API/gunicorn-error.log"

bind = "0.0.0.0:8000"

worker_class = "uvicorn.workers.UvicornWorker"
workers = multiprocessing.cpu_count () * 2 + 1
worker_connections = 1024
backlog = 2048
max_requests = 5120
timeout = 1200
keepalive = 50

#debug = os.environ.get("debug", "false") == "true"
debug = True
reload = debug
preload_app = False
daemon = False

capture_output = True

loglevel = 'debug'

def worker_abort(worker):
    pid = worker.pid
    print("worker is being killed - {}".format(pid))
    dump_stack_for_process(pid)