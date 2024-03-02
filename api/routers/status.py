from fastapi import APIRouter

router = APIRouter(
    prefix=("/status"),
    tags=["Status"]
)

@router.get("/status")
def status():
    return {"status": "Api is up and running!!!"}