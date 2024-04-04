import random

class Gene:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def mutate_weight(self):
        if random.uniform(0, 1) < 0.1:
            self.weight = random.uniform(-1, 1)
        else: 
            self.weight+= random.gauss(0, 1)/10 #mean at 0, deviane by 1
            if self.weight > 1:
                self.weight = 1
            elif self.weight < -1:
                self.weight = -1
        
    def clone(self, from_node, to_node):
        clone = Gene(from_node, to_node, self.weight)
        return clone