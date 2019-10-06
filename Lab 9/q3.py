import csv

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
 

prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))


prior = learn_prior("spam-labelled.csv")
print("Prior probability of not spam is {:.5f}.".format(1 - prior))


prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
print(format(prior, ".5f"))