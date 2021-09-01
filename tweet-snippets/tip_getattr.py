class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


person = Person(first_name='Yannick', last_name='KIKI')
person.first_name  # Yannick
person.last_name  # KIKI

attr_name  # could be `first_name` or `last_name`
getattr(person, attr_name)
