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
    parent_select = []
    
    def __init__(self, ukuran_pop, gen_length):
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
       
        value_x1 = variabel_limit_x1[0] + ((variabel_limit_x1[1] - variabel_limit_x1[0]) *kk(gen_list[:int(self.gen_length/2) ]) )
        value_x2 = variabel_limit_x2[0] + ((variabel_limit_x2[1] - variabel_limit_x2[0]) *kk(gen_list[int(self.gen_length/2):]) )      

        return [value_x1, value_x2]


    def fitness(self, id: Individu):
        fenotype = self.decode(id.gen)
        rumus = (4-(2*1*(fenotype[0]**2)) + ((fenotype[0]**4)/3))*(fenotype[0]**2) +  fenotype[0] * fenotype[1] + (-4 + 4*(fenotype[0]**2))*(fenotype[1]**2)
        return 1/ rumus + 0.000001

    def max_fitness(self,max_list : list) -> int :
        max = None
        for i in range(0, len(max_list)):
            if max == None :
                max = i 
            elif (self.fitness(max_list[max])< self.fitness(max_list[i])):
                max = i        
        return max
    def parent_selection(self):
        self.parent_select = []
        parent =int(0.25 * self.ukuran_pop)
        select = []
        for id in self.cur_pop:
            for i in range(0, int(self.fitness(id))):
                select.append(id.gen)
            random_parent = []    
        for i in range(0,parent):
             random_parent.append(random.choice(select))
        self.parent_select = random_parent
    def ortu(self, id : int)-> Individu :
        for i in self.cur_pop:
            if(i.gen == id):
                return i    
        return None        


    def crossover(self):
        self.keturunan = []
        
        for idx in range (0,len(self.parent_select)-1):
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
    
    def survivor_selection(self):
        temp = self.cur_pop[:] + self.keturunan[:]
        temp_list = []
        while temp != [] :
            temp_list.append(temp.pop(self.max_fitness(temp)))
        self.cur_pop = temp_list[:self.ukuran_pop]
        self.keturunan = []
        for i in self.cur_pop :
            print('Mutasi Gen  : ')
            print(i.gen)     
   
    def new_gen(self, generation):
        for i in range(0, generation):
            self.crossover()
            self.survivor_selection()
    def print_fitness(self):
        nilai = self.cur_pop[self.max_fitness(self.cur_pop)]
        print('Gen : %s'% str(nilai.gen)) 
        print('Fenotype : %s'% str(self.decode(nilai.gen)))
        print('Fitness : %s' % str(self.fitness(nilai)))        
            

if __name__ == '__main__':
    populasi = Population(ukuran_pop = 3, gen_length=17)
    print('Generasi Awal : ')
    populasi.print_fitness()
    populasi.new_gen(3)
    print('Generasi Baru : ')
    populasi.print_fitness()
