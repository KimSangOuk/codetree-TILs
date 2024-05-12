class Agent:
    def __init__(self, name, score):
        self.name=name
        self.score=score

agents=[]
min_score=101
min_index=-1
for i in range(5):
    name,score=map(str,input().split())
    agents.append(Agent(name,int(score)))
    if int(score)<min_score:
        min_score=int(score)
        min_index=i

print(agents[min_index].name,agents[min_index].score)