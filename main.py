from pathlib import Path
from fastapi import FastAPI
from AppConfig import CurrentConfig

app = FastAPI()

# Check for existence of hostname
hostname = "HOSTNAME FILE NOT FOUND"
hostname_path = Path("/etc/hostname")
if hostname_path.exists():
    hostname = hostname_path.read_text()
    hostname = hostname.strip()
#Simulate a log
print(hostname)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/configtest")
def configtest():
    return {
        "test_return":CurrentConfig().getConfig().test_return,
        "sent_from":hostname
    }

