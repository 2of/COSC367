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




print(len(likelihood))
print([len(item) for item in likelihood])



likelihood = learn_likelihood("spam-labelled.csv")

print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))


likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

print("With Laplacian smoothing:")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))