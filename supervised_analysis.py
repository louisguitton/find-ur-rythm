# from sklearn.ensemble import RandomForestClassifier
import sklearn
from sklearn import *
from dataset_generator import *
import spectrum
# import numpy as np
import random
import copy
# import matplotlib.pyplot as plt
# import numpy.fft
# import math
# from scipy import signal

FREQ_RANGES = [[0.5, 4], [4, 8], [8, 12], [11, 15], [15, 30], [30, 45]]
# Delta, Theta, Alpha, Beta, Sigma, Delta

SIGNALS_TO_ANALYZE = ["T8", "C4", "F4", "T7", "C3", "CZ"]


def get_spectral_intensities(data, ranges=FREQ_RANGES):
    intensities = []
    spectral_data = spectrum.pmtm(data, 2.5, show=False)
    l = len(data)
    for [min, max] in ranges:
        intensities.extend(sum(spectral_data[int(min * l / FREQ):int(max * l / FREQ)]) / (max - min))
    return(intensities)


def get_all_spectral_intensities(sample, ranges=FREQ_RANGES, signals=SIGNALS_TO_ANALYZE):
    intensities = []
    for signal in signals:
        intensities.extend(get_spectral_intensities(sample[signal], ranges))
    return(intensities)


def get_dataset_from_enr(enr, playlist, length):
    inputs = []
    outputs = {}
    for feature in playlist:
        outputs[feature] = []
    for i in range(10):
        for sample in cut_sample(enr[i], length):
            inputs.append(get_all_spectral_intensities(sample))
            for feature in playlist:
                outputs[feature].append(playlist[feature][i])
    return({"inputs": inputs, "outputs": outputs})


def shuffle_dataset(dataset):
    length = len(dataset["inputs"])
    shuffled_indices = random.sample(range(length), length)
    tmp = copy.deepcopy(dataset)
    for i in range(length):
        dataset["inputs"][i] = tmp["inputs"][shuffled_indices[i]]
        for feature in dataset["outputs"]:
            dataset["outputs"][feature][i] = tmp["outputs"][feature][shuffled_indices[i]]


def join_datasets(datasets):
    inputs = []
    outputs = {"sung": [], "rythmic": [], "charles likes": [], "louis likes": []}
    for dataset in datasets:
        inputs.extend(dataset["inputs"])
        for feature in outputs:
            outputs[feature].extend(dataset["outputs"][feature])
    return({"inputs": inputs, "outputs": outputs})


def get_accuracy_one_set(classifier, feature, dataset, learning_share):
    c = classifier()
    l = len(dataset["inputs"])
    k = int(l * learning_share)
    c.fit(dataset["inputs"][0:k], dataset["outputs"][feature][0:k])
    return(c.score(dataset["inputs"][k:l], dataset["outputs"][feature][k:l]))


def get_accuracy(classifier, feature, learning_set, test_set):
    c = classifier()
    c.fit(learning_set["inputs"], learning_set["outputs"][feature])
    return(c.score(test_set["inputs"], test_set["outputs"][feature]))


def print_accuracies(feature, classifier, learning_share):
    print("Testing feature: " + feature)
    print("  On same taping ({:.0f}% for learning, {:.0f}% for testing):".format(100 * learning_share, 100 * (1 - learning_share)))
    if feature != "charles likes":
        print("    Louis #1:         {:.0f}%".format(100 * get_accuracy_one_set(classifier, feature, datasetL1, learning_share)))
        print("    Louis #2:         {:.0f}%".format(100 * get_accuracy_one_set(classifier, feature, datasetL2, learning_share)))
    if feature != "louis likes":
        print("    Charles #1:       {:.0f}%".format(100 * get_accuracy_one_set(classifier, feature, datasetC1, learning_share)))
        print("    Charles #2:       {:.0f}%".format(100 * get_accuracy_one_set(classifier, feature, datasetC2, learning_share)))
    print("  From one taping to another")
    if feature != "charles likes":
        print("    Louis #1 to #2:   {:.0f}%".format(100 * get_accuracy(classifier, feature, datasetL1, datasetL2)))
        print("    Louis #2 to #1:   {:.0f}%".format(100 * get_accuracy(classifier, feature, datasetL2, datasetL1)))
    if feature != "louis likes":
        print("    Charles #1 to #2: {:.0f}%".format(100 * get_accuracy(classifier, feature, datasetC1, datasetC2)))
        print("    Charles #2 to #1: {:.0f}%".format(100 * get_accuracy(classifier, feature, datasetC2, datasetC1)))
    if feature in ["sung", "rythmic"]:
        print("  From one guinea pig to another:")
        print("    Louis to Charles: {:.0f}%".format(100 * get_accuracy(classifier, feature, datasetL, datasetC)))
        print("    Charles to Louis: {:.0f}%".format(100 * get_accuracy(classifier, feature, datasetC, datasetL)))


print("Generating dataset from taping Louis #1...")
datasetL1 = get_dataset_from_enr(enrL1, playlist1, 5)
print("Done. Size of the set: {:d}".format(len(datasetL1["inputs"])))
print("Generating dataset from taping Louis #2...")
datasetL2 = get_dataset_from_enr(enrL2, playlist2, 5)
print("Done. Size of the set: {:d}".format(len(datasetL2["inputs"])))
print("Generating dataset from taping Charles #1...")
datasetC1 = get_dataset_from_enr(enrC1, playlist1, 5)
print("Done. Size of the set: {:d}".format(len(datasetC1["inputs"])))
print("Generating dataset from taping Charles #2...")
datasetC2 = get_dataset_from_enr(enrC2, playlist2, 5)
print("Done. Size of the set: {:d}".format(len(datasetC2["inputs"])))

datasetL = join_datasets([datasetL1, datasetL2])
datasetC = join_datasets([datasetC1, datasetC2])


while True:
    feature = ""
    while feature not in ["sung", "rythmic", "louis likes", "charles likes"]:
        feature = input("Feature: ")
    classifier_index = -1
    while (classifier_index < 1) | (classifier_index > 2):
        classifier_index = int(input("Classifier:\n  1: logistic regression\n  2: random forest\n> "))
    classifier = [sklearn.linear_model.LogisticRegression, sklearn.ensemble.RandomForestClassifier][classifier_index - 1]
    learning_share = 0
    while (learning_share <= 0) | (learning_share >= 1):
        learning_share = float(input("Learning share: "))
    shuffle_dataset(datasetL1)
    shuffle_dataset(datasetL2)
    shuffle_dataset(datasetC1)
    shuffle_dataset(datasetC2)
    shuffle_dataset(datasetL)
    shuffle_dataset(datasetC)
    print_accuracies(feature, classifier, learning_share)
