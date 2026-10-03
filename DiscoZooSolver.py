## this is it
import heapq
from Utils import findPlacements
from DiscoZooState import DiscoZooState

class DiscoZooSolver:

    @staticmethod
    def aStarSolver(initialState):

        frontier = []

        closedSet = set()

        initialState.evaluate()
        
        heapq.heappush(frontier,initialState)

        while len(frontier) > 0: # same as while len(frontier) > 0

            current = heapq.heappop(frontier)

            if (current.isFinal()):
                return current

            if current in closedSet:
                continue

            closedSet.add(current)
            
            for child in current.getChildren():

                
                if child in closedSet:
                    continue

               

                heapq.heappush(frontier,child)

        return None

    @staticmethod
    def backtrack(final_state):

        temp = final_state
        
        raw_clicks = []
        while temp.parent is not None:
            
            raw_clicks.append(temp.last_click)
            temp=temp.parent

        
        raw_clicks.reverse()
        
        for i,click in enumerate(raw_clicks,1):
            print(f"Click {i}: {click}")
           

    @staticmethod
    def backtrackUI(final_state):
    
        temp = final_state
            
        raw_clicks = []
        while temp.parent is not None:
                
            raw_clicks.append(temp.last_click)
            temp=temp.parent
    
        raw_clicks.reverse()  
        
        
        for i,click in enumerate(raw_clicks,1):
            print(f"Click {i}: {click[0]+1},{click[1]+1}")
            i+=1


if __name__ == "__main__":
    koala = [(0,0), (0,1), (1,1)]
    horse = [(0,0),(1,0),(2,0)]
    
    koala_placements = findPlacements(koala)
    

    initialState = DiscoZooState(None,koala_placements,None)

    sol = DiscoZooSolver.aStarSolver(initialState)

    if (sol is not None):
        DiscoZooSolver.backtrack(sol)
    else:
        print("No solution found?? Why?")

    # hippo = [(0, 0), (2,0),(0,2),(2,2)]
    # hippo_placements = findPlacements(hippo)
    # initialStateHippo = DiscoZooState(None,hippo_placements,None)
    # hippo_sol = DiscoZooSolver.aStarSolver(initialStateHippo)

    # print(f"\n\n---SASQUATCH SOLUTION---")
    # if (hippo_sol is not None):
    #     DiscoZooSolver.backtrack(hippo_sol)

    # else:
    #     print("No solution found?? Why?")





