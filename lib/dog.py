import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    all = []
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
            );
        """

        cls.all = CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS dogs;
        """

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO dogs (name, breed) VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.breed))
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM dogs").fetchone()[0]

    @classmethod
    def create(cls, name, breed):
        dog = Dog(name, breed)
        dog.save()

        return dog

    @classmethod
    def new_from_db(cls, row):
        dog = cls(row[1], row[2])
        dog.id = row[0]
        return dog

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM dogs
        """

        dogs = CURSOR.execute(sql).fetchall()
        all = [cls.new_from_db(dog) for dog in dogs]
        return all

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM dogs
            WHERE name = ?
        """

        dog = CURSOR.execute(sql, (name,)).fetchone()
        if dog:
            return cls.new_from_db(dog)

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM dogs
            WHERE id = ?
        """

        dog = CURSOR.execute(sql, (id,)).fetchone()
        return cls.new_from_db(dog)

    @classmethod
    def find_or_create_by(cls, name, breed):
        dog = cls.find_by_name(name)
        
        if not dog:
            dog = cls.create(name, breed)
            
        return dog

    def update(self):
        sql = """
            UPDATE dogs
            SET name = ?, breed = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.breed, self.id))

""" 

Class Dog in dog.py initializes with name and breed attributes.
Class Dog in dog.py contains method "create_table()" that creates table "dogs" if it does not exist.
Class Dog in dog.py contains method "drop_table()" that drops table "dogs" if it exists.
Class Dog in dog.py contains method "save()" that saves a Dog instance to the database.
Class Dog in dog.py contains method "create()" that creates a new row in the database and returns a Dog instance.
Class Dog in dog.py contains method "new_from_db()" that takes a database row and creates a Dog instance.
Class Dog in dog.py contains method "get_all()" that returns a list of Dog instances for every record in the database.
Class Dog in dog.py contains method "find_by_name()" that returns a Dog instance corresponding to its database record retrieved by name.
Class Dog in dog.py contains method "find_by_id()" that returns a Dog instance corresponding to its database record retrieved by id.
Class Dog in dog.py contains method "find_or_create_by()" that takes a name and a breed as arguments and creates a Dog instance matching that record if it does not exist.
Class Dog in dog.py contains a method "save()" that saves a Dog instance to the database and returns a Dog instance with id.
Class Dog in dog.py contains a method "update()" that updates an instance's corresponding database record to match its new attribute values.

"""