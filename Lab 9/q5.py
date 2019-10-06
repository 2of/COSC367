import csv
def learn_likelihood(file_name, pseudo_count=0):
    prior = 0
    skip_ahead  = 1
    row_num = 0
    likelihoods = [[pseudo_count,pseudo_count] for i in range(12)]
    with open(file_name, 'r', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if skip_ahead:
                skip_ahead = 0
                continue
            row_num += 1
            spam = int(row[-1])
            for i in range(12):
                likelihoods[i][spam] += int(row[i])
            prior += spam
    for each in likelihoods:
        each[1] /= (prior + 2 * pseudo_count)
        each[0] /= (row_num - prior + 2 * pseudo_count)
    return likelihoods

def learn_prior(file_name, pseudo_count=0):
    ''' Just tally up the probability i guess'''
    count_spam = 0
    row_count = 0
    skip_head = 1
    with open(file_name, 'r', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if skip_head:
                skip_head = 0
                continue
           
            row_count += 1
            if row[-1] == '1':
                count_spam += 1
    return (count_spam + pseudo_count)/(row_count + 2 * pseudo_count)

def posterior(prior, likelihood, observation):
    true = prior
    false = 1 - true
    for i in range(len(observation)):
        if observation[i]:
            true *= likelihood[i][1]
            false *= likelihood[i][0]
        else:
            true *= (1 - likelihood[i][1])
            false *= (1 - likelihood[i][0])
    return true / (true + false)



def nb_classify(prior,likelihood,input_vector):
    result = posterior(prior,likelihood,input_vector) 
    if (result > 0.5):
        return ("Spam",result)
    return ("Not Spam",1-result)


prior = learn_prior("spam-labelled.csv")
likelihood = learn_likelihood("spam-labelled.csv")



prior = learn_prior("spam-labelled.csv")
likelihood = learn_likelihood("spam-labelled.csv")

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))




prior = learn_prior("spam-labelled.csv", pseudo_count=1)
likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))