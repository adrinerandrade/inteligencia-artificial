from random import randint

class Mutation:
    def __init__(self, chromosome):
        self.chromosome = chromosome

    # Realiza a mutação em um cromossomo
    def mutate(self):
        genes = self.chromosome.get_cities()
        gene_1 = randint(0, len(genes) - 1)
        gene_2 = randint(0, len(genes) - 1)
        tmp = genes[gene_1]
        genes[gene_1] = genes[gene_2]
        genes[gene_2] = tmp