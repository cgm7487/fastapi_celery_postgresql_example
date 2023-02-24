from fastapi import FastAPI

from sqlalchemy.orm import Session

from .db.models import models
from .db.postgres.database import engine

from .api.v0 import router

#import task here
#from worker import port_scan_task
#import schemas here
#from schemas import DevicePorts

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router.api_router)



#@app.post("/portscan/")
#async def device_ports_scan(device_ports:DevicePorts):#, background_tasks: BackgroundTasks):
#    json_compatible_device_port_data = jsonable_encoder(device_ports)
#    task = port_scan_task.delay(json_compatible_device_port_data)
#    return JSONResponse({"task_id": task.id})