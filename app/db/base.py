import uuid
from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

# Define the base class using the SQLAlchemy declarative base
Base = declarative_base()


class BaseModel(Base):
    """
    Abstract base class for SQLAlchemy models, providing common columns and behavior.
    """

    __abstract__ = True  # Indicates that this class is not to be mapped to a table

    # Primary key for all models, using UUID
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)

    # Timestamp when the record is created, stored in UTC
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)

    # Timestamp when the record is updated, stored in UTC, updated automatically on record update
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)

    # Timestamp for soft deletion, stored in UTC, nullable since not all records may be deleted
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def soft_delete(self):
        """
        Mark the record as deleted by setting the `deleted_at` field to the current time.
        """
        self.deleted_at = func.now()

    def __repr__(self):
        """
        Provide a string representation of the model that includes the class name and its primary key.
        """
        return f"<{self.__class__.__name__}(id={self.id})>"
