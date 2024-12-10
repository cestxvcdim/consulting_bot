from model import User


class UserDAO:
    """
    This class is the 3rd layer, which works with a database only.

    Methods of the class address to the database
    And get data from there
    Or put data there.
    """
    def __init__(self, session):
        """Defines a database's session."""
        self.session = session

    def get_one(self, uid):
        """Returns object by id from the database."""

        return self.session.query(User).get(uid)

    def get_all(self):
        """Returns all objects from the database."""

        return self.session.query(User).all()

    def create(self, data):
        """
        Create new object of model
        And put him in the database.

        Returns the created object.
        """

        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user):
        """
        Put transferred object to the database
        And update him in this way.

        Nothing returns.
        """

        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        """
        Get object by id from the database
        And delete him from there.

        Nothing returns.
        """

        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()
