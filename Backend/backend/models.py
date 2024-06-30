from datetime import datetime
from sqlalchemy import func, String, ForeignKey
from sqlalchemy.orm import Mapped, registry, mapped_column, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(init=False, default=func.now(), onupdate=func.now())

@table_registry.mapped_as_dataclass
class category:
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    description: Mapped[str] = mapped_column(String(255), unique=True)

@table_registry.mapped_as_dataclass
class product:
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    description: Mapped[str] = mapped_column(String(255), unique=True)
    price: Mapped[str] = mapped_column(String(255), unique=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))

    category: Mapped['category'] = relationship("Category", back_populates="products")
    
    
