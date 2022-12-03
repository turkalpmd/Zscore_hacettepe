from deta import Deta

DETA_KEY = "a06jeh1v_GJmS8DEiFToMLujbKenNi4rKPKj4fMNr"

deta = Deta(DETA_KEY)

db = deta.Base("users_db ") 

def insert_user(username,name,password):
    return db.put({"key":username,
                   "name":name,
                   "pasword":password })

insert_user("izzet","turkalpmd","turko")