from db.db_config import conn
from models.tables import product as product_model
from schemas.product import Product,ProductInDB
from fastapi import HTTPException,status

def get_product_by_id(id: str):
    product = conn.execute(product_model.select().where(product_model.c.id == id)).first()
    print(product)
    if product is None:
        raise HTTPException(status_code=404,detail="No product")
    return product


# def get_users():
#     return conn.execute(users.select()).fetchall()


# def aut_user(username: str, password: str):
#     user = get_user_by_username(username)
#     if not user:
#         return False
#     else:
#         return user if check_hash_password(password, user.password) else False


# def create_user(user: UserInDB):
#     new_user = {"username": user.username,
#                 "description": user.description,
#                 "roleID": "USER",
#                 "isDisable": False,
#                 "avtSrc": user.avtSrc
#                 }
#     new_user["password"] = get_hash_password(user.password)
#     print(new_user)
#     result = conn.execute(users.insert().values(new_user))
#     print(result)
#     return new_user


# def update_user(username: str, user: User):
#     return conn.execute(
#         users.update().values(
#             description=user.description, 
#             avtSrc=user.avtSrc
#             ).where(users.c.username == username))

# def del_user(username: str):
#     user_c = get_user_by_username(username)
#     if not user_c:
#         return False
#     else:
#         conn.execute(
#             users.update().values(isDisable=True).where(
#                 users.c.username == username))
#         return True


# def actviate_user(username: str):
#     user_c = get_user_by_username(username)
#     if not user_c:
#         return False
#     else:
#         return conn.execute(users.update().values(isDisable=False).where(users.c.username == username))
