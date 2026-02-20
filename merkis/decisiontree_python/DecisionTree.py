from collections import Counter
import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def _is_leaf_node(self):
        return self.value is not None


class DecisionTree:
    def __init__(self,min_num_splits = 2, max_depth=2, n_features=None):  
        self.min_num_splits = min_num_splits
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):
        self.n_features = X.shape[1] if not self.n_features else min(X.shape[1], self.n_features)
        self.root = self._grow_tree(X, y)
    
    def _grow_tree(self, X, y, depth = 0):
        num_splits, n_feats = X.shape
        labels = len(np.unique(y))


        if (labels == 1 or num_splits <= self.min_num_splits or self.max_depth <= depth):
            leaf_node_value = self._choices(y)
            return Node(value=leaf_node_value)

        features = np.random.choice(n_feats, self.n_features, replace=False)
    
        best_feature, best_threshold = self._best_split(X, y, features)

        left_idx, right_idx = self._split(X.iloc[: , best_feature], best_threshold)

        left = self._grow_tree(X.iloc[left_idx , :], y[left_idx], depth+1)
        right = self._grow_tree(X.iloc[right_idx, :], y[right_idx],depth+1)
        return Node(best_feature, best_threshold, left, right)




    
    def _choices(self, y):
        counter = Counter(y)
        value = counter.most_common(1)[0][0]
        print(value)
        return value



    def _best_split(self, X, y, features):
        best_gain = -1
        best_feature, best_threshold = None, None

        for feat in features:
            X_column = X.iloc[: , feat]
            thresholds = np.unique(X_column)

            for thr in thresholds:
                gain = self._information_gain(X_column,y, thr)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feat
                    best_threshold = thr
        
        return best_feature, best_threshold
    

    def _information_gain(self, X_column, y, thr):
        parent_entropy = self._entropy(y)

        left_indices, right_indices = self._split(X_column, thr)

        if len(left_indices) == 0 or len(right_indices) == 0:
            return 0

        n = len(y)
        l_n , r_n = len(left_indices) , len(right_indices)
        e_l , e_r = self._entropy(y[left_indices]), self._entropy(y[right_indices])
        children_entropy_weighted = e_l*(l_n/n) + e_r*(r_n/n)
        return parent_entropy - children_entropy_weighted

    
    def _split(self, X_column, thr):
        if thr == 0:
            print(thr)
        left_indices = np.argwhere(X_column <= thr).flatten()
        right_indices = np.argwhere(X_column > thr).flatten()
        return left_indices, right_indices

    
    def _entropy(self, y):
        bins = np.bincount(y)
        ps = bins/len(y)
        return -np.sum([p * np.log(p) for p in ps if p > 0])
    
    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for _, x in X.iterrows()])
    
    def _traverse_tree(self, x, node):
        if node._is_leaf_node():
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

