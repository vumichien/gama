import numpy as np

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import FeatureAgglomeration
from sklearn.preprocessing import MaxAbsScaler, MinMaxScaler, Normalizer, PolynomialFeatures, RobustScaler, \
    StandardScaler, Binarizer
from sklearn.kernel_approximation import Nystroem, RBFSampler
from sklearn.decomposition import PCA, FastICA
from sklearn.feature_selection import SelectFwe, SelectPercentile, f_classif, VarianceThreshold

# This selection of operators and hyperparameters is currently most of what TPOT supports, for comparison.

clf_config = {

    'alpha': [1e-3, 1e-2, 1e-1, 1., 10., 100.],
    'fit_prior': [True, False],
    'min_samples_split': range(2, 21),
    'min_samples_leaf': range(1, 21),

    # Classifiers
    SVC: {
        'C': [2**i for i in range(-5, 6)],
        'kernel': ['rbf', 'poly', 'sigmoid'],
        'degree': range(1, 6),
        'gamma': [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10],
        'coef0': np.arange(-1, 1.01, 0.2),
        'shrinking': [True, False],
        'tol': [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
    },

    GaussianNB: {
    },

    BernoulliNB: {
        'alpha': [],
        'fit_prior': []
    },

    MultinomialNB: {
        'alpha': [],
        'fit_prior': []
    },

    DecisionTreeClassifier: {
        'criterion': ["gini", "entropy"],
        'max_depth': range(1, 11),
        'min_samples_split': [],
        'min_samples_leaf': []
    },

    ExtraTreesClassifier: {
        'n_estimators': [100],
        'criterion': ["gini", "entropy"],
        'max_features': np.arange(0.05, 1.01, 0.05),
        'min_samples_split': [],
        'min_samples_leaf': [],
        'bootstrap': [True, False]
    },

    RandomForestClassifier: {
        'n_estimators': [100],
        'criterion': ["gini", "entropy"],
        'max_features': np.arange(0.05, 1.01, 0.05),
        'min_samples_split': range(2, 21),
        'min_samples_leaf': range(1, 21),
        'bootstrap': [True, False]
    },

    GradientBoostingClassifier: {
        'n_estimators': [100],
        'criterion': ["friedman_mse"],
        'validation_fraction': [0.1],
        'tol': [1e-4],
        'min_weight_fraction_leaf': [0.],
        'min_impurity_decrease': [0.],
        'learning_rate': [1e-3, 1e-2, 1e-1, 0.5, 1.],
        'max_depth': range(1, 11),
        'min_samples_split': range(2, 21),
        'min_samples_leaf': range(1, 21),
        'subsample': np.arange(0.05, 1.01, 0.05),
        'max_features': np.arange(0.05, 1.01, 0.05)
    },

    KNeighborsClassifier: {
        'n_neighbors': range(1, 51),
        'weights': ["uniform", "distance"],
        'p': [1, 2]
    },

    LogisticRegression: {
        'penalty': ['l2'],
        'C': [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1., 5., 10., 15., 20., 25.],
        'dual': [False, True],
        'solver': ['lbfgs']
    },

    Binarizer: {
        'threshold': np.arange(0.0, 1.01, 0.05)
    },

    FastICA: {
        'tol': np.arange(0.0, 1.01, 0.05)
    },

    FeatureAgglomeration: {
        'linkage': ['ward', 'complete', 'average'],
        'affinity': ['euclidean', 'l1', 'l2', 'manhattan', 'cosine', 'precomputed'],
        'param_check': [lambda params: (not params['linkage'] == "ward") or params['affinity'] == "euclidean"]
    },

    MaxAbsScaler: {
    },

    MinMaxScaler: {
    },

    Normalizer: {
        'norm': ['l1', 'l2', 'max']
    },

    Nystroem: {
        'kernel': ['rbf', 'cosine', 'chi2', 'laplacian', 'polynomial', 'poly', 'linear', 'additive_chi2', 'sigmoid'],
        'gamma': np.arange(0.0, 1.01, 0.05),
        'n_components': range(1, 11)
    },

    PCA: {
        'svd_solver': ['randomized'],
        'iterated_power': range(1, 11)
    },

    PolynomialFeatures: {
        'degree': [2],
        'include_bias': [False],
        'interaction_only': [False]
    },

    RBFSampler: {
        'gamma': np.arange(0.0, 1.01, 0.05)
    },

    RobustScaler: {
    },

    StandardScaler: {
    },

    # Selectors
    SelectFwe: {
        'alpha': np.arange(0, 0.05, 0.001),
        'score_func': {
            f_classif: None
        }
    },

    SelectPercentile: {
        'percentile': range(1, 100),
        'score_func': {
            f_classif: None
        }
    },

    VarianceThreshold: {
        'threshold': np.arange(0.05, 1.01, 0.05)
    }
}
