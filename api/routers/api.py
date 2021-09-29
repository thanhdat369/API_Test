from fastapi import APIRouter
import api.routers.auth as auth
import api.routers.user as user
import api.routers.product as product
api_router = APIRouter()
api_router.include_router(auth.router,tags=["Authenticate"])
api_router.include_router(user.router,prefix="/users",tags=["User"])
api_router.include_router(product.router,prefix="/products",tags=["Product"])