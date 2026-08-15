from collections import deque

class SocialNetwork:

    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = set()
            print(user, "added successfully.")
        else:
            print(user, "already exists.")

    def add_friend(self, user1, user2):
        if user1 not in self.graph:
            self.add_user(user1)

        if user2 not in self.graph:
            self.add_user(user2)

        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

        print("Friendship added between", user1, "and", user2)

    def display_network(self):
        print("\n--- Social Network ---")

        for user in self.graph:
            print(user, "->", ", ".join(self.graph[user]))

    def mutual_friends(self, user1, user2):

        if user1 not in self.graph or user2 not in self.graph:
            return set()

        return self.graph[user1].intersection(self.graph[user2])

   
    def recommend_friends(self, user):

        if user not in self.graph:
            print("User not found.")
            return

        recommendations = {}

     
        for friend in self.graph[user]:

            for friend_of_friend in self.graph[friend]:

                if (friend_of_friend != user and
                        friend_of_friend not in self.graph[user]):

                    if friend_of_friend not in recommendations:
                        recommendations[friend_of_friend] = 0

                    recommendations[friend_of_friend] += 1

        if not recommendations:
            print("No friend recommendations available.")
            return

       
        recommendations = sorted(
            recommendations.items(),
            key=lambda x: x[1],
            reverse=True
        )

        print("\n--- Friend Recommendations for", user, "---")

        for person, count in recommendations:
            print(person, "-", count, "mutual friend(s)")

    def bfs(self, start):

        if start not in self.graph:
            print("User not found.")
            return

        visited = set()
        queue = deque([start])

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


network = SocialNetwork()

users = ["Purvesh", "Rahul", "Aman", "Riya", "Sneha", "Karan"]

for user in users:
    network.add_user(user)

network.add_friend("Purvesh", "Rahul")
network.add_friend("Purvesh", "Riya")

network.add_friend("Rahul", "Aman")
network.add_friend("Rahul", "Sneha")

network.add_friend("Riya", "Sneha")
network.add_friend("Sneha", "Karan")

network.display_network()

network.recommend_friends("Purvesh")

network.bfs("Purvesh")

print("\nMutual friends between Rahul and Riya:",
      network.mutual_friends("Rahul", "Riya"))