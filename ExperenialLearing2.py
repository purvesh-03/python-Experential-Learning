from collections import deque


class SocialNetwork:

    def __init__(self):
        self.graph = {}

    # Add user
    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = set()
            print(user, "added successfully.")
        else:
            print(user, "already exists.")

    # Add friendship
    def add_friend(self, user1, user2):

        if user1 not in self.graph:
            self.add_user(user1)

        if user2 not in self.graph:
            self.add_user(user2)

        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

        print("Friendship added between", user1, "and", user2)

    # Display network
    def display_network(self):

        print("\n--- SOCIAL NETWORK ---")

        for user in self.graph:
            print(user, "->", end=" ")

            if self.graph[user]:
                print(", ".join(self.graph[user]))
            else:
                print("No friends")

    # Find mutual friends
    def mutual_friends(self, user1, user2):

        if user1 not in self.graph or user2 not in self.graph:
            print("User not found.")
            return

        mutual = self.graph[user1] & self.graph[user2]

        print("\nMutual friends between", user1, "and", user2, ":")

        if mutual:
            print(", ".join(mutual))
        else:
            print("No mutual friends.")

    # Recommend friends
    def recommend_friends(self, user):

        if user not in self.graph:
            print("User not found.")
            return

        recommendations = {}

        # Check friends of friends
        for friend in self.graph[user]:

            for person in self.graph[friend]:

                if person != user and person not in self.graph[user]:

                    if person not in recommendations:
                        recommendations[person] = 0

                    recommendations[person] += 1

        print("\n--- FRIEND RECOMMENDATIONS ---")

        if not recommendations:
            print("No recommendations available.")
            return

        # Sort by mutual friends
        result = sorted(
            recommendations.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for person, count in result:
            print(person, "-", count, "mutual friend(s)")

    # BFS Traversal
    def bfs(self, start):

        if start not in self.graph:
            print("User not found.")
            return

        visited = set()
        queue = deque()

        queue.append(start)

        print("\nBFS Traversal:")

        while queue:

            current = queue.popleft()

            if current not in visited:

                print(current, end=" ")
                visited.add(current)

                for friend in self.graph[current]:

                    if friend not in visited:
                        queue.append(friend)

        print()

    # Shortest connection using BFS
    def shortest_connection(self, start, target):

        if start not in self.graph or target not in self.graph:
            print("User not found.")
            return

        queue = deque()
        visited = set()

        queue.append((start, 0))
        visited.add(start)

        while queue:

            current, distance = queue.popleft()

            if current == target:

                print(
                    "\nMinimum connections between",
                    start,
                    "and",
                    target,
                    "=",
                    distance
                )

                return

            for friend in self.graph[current]:

                if friend not in visited:

                    visited.add(friend)
                    queue.append((friend, distance + 1))

        print("No connection found.")


# ---------------------------------
# MAIN PROGRAM
# ---------------------------------

network = SocialNetwork()

# Add users
network.add_user("Purvesh")
network.add_user("Rahul")
network.add_user("Aman")
network.add_user("Riya")
network.add_user("Sneha")
network.add_user("Karan")

# Add friendships
network.add_friend("Purvesh", "Rahul")
network.add_friend("Purvesh", "Riya")

network.add_friend("Rahul", "Aman")
network.add_friend("Rahul", "Sneha")

network.add_friend("Riya", "Sneha")

network.add_friend("Sneha", "Karan")


# Display network
network.display_network()

# Friend recommendations
network.recommend_friends("Purvesh")

# Mutual friends
network.mutual_friends("Rahul", "Riya")

# BFS
network.bfs("Purvesh")

# Shortest connection
network.shortest_connection("Purvesh", "Karan")