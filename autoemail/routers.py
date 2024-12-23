class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """Direct read queries for the birthday model to MySQL."""
        if model._meta.app_label == 'autoemail':
            return 'mysql_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """Direct write queries for the birthday model to MySQL."""
        if model._meta.app_label == 'autoemail':
            return 'mysql_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if both objects are in the same database."""
        db_set = {'mysql_db', 'default'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the birthday model is migrated only in MySQL."""
        if app_label == 'autoemail':
            return db == 'mysql_db'
        return db == 'default'
