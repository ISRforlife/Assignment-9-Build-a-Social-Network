class Person:
    """Represents one person and their friends in the network."""

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Avoid adding the same friend twice.
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    """Stores people and their two-way friendships as a graph."""

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return
        if person1_name == person2_name:
            print("A person cannot be friends with themselves!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(names) if names else 'no one yet'}")


if __name__ == "__main__":
    network = SocialNetwork()

    # Add six people to the network.
    for name in ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]:
        network.add_person(name)

    # Add eight two-way friendships.
    friendships = [
        ("Alex", "Jordan"),
        ("Alex", "Morgan"),
        ("Jordan", "Taylor"),
        ("Morgan", "Casey"),
        ("Taylor", "Riley"),
        ("Casey", "Riley"),
        ("Morgan", "Riley"),
        ("Alex", "Taylor"),
    ]
    for person1, person2 in friendships:
        network.add_friendship(person1, person2)

    print("Testing a missing person:")
    network.add_friendship("Jordan", "Johnny")

    print("\nTesting a duplicate person:")
    network.add_person("Alex")

    print("\nTesting a duplicate friendship:")
    network.add_friendship("Alex", "Jordan")

    print("\nTesting a friendship with yourself:")
    network.add_friendship("Alex", "Alex")

    print("\nFinal social network:")
    network.print_network()
