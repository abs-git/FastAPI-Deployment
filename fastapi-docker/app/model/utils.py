## data handler
import numpy as np
import matplotlib.pyplot as plt

def get_eval_batch(data:dict, ref_dict, ref_key='all'):
    '''
    data : {'class' : [...]}
    ref_dict : {'all': {'0' : [...], '1' : [...], ... , '21' : [...]}}
    '''
    n_class = len(ref_dict[ref_key])

    test_batch = []
    test_targets = []

    anchors = np.array([data]*n_class)
    comparison = np.array(list(ref_dict[ref_key].values())).squeeze(axis=1)
    
    pairs = list(np.array([anchors, comparison]))
    targets = np.zeros((n_class,1))
    targets[int(data.keys)] = 1

    test_batch.append(pairs)
    test_targets.append(targets)

    return test_batch, test_targets


def plot_images(input_list):
    x, y = zip(*input_list)

    plt.xlim([-0.2, 1.2])
    plt.ylim([-0.2, 1.2])
    plt.plot(x,y)
    plt.scatter(x,y)

    return 