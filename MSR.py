import math
import random

class individual:
    def __init__(self,code,startArray):
        self.codeWeight=2
        self.breakPointsWeight=1
        self.code=code
        self.array=startArray
        self.breakpoints=self.getBreakpoints()
        self.fitness=self.calculateFitnes()
        
    def getBreakpoints(self):
        breakPoints=0
        for i in range(1,len(self.array)-1):
            if abs(self.array[i-1]-self.array[i])>1:
                breakPoints+=1
        return breakPoints
    def calculateFitnes(self):
        return self.breakPointsWeight*self.breakpoints+self.codeWeight*len(self.code)



class MSR:
    def __init__(self,array):
        
        self.populationSize=math.floor(len(array)*math.log(len(array))) #Velicina populacije je floor(n*log n)
        self.array=array
        self.breakPoints=self.getBreakpoints()
        self.population=[]
        self.initializePopulation()
       
        self.tournamentSize=math.ceil(0.15*self.populationSize)
    def getBreakpoints(self):
        breakPoints=0
        for i in range(1,len(self.array)-1):
            if abs(self.array[i-1]-self.array[i])>1:
                breakPoints+=1
        return breakPoints
    def generateIndividual(self,size):
        code=[]
        for i in range(size):
            m=math.ceil(random.randrange(1,math.ceil(len(self.array)/10)+1))
            n=math.ceil(random.randrange(0,math.ceil(9*len(self.array)/10-1)))
            begin=n
            end=m+n
            code.append(begin)
            code.append(end)
        return individual(code,self.array)
            
    def initializePopulation(self):
        lowerBound=self.breakPoints
        upperBound=len(self.array)
        for i in range(self.populationSize):
            size=random.randrange(lowerBound,upperBound+1)
            self.population.append(self.generateIndividual(size))
    def selection(self):
        selected=random.sample(self.population,self.tournamentSize)
        best=min(selected,key=lambda x:x.fitness)
        return best
    def crossover(self,parent1,parent2):
        if len(parent1)==len(parent2):
            while(True):
                firstPoint=random.randrange(0,len(parent1))
                secondPoint=random.randrange(0,len(parent1))
                if firstPoint!=secondPoint:
                    break
            if firstPoint>secondPoint:
                firstPoint,secondPoint=secondPoint,firstPoint
            child1=parent1[:firstPoint]+parent2[firstPoint:secondPoint]+parent1[secondPoint:]
            child2=parent2[:firstPoint]+parent1[firstPoint:secondPoint]+parent2[secondPoint:]
        else:
            if len(parent1)<len(parent2):
                parent1,parent2=parent2,parent1
            point=random.randrange(0,len(parent1)-len(parent2)+1)
            child1=parent1[:point]+parent2+parent1[point+len(parent2):]
            child2=parent1[point:point+len(parent2)]
        return individual(child1,self.array),individual(child2,self.array)
