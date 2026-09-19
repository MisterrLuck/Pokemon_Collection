from database import init_db, db_session
from models import User, Card
init_db()

print("db_session.add(u)")
print("db_session.commit()")
print("User.query.all()")
