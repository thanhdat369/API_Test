from fastapi import Depends,status,HTTPException
from fastapi.routing import APIRouter

from typing import List,Optional

from api.dependencies.user import get_current_active_user,get_current_active_admin
from schemas.product import Product,ProductInDB
from schemas.user import UserInDB
import services.product as product_services

router = APIRouter()

# @router.get("/",response_model=List[User])
# async def get_all_user(current_user: UserInDB = Depends(get_current_active_admin)):
#     return user_services.get_users()

@router.get("/{id}",response_model=Product)
async def get_all_user(id:str):
    return product_services.get_product_by_id(id)

@router.post("/")
async def create_product(
    # product:Product,
    page:Optional[int]=1,
    limit:Optional[int]=10,
    dat:Optional[int] = None
    ):
    return {"page":page,"limit":limit}

# @router.delete("/{username}")
# async def delete_user(username:str,current_user: UserInDB = Depends(get_current_active_user)):
#     if current_user.roleID=="ADMIN" or current_user.username == username:
#         return user_services.del_user(username)
#     else:
#         raise HTTPException(status_code=401, detail="No Permission")



# @router.put("/{username}")
# async def update_user(username:str,user_update:User,current_user: UserInDB = Depends(get_current_active_user)):
#     if current_user.roleID=="ADMIN" or current_user.username == username:
#         return user_services.update_user(username,user_update)
#     else:
#         raise HTTPException(status_code=401, detail="No Permission")