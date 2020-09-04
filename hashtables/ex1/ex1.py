# iterate through the list of weights and add each value to the weight_dict
    # key: weight
    # value: limit - weight
# iterate through our weight_dict and determine if limit - weight
# of current weight exists in our original list of weights
# if it is, then we just need to find the index of both and return

def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {}

    for weight in weights:
        if weight not in weight_dict:
            weight_dict[weight] = limit - weight

    for weight in weight_dict.items():
        print(weight)
        # if we only have two items in our list, reverse the list and grab first index, then grab first index
        if len(weights) == 2:
            result = [len(weights) - 1 - weights[::-1].index(weights[1]), weights.index(weight[1])]
            return result
        if weight[1] in weights:
            return [weights.index(weight[1]), weights.index(weight_dict[weight[1]])]
    # Exit if no index is found
    return None
