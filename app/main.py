class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]
    for p in people:
        inst = Person.people[p["name"]]
        wife_name = p.get("wife")
        husband_name = p.get("husband")
        if wife_name:
            inst.wife = Person.people[wife_name]
        if husband_name:
            inst.husband = Person.people[husband_name]
    return person_list
