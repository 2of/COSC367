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


prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  


prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, False, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true)) 