# #!/usr/bin/env python
# # coding: utf-8

# # In[5]:


# import math
# import random
# import copy


# # In[6]:


# class individual:
#     def __init__(self,code,startArray):
#         self.codeWeight=1
#         self.breakPointsWeight=5
#         self.code=code
#         self.array = []
#         self.startArray = startArray
#         self.applyReversals()
#         self.breakpoints=self.getBreakpoints()
#         self.fitness=self.calculateFitnes()
        
#     def applyReversals(self):
#         self.array = copy.deepcopy(self.startArray)
#         for k in range(0,len(self.code),2):
#             i = self.code[k]
#             j = self.code[k+1]
#             for l in range(int((j-i+1)/2)):
#                 self.array[i+l],self.array[j-l] = self.array[j-l],self.array[i+l]

#     def getBreakpoints(self):
#         breakPoints=0
#         for i in range(1,len(self.array)-1):
#             if abs(self.array[i-1]-self.array[i])>1:
#                 breakPoints+=1
#         return breakPoints
#     def calculateFitnes(self):
#         return self.breakPointsWeight*self.breakpoints+self.codeWeight*len(self.code)


# # In[7]:


# class MSR:
#     def __init__(self,array):
#         self.populationSize=math.floor(len(array)*math.log(len(array))) #Velicina populacije je floor(n*log n)
#         self.array=array
#         self.breakPoints=self.getBreakpoints()
#         self.population=[]
#         self.initializePopulation()
#         self.tournamentSize=math.ceil(0.15*self.populationSize)
#         self.bestUnit = self.population[0]
#         self.mutationRate = 0.01
#         self.numOfIters = 1000000000
#     def getBreakpoints(self):
#         breakPoints=0
#         for i in range(1,len(self.array)-1):
#             if abs(self.array[i-1]-self.array[i])>1:
#                 breakPoints+=1
#         return breakPoints
#     def generateIndividual(self,size):
#         code=[]
#         for i in range(size):
#             m=math.ceil(random.randrange(1,math.ceil(len(self.array)/10)+1))
#             n=math.ceil(random.randrange(0,math.ceil(9*len(self.array)/10-1)))
#             begin=n
#             end=m+n
#             code.append(begin)
#             code.append(end)
#         return individual(code,self.array)
            
#     def initializePopulation(self):
#         lowerBound=self.breakPoints
#         upperBound=len(self.array)
#         for i in range(self.populationSize):
#             size=random.randrange(lowerBound,upperBound+1)
#             self.population.append(self.generateIndividual(size))
#     def selection(self):
#         selected=random.sample(self.population,self.tournamentSize)
#         best=min(selected,key=lambda x:x.fitness)
#         return best
#     def crossover(self,parent1,parent2):
#         if len(parent1)==len(parent2):
#             while(True):
#                 firstPoint=random.randrange(0,len(parent1))
#                 secondPoint=random.randrange(0,len(parent1))
#                 if firstPoint!=secondPoint:
#                     break
#             if firstPoint>secondPoint:
#                 firstPoint,secondPoint=secondPoint,firstPoint
#             child1=parent1[:firstPoint]+parent2[firstPoint:secondPoint]+parent1[secondPoint:]
#             child2=parent2[:firstPoint]+parent1[firstPoint:secondPoint]+parent2[secondPoint:]
#         else:
#             if len(parent1)<len(parent2):
#                 parent1,parent2=parent2,parent1
#             point=random.randrange(0,len(parent1)-len(parent2)+1)
#             child1=parent1[:point]+parent2+parent1[point+len(parent2):]
#             child2=parent1[point:point+len(parent2)]
#         return individual(child1,self.array),individual(child2,self.array)

#     def mutation(self,unit):
#         while(True):
#             i = random.randrange(0,int(len(unit.code)/2))
#             j = random.randrange(0,int(len(unit.code)/2))
#             if i !=j:
#                 break
#         if j < i :
#             i,j = j,i
#         i = 2*i
#         j = 2*j
#         for k in range(j,len(unit.code)-1):
#             unit.code[k] = unit.code[k+1]
#         del unit.code[-1]
#         for k in range(i,len(unit.code)-1):
#             unit.code[k] = unit.code[k+1]
#         del unit.code[-1]

#         unit.applyReversals()
#         unit.breakPoints = unit.getBreakpoints()
#         unit.fitness = unit.calculateFitnes()

#     def generatePopulation(self):
#         population = []
#         for i in range(0,self.populationSize,2):
#             parent1 = self.selection()
#             parent2 = self.selection()
#             child1,child2 = self.crossover(parent1.code,parent2.code)
#             if random.random() < self.mutationRate:
#                 self.mutation(child1)
#             if random.random() < self.mutationRate:
#                 self.mutation(child2)
#             population.append(child1)
#             population.append(child2)
#         self.population = population
#         return population

#     def findBest(self):
#         best=min(self.population,key=lambda x:x.fitness)
#         return best

#     def solve(self):
#         self.initializePopulation()
#         for i in range(self.numOfIters):
#             best = self.findBest()
#             if best.fitness < self.bestUnit.fitness:
#                 self.bestUnit = best
#             if i%20 == 0:
#                 print("Najbolja jedinka:\nFitness: " + str(self.bestUnit.fitness) + "\nBrojInverzija: " + str(len(self.bestUnit.code)/2))
#             self.generatePopulation()
#             print(i)
#         print("Gotovo")
#         print("Najbolja jedinka:\nFitness: " + str(self.bestUnit.fitness) + "\nBrojInverzija: " + str(len(self.bestUnit.code)/2))


# # In[8]:


# msr=MSR([5,1,3,6,4,2,7])
# msr.solve()


# # In[ ]:


# #num(breakpoint)+length(code)

