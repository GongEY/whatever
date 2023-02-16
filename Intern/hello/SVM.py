#Linear SVM 모델의 학습과 실행
'''
import numpy as np
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

iris = datasets.load_iris()
X = iris["data"][:, (2,3)]
y = (iris['target'] == 2).astype(np.float64)

svm_clf = Pipeline([
    ("scaler", StandardScaler()),
    ("linear_svc", LinearSVC(C=100, loss='hinge', random_state=42)),
])

svm_clf.fit(X,y)
print(svm_clf.predict([[5.5, 1.7]]))
'''

#Nonlinear SVM 모델 - Polynomial features : 실행 오류

#Nonlinear SVM 모델 - Kernel trick
'''
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=100, noise=0.15, random_state=42)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

poly_kernel_svm_clf = Pipeline([
    ("scaler", StandardScaler()),
    ("svm_clf", SVC(kernel="poly", degree=3, coef0=1, C=5))
])

poly_kernel_svm_clf.fit(X, y)
'''

#Nonlinear SVM 모델 - Gaussain RBF
'''
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=100, noise=0.15, random_state=42)
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

gamma1, gamma2 = 0.1, 5
C1, C2 = 0.001, 1000
hyperparams = (gamma1, C1), (gamma1, C2), (gamma2, C1), (gamma2, C2)

svm_clfs = []
for gamma, C in hyperparams:
    rbf_kernel_svm_clf = Pipeline([
        ("scaler", StandardScaler()),
        ("svm_clf", SVC(kernel="rbf", gamma=gamma, C=C))
    ])
    rbf_kernel_svm_clf.fit(X, y)
    svm_clfs.append(rbf_kernel_svm_clf)
'''

#Nonliear SVM 모델의 학습과 실행 (kernel 함수)
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y !=0, :2]
y = y[y != 0]

n_sample = len(X)

np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(np.float)

X_train = X[:int(.9 * n_sample)]
y_train = y[:int(.9 * n_sample)]
X_test = X[int(.9 * n_sample):]
y_test = y[int(.9 * n_sample):]

for fig_num, kernel in enumerate(('linear', 'rbf', 'poly')):
    clf = svm.SVC(kernel=kernel, gamma=10)
    clf.fit(X_train, y_train)

    plt.figure(fig_num)
    plt.clf()
    plt.scatter(X[:, 0], X[:, 1], c=y, zorder=10, cmap=plt.cm.Paired, edgecolor='k', s=20)
    plt.scatter(X_test[:, 0], X_test[:, 1], s=80, facecolors ='none', zorder=10, edgecolor ='k')

    plt.axis('tight')
    x_min = X[:, 0].min()
    x_max = X[:, 0].max()
    y_min = X[:, 1].min()
    y_max = X[:, 1].max()

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(XX, YY, Z, colors = ['k', 'k', 'k'],
                linestyles=['--','-','--'], levels=[-.5, 0, .5])

    plt.title(kernel)
    plt.show()

'''


#SVM Regression
'''
from sklearn.svm import LinearSVR
import numpy as np

np.random.seed(42)
m = 50
X = 2 * np.random.rand(m, 1)
y = (4 + 3*X + np.random.randn(m, 1)).ravel()

svm_reg1 = LinearSVR(epsilon=1.5, random_state=42)
svm_reg2 = LinearSVR(epsilon=0.5, random_state=42)
svm_reg1.fit(X,y)
svm_reg2.fit(X,y)

from sklearn.svm import SVR

np.random.seed(42)
m = 100
X = 2 * np.random.rand(m,1) - 1
y = (0.2 + 0.1 * X + 0.5*X**2 + np.random.randn(m,1)/10).ravel()

svm_poly_reg1 = SVR(kernel="poly", degree=2, C=100, epsilon=0.1)
svm_poly_reg2 = SVR(kernel="poly", degree=2, C=0.01, epsilon=0.1)
svm_poly_reg1.fit(X,y)
svm_poly_reg2.fit(X,y)
'''

# SVR 예시
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

y[::5] += 3 * (0.5 - np.random.rand(8))

svr_rbf = SVR(kernel='rbf', C=10, gamma=0.1)
svr_lin = SVR(kernel='linear', C=10)
svr_poly = SVR(kernel='poly', C=10, degree=2)
y_rbf = svr_rbf.fit(X,y).predict(X)
y_lin = svr_lin.fit(X,y).predict(X)
y_poly = svr_poly.fit(X,y).predict(X)

lw = 2
plt.scatter(X, y, color = 'darkorange', label = 'data')
plt.plot(X, y_rbf, color = 'navy', lw=lw, label = 'RBF')
plt.plot(X, y_lin, color = 'c', lw=lw, label = 'Linear')
plt.plot(X, y_poly, color = 'cornflowerblue', lw=lw, label ='Poly')
plt.xlabel('data')
plt.ylabel('target')
plt.title('SVR')
plt.legend()
plt.show()