from app.database import engine, Base, SessionLocal
from app.models.user import User, Student, Faculty
from app.models.attendance import Attendance
from passlib.context import CryptContext

# Tables create karanyasathi he garjeche ahe
Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db = SessionLocal()

# Check if admin already exists
existing_admin = db.query(User).filter(User.email == "durgamundkar123@gmail.com").first()

if existing_admin:
    print("Admin already exists!")
else:
    hashed_pass = pwd_context.hash("123")
    
    new_admin = User(
        full_name="Durga Mundkar",
        email="durgamundkar123@gmail.com",
        password=hashed_pass,
        role="admin"
    )
    
    db.add(new_admin)
    db.commit()
    print("Admin created successfully!")

db.close()