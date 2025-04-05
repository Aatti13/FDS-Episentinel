from passlib.context import CryptContext 

passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")