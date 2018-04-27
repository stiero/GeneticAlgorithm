#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:44:48 2018

@author: tauro
"""

def fitness(password, test_word):
    
    if len(test_word) != len(password):
        print("Confucius say: This password no good")
        return
    
    else:
        score = 0
        
        for i in range(len(password)):
            if password[i] == test_word[i]:
                score += 1
        
        return (score * 100) / len(password)
    
    

import random

def generateWord(length):
    i = 0
    result = ""
    while i < length:
        letter = chr(97 + int(26 * random.random()))
        result += letter
        i += 1
    return result


def generateFirstPopulation(sizePopulation, password):
    population = []
    i = 0
    while i < sizePopulation:
        population.append(generateWord(len(password)))
        i += 1
    return population


import operator

def computePerfPopulation(population, password):
    populationPerf = {}
    for individual in population:
        populationPerf[individual] = fitness(password, individual)
    #return populationPerf
    return sorted(populationPerf.items(), key=operator.itemgetter(1), reverse=True)
    

def selectFromPopulation(populationSorted, best_sample, lucky_ones):
    next_generation=[]
    for i in range(best_sample):
        next_generation.append(populationSorted[i][0])
    for i in range(lucky_ones):
        next_generation.append(random.choice(populationSorted)[0])
    random.shuffle(next_generation)
    
    return next_generation

def mutateWord(word):
    word = list(word)
    index_modification = int(random.random() * len(word))
    word[index_modification] = chr(97 + int(26 * random.random()))
    word = str(''.join(word))
    return word

def mutatePop(new_generation):
    mutated_words = []
    for word in new_generation:
        word = mutateWord(word)
        mutated_words.append(word)
    return mutated_words



def run_for_generations(password, sizePopulation, best_sample, lucky_ones,
                        num_generations):
    
    first_gen = generateFirstPopulation(sizePopulation, password)
    current_gen = first_gen
    
    for gen in range(num_generations):
        pop_score = computePerfPopulation(current_gen, password)
        best_pop = selectFromPopulation(pop_score, best_sample, lucky_ones)
        mutated_pop = mutatePop(best_pop)
        current_gen = mutated_pop
    
    return current_gen


#####
    
password = "banana"
sizePopulation = 100
best_sample = 20
lucky_ones = 20
num_generations = 100000

#first_pop = generateFirstPopulation(sizePopulation, password)

#pop_score = computePerfPopulation(first_pop, password)

#best_pop = selectFromPopulation(pop_score, best_sample, lucky_ones)

#mutated_pop = mutatePop(best_pop)

final_pop = run_for_generations(password, sizePopulation, best_sample, lucky_ones,
                                num_generations)

