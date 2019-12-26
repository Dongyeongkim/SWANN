
import os
import random as rd
import src.SNN as SNN
import src.NEAT as NEAT
import src.Genetic as Genetic
import src.ribosome as ribosome


Generation_num = int(input("Input the number of testing generations"))

for i in range(Generation_num):
    gene_list = Genetic.Read_Gene()
    score_set = [-2, -1, 1, 2]
    gene_score_list = []
    real_score = []
    selected_gene = []
    descendants_gene = []
    for score in score_set:
        partial_score_list = []
        ribosome.Translate_Into_Networks(80*80, [80, 80], 4, score)
        path = "Network/"
        file_list = os.listdir(path)
        network_file = [file for file in file_list if file.endswith(".pt")]
        network_list = SNN.import_network(network_file)
        partial_score_list = SNN.return_score(network_list)
        gene_score_list.append(partial_score_list)
    for j in range(len(gene_score_list)):
        real_score.append(gene_score_list[0][j]+gene_score_list[1][j]+gene_score_list[2][j]+gene_score_list[3][j])
    selected_gene: list = NEAT.calc_and_select_gene(real_score, gene_list)
    gene_num: int = len(gene_list)/2
    for k in range(gene_num):
        cross1 = rd.choice(selected_gene)
        cross2 = rd.choice(selected_gene)
        Agene1,Agene2 = NEAT.Crossover(cross1, cross2)
        gene_list.remove(cross1)
        gene_list.remove(cross2)
        descendants_gene.append(Agene1)
        descendants_gene.append(Agene2)
    Genetic.Write_Gene(descendants_gene)



