from src.Point import Point
from src.Pokemon import Pokemon
import networkx as nx



class Agent:

    def __init__(self, id: int = 0, value: float = 0, src: int = 0, dest: int = 0, speed: float = 0,
                 pos: Point = Point(), jsonStr=None):
        if jsonStr is not None:
            self.parseAgent(jsonStr)
        else:
            self.id = id
            self.value = value  # how many did the agent eat till now
            self.dest = dest
            self.src = src
            self.speed = speed
            self.pos = pos
        self.path = []
        self.timeStamps = []

    def parseAgent(self, jsonStr):
        """Function receives json object of pokemon and parses it, assigning values to current pokemon"""
        self.id = jsonStr['id']
        self.value = jsonStr['value']
        self.src = jsonStr['src']
        self.dest = jsonStr['dest']
        self.speed = jsonStr['speed']
        self.pos = Point(jsonStr['speed'])

    def __str__(self):
        return "{id: " + str(self.id) + ", value: " + str(self.value) + ", src: " + str(self.src) + ", dest: " + str(
            self.dest) + ", speed: " + str(self.speed) + ", pos: " + str(self.pos) + ", path: " + str(self.path)

    def __repr__(self):
        return self.__str__()

    def getId(self):
        """get the id of the agent"""
        return self.id

    def getValue(self):
        """get the value of the agent"""
        return self.value

    def get_speed(self):
        """get the speed of the agent"""
        return self.speed

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos

    def getSrc(self):
        return self.src

    def setSrc(self, src):
        self.src = src

    def getDest(self):
        return self.dest

    def setDest(self, dest):
        self.dest = dest

    def addToPath(self, nodeId):
        """Set the path the agent need to move on to get the pokemon as fast as he can"""
        self.path.append(nodeId)

    def getPathHead(self):
        return self.path[0]

    def getTimeStamps(self):
        return self.timeStamps

    def setTimeStamps(self, time):
        self.timeStamps = time

    def addTimeStamp(self, time):
        self.timeStamps.append(time)

    def removeHeadTimeStamp(self):
        temp = self.timeStamps[0]
        self.timeStamps.pop(0)
        return temp

    def getPath(self):
        """Get the path the agent need to moove on to get the pokemon as fast as he can"""
        return self.path

    # def GetAgentsList(self):
    #     """Get a list of all the Agents"""

    def is_moving(self):  # TODO
        """If the agent is moving on edges"""

    def get_current_edge(self):  # TODO
        """retur the edge that the agent is currently on"""


    def calculateTime(self, pokemon: Pokemon, graph: nx.DiGraph): #total time to
        total_time= self.speed/ graph.edges.get(pokemon.node_src)


