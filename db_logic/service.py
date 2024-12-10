from db_logic.dao import UserDAO


class UserService:
    """
    This class is 2nd layer, which works with business-logic of the application.

    Methods of the class handle a data
    And give this to next layer.
    """
    def __init__(self, dao: UserDAO):
        """Defines DAO for working with database's session."""

        self.dao = dao

    def get_one(self, lid):
        """Returns object by id."""

        return self.dao.get_one(lid)

    def get_all(self):
        """Returns all objects"""

        return self.dao.get_all()

    def create(self, data):
        """Create new object of model."""

        return self.dao.create(data)

    def update(self, data, uid):
        """Update object fully."""

        user = self.dao.get_one(uid)

        user.fullname = data.get("fullname")
        user.tg_id = data.get("tg_id")
        user.tg_name = data.get("tg_name")

        self.dao.update(user)

    def update_partial(self, data, uid):
        """Update object partially."""

        user = self.get_one(uid)

        if "fullname" in data:
            user.fullname = data.get("fullname")
        if "tg_id" in data:
            user.tg_id = data.get("tg_id")
        if "tg_name" in data:
            user.tg_name = data.get("tg_name")

        self.dao.update(user)

    def delete(self, uid):
        """Delete object."""

        self.dao.delete(uid)
