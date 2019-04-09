from random import randint
from queue import *

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # while the number of friendships is less than the total number of users
        if not numUsers > avgFriendships:
            avgFriendships = numUsers - 1
        # Add users
        for num in range(1, numUsers + 1):
            self.addUser(num)

        # Create friendships
        all_friendships = (numUsers * avgFriendships) // 2
        friendships = []

        while len(friendships) < all_friendships:
            #generate all possible friendship combinations
            possibilities = sorted([randint(1, numUsers), randint(1, numUsers)])
            # discard if friends with themselves
            if possibilities [0] == possibilities [1]:
                continue
            # discard if friendship already exists
            if possibilities in friendships:
                continue
            
            # add friendship 
            friendships.append(possibilities)
        
        for friendship in friendships:
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()
        queue.put([userID])

        while not queue.empty():
            current_path = queue.get()
            current = current_path[-1]
            if current not in visited:
                visited[current] = current_path
                for item in self.friendships[current]:
                    if item not in visited:
                        queue.put(list(current_path) + [item])
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
