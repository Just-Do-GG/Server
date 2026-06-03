import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, JSON, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    game_id = Column(String, nullable=False, index=True)
    auth_type = Column(String, nullable=False)  # guest, google, apple
    auth_id = Column(String, nullable=True)  # google/apple sub
    display_name = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    last_login = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    saves = relationship("Save", back_populates="user", cascade="all, delete-orphan")


class Save(Base):
    __tablename__ = "saves"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    game_id = Column(String, nullable=False, index=True)
    data = Column(JSON, nullable=False, default=dict)
    version = Column(String, nullable=False, default="1.0")
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="saves")


class GameConfig(Base):
    __tablename__ = "game_configs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    game_id = Column(String, nullable=False, unique=True, index=True)
    features = Column(JSON, nullable=False, default=dict)
    ads_keys = Column(JSON, nullable=False, default=dict)  # {android: "", ios: ""}
    iap_products = Column(JSON, nullable=False, default=list)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
