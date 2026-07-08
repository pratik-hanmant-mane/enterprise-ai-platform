from typing import Generic, TypeVar, Type

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Generic repository providing common persistence operations.
    """

    def __init__(
        self,
        session: Session,
        model: Type[ModelType],
    ):
        self.session = session
        self.model = model

    def get_by_id(
        self,
        entity_id: int,
    ) -> ModelType | None:
        """
        Retrieve an entity by its primary key.
        """
        return self.session.get(self.model, entity_id)

    def list(
        self,
    ) -> list[ModelType]:
        """
        Retrieve all entities.
        """
        stmt = select(self.model)
        return list(self.session.scalars(stmt).all())

    def create(
        self,
        entity: ModelType,
    ) -> ModelType:
        """
        Persist a new entity.
        """
        self.session.add(entity)
        self.session.flush()
        return entity

    def delete(
        self,
        entity: ModelType,
    ) -> None:
        """
        Delete an entity.
        """
        self.session.delete(entity)

    def exists(
        self,
        entity_id: int,
    ) -> bool:
        """
        Check whether an entity exists.
        """
        return self.get_by_id(entity_id) is not None