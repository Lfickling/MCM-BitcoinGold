import numpy as np


def scratch_main(): 
    weights = np.random.dirichlet(np.ones(3), size =1)[0].tolist()
    #weights1 = weights[0].tolist()
    print(weights)

    print(sum(weights))


if __name__ == '__main__':
    scratch_main()

