import math

class DiscoZooState:

    ROWS = 5
    COLS = 5

    HEURISTIC = "zero"
    VALID_HEURISTICS = ("zero", "maxClicks", "disjoint")

    def __init__(self, parent, remaining_placements,last_click):
        self.remaining_placements = remaining_placements
        self.last_click = last_click
        self.parent = parent

    @classmethod
    def set_grid_dimensions(cls, rows, cols):
        cls.ROWS=rows
        cls.COLS=cols

    @classmethod
    def set_heuristic(cls,heuristic):
        if heuristic not in cls.VALID_HEURISTICS:
            raise ValueError(f"Unknown heuristic {heuristic!r}. Valid heuristics: {cls.VALID_HEURISTICS}")
        cls.HEURISTIC = heuristic
        


    @property
    def gCost(self):
        return self.parent.gCost + 1 if self.parent else 0

    @property
    def f(self):
        return self.gCost + self.h()

     

    def getChildren(self):

        children = set()

        ## seperate the unique tiles of all the placements
        ## i did a double loop previously looping through every possible click. 
        ## but some tiles can exist on many patterns at the same time. 
        ## thus producing more child states for the same clicks,
        ## slowing down the algorithm

        unique_clicks = {tile for placement in self.remaining_placements for tile in placement}

        for click in unique_clicks:

            ## survivors needs to be a frozenset so that it is hashable
            survivors = frozenset(p for p in self.remaining_placements if click not in p)


            child = DiscoZooState(self, survivors, click)

            children.add(child)

        return frozenset(children)

    ## we have to define these methods so that the states are compared based on the remaining placements
    ## and not memory addresses etc.
    def __eq__(self, other):
        if not isinstance(other, DiscoZooState):
            return False
        return self.remaining_placements == other.remaining_placements

    def __hash__(self):
        return hash(self.remaining_placements)

    def __lt__(self,other):

        # compare the f score first
        if (self.f != other.f):
            return self.f < other.f
        elif (len(self.remaining_placements) != len(other.remaining_placements)):
            # if equal, choose the one with the least remaining_placements first
            # example: child1_f = 1 + ceil(5/4) = 3 child2_f = 1 + (6/4)=3
            # here, 4 is the pattern size, 1 is the gCost and 5 and 6 are the remaining placements
            # for child_1 and child_2 respectively
            
            return len(self.remaining_placements) < len(other.remaining_placements)
        else:
            return self.distanceFromCenter() < other.distanceFromCenter()

    def h_zero(self):
        return 0
    
    def h_maxClicks(self):

        
        remaining = len(self.remaining_placements)

        
        if remaining == 0:
            return 0
        
        pattern_size = len(next(iter(self.remaining_placements)))

        return math.ceil(remaining/pattern_size)

    def h_disjoint(self):
        disjointSets = set()
        count = 0;
        for placement in self.remaining_placements:
            if placement.isdisjoint(disjointSets):
                count+=1
                disjointSets = disjointSets.union(placement)
        return count

    def h(self):
        return getattr(self,f"h_{self.HEURISTIC}")()
    
    def isFinal(self):
        return len(self.remaining_placements) == 0

    def get_coords(self):
        return str(self.last_click)

    def distanceFromCenter(self):
        if self.last_click is None:
            return 0

        mid_row = (DiscoZooState.ROWS-1)//2
        mid_col = (DiscoZooState.COLS-1)//2
        r,c = self.last_click
        return abs(r-mid_row) + abs(c-mid_col)

