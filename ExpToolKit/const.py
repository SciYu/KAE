class DATASET_CONST:
    DATASET_DIR = "~/Datasets"

    DATASET_MNIST = "MNIST"
    DATASET_FASHION_MNIST = "FashionMNIST"
    DATASET_CIFAR10 = "CIFAR10"
    DATASET_CIFAR100 = "CIFAR100"

    DATASET_RGB_TYPES = [
        DATASET_CIFAR10,
        DATASET_CIFAR100,
    ]
    DATASET_TYPES = [
        DATASET_MNIST,
        DATASET_FASHION_MNIST,
        DATASET_CIFAR10,
        DATASET_CIFAR100,
    ]

    MNIST_INPUT_DIM = 28 * 28
    FASHION_MNIST_INPUT_DIM = 28 * 28
    CIFAR10_INPUT_DIM = 32 * 32
    CIFAR100_INPUT_DIM = 32 * 32

    PREPROCESSING_ORIGINAL = "ORIGINAL"
    PREPROCESSING_INVERSE = "INVERSE"
    PREPROCESSING_NORMALIZE = "NORMALIZE"
    PREPROCESSING_STANDARDIZE = "STANDARDIZE"
    PREPROCESSING_METRIC = [
        PREPROCESSING_ORIGINAL,
        PREPROCESSING_NORMALIZE,
        PREPROCESSING_INVERSE,
        PREPROCESSING_STANDARDIZE,
    ]


class MODEL_CONST:
    MODEL_AE = "AE"


class TRAIN_CONST:
    SGD_OPTIM = "SGD"
    ADAM_OPTIM = "ADAM"
    ADAMW_OPTIM = "ADAMW"
