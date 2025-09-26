import heapq


# Node class to store coordinates and costs
class Node:
   def __init__(self, x, y, g=0, h=0, parent=None):
       self.x = x
       self.y = y
       self.g = g  # Cost from start to node
       self.h = h  # Heuristic cost from node to goal
       self.f = g + h  # Total cost
       self.parent = parent


   def __lt__(self, other):
       return self.f < other.f


# Heuristic function (Manhattan Distance)
def heuristic(current, goal):
   return abs(current.x - goal.x) + abs(current.y - goal.y)


# Helper function to check if a node is walkable
def is_walkable(grid, x, y):
   return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0


# A* search algorithm
def a_star(grid, start, goal):
   open_list = []
   closed_set = set()


   start_node = Node(start[0], start[1])
   goal_node = Node(goal[0], goal[1])
   start_node.h = heuristic(start_node, goal_node)
   start_node.f = start_node.g + start_node.h


   heapq.heappush(open_list, start_node)


   while open_list:
       current = heapq.heappop(open_list)


       if (current.x, current.y) == (goal_node.x, goal_node.y):
           path = []
           while current:
               path.append((current.x, current.y))
               current = current.parent
           return path[::-1]


       closed_set.add((current.x, current.y))


       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           neighbor_x, neighbor_y = current.x + dx, current.y + dy


           if (neighbor_x, neighbor_y) in closed_set or not is_walkable(grid, neighbor_x, neighbor_y):
               continue


           g = current.g + 1
           neighbor_node = Node(neighbor_x, neighbor_y, g)
           neighbor_node.h = heuristic(neighbor_node, goal_node)
           neighbor_node.f = neighbor_node.g + neighbor_node.h
           neighbor_node.parent = current


           heapq.heappush(open_list, neighbor_node)


   return None  # No path found


# Example grid: 0 = walkable, 1 = obstacle
grid = [
   [0, 0, 0, 1, 0],
   [0, 1, 0, 1, 0],
   [0, 1, 0, 0, 0],
   [0, 0, 0, 1, 0],
   [1, 0, 0, 0, 0]
]


start = (0, 0)
goal = (4, 4)


path = a_star(grid, start, goal)
print("Path:", path)

