from fastapi import APIRouter
from .v1 import user_routes

router_v1 = APIRouter(prefix="/api/v1")

router_v1.include_router(user_routes)
