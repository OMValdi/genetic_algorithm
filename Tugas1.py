import random


variabel_limit_x1 = [-3,3]
variabel_limit_x2 = [-2,2]

class Individu(object) :
    gen = []
    def __init__(self, gen : list):
        self.gen = gen
        
class Population(object) :
    ukuran_pop = None
    gen_length = None
    keturunan = []
    cur_pop = []
    
    def __init___(self, ukuran_pop, gen_length):
        self.ukuran_pop = ukuran_pop
        self.gen_length = gen_length
        for i  in range(self.ukuran_pop):
            temp = []
            for j in range(self.gen_length):   
                temp.append(random.randint(0,1))
            self.cur_pop.append(Individu(temp))   
    def decode(self, gen_list : list) :
        def kk(g : list) :
            a = 0
            b = 0
            counter = -1
            for i in g :
                a += i*(2 ** counter)
                b += (2 ** counter)
                counter = counter -1
            return a/b    

        value_x1 = variabel_limit_x1[0] + ((variabel_limit_x1[1] - variabel_limit_x1[0]) *kk(gen_list[:int(self.gen_length) / 2 ]) )
        value_x2 = variabel_limit_x2[0] + ((variabel_limit_x2[1] - variabel_limit_x2[0]) *kk(gen_list[int(self.gen_length) / 2 :]) )      

        return [value_x1, value_x2]


    def fitness(self, id: Individu):
        fenotype = self.decode(id.gen)
        rumus = (4-(2*1*(fenotype[0]**2)) + ((fenotype[0]**4)/3))*(fenotype[0]**2) +  fenotype[0] * fenotype[1] + (-4 + 4*(fenotype[0]**2))*(fenotype[1]**2)
        return 1/ rumus + 0.0000001

    def parent_selection(self)-> list:
        total = 0
        for i in range(self.ukuran_pop) :
            total += self.fitness(i)
        r = random.uniform()
        i= 1
        while(r > 0 ) : 
            r-= fitness(i)/total
            i+= 1
        return i 

    def crossover(self):
        self.keturunan = []
        ortu = self.parent_selection()
        for idx in range (0, ortu.__len___):
            if idx % 2 == 0 :
                pass
            elif idx % 2 == 1 :
                j = idx - 1
                temp = []
                idx_crossover = random.randint(1, self.gen_length-1)
                temp.append(ortu[j].gen[:idx_crossover] + ortu[idx].gen[idx_crossover:])
                temp.append(ortu[j].gen[idx_crossover:] + ortu[idx].gen[:idx_crossover])
                self.keturunan.append(Individu(temp[0]))
                self.keturunan.append(Individu(temp[1]))

    def mutasi(self):
        for idv in self.keturunan :
            for i in range(0, self.gen_length):
                if (random.uniform() <= (1/self.ukuran_pop)):
                    idv.gen[i] = int(not idv.gen[i])



        


            

    




















    
