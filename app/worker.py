#define celery worker here
import os
import time
import subprocess
import json
import re

import crud, models, schemas

from celery import Celery
from celery.utils.log import get_task_logger

from sqlalchemy.orm import Session
from database import SessionLocal, engine


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

celery_log = get_task_logger(__name__)

'''def execute_nmap_tcp_scan(ip, ports):
    result = subprocess.run(["nmap", "-p"+ports, "-T5", "--open", "-r", ip], capture_output=True)
    if result.returncode == 0:
        rex = re.compile(r'\d+\/tcp')
        parse_result = result.stdout.decode('utf-8')
        ports_result = rex.findall(parse_result)

        return [int(port.strip('/tcp')) for port in ports_result]

    return None



@celery.task(name="port_scan_task")
def port_scan_task(device_ports):

    db = SessionLocal()
    device = crud.get_device(db, device_ports["device_id"])
    db.close()

    print("scan port...")
    open_ports = []
    if device != None:
        open_ports = execute_nmap_tcp_scan(device.ip, device_ports["ports_range"])
        if open_ports != None:
            db = SessionLocal()
            crud.update_device_open_port(db, device_ports["device_id"], open_ports)
            db.close()
            return open_ports

    return None'''
