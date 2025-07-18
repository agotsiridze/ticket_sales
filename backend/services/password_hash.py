from abc import ABC, abstractmethod
import bcrypt


class PasswordEncode(ABC):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        raise NotImplementedError("Method must be implemented in subclass!")

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        raise NotImplementedError("Method must be implemented in subclass!")



class BCryptPasswordEncode(PasswordEncode):
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    encoding = 'utf-8'
    
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(self.encoding), salt)
        return hashed.decode(self.encoding)
    
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode(self.encoding), hashed_password.encode(self.encoding))