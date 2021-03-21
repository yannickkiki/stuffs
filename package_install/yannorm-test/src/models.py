from yannorm import BaseModel, BaseManager

from src.settings import DB_SETTINGS


BaseManager.set_connection(database_settings=DB_SETTINGS)


class Employee(BaseModel):
    table_name = "employees"
    manager_class = BaseManager
