import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class GDRegressor:
    def __init__(self, alpha=0.0001, max_iter=2000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta_history = [0] * self.max_iter  # переменная для сохранения теты
        self.cost_history = [0] * self.max_iter  # переменная для сохранения значений целевой функции

    def fit(self, X_train, y_train): # добавить столбец из единичек в нулевую матрицу х
        """
        Обучаем модель на данных
        :param X_train: матрица признаков
        :param y_train: матрица ответов
        :return: coef_ - вектор оценок для theta_i (i - значение от 1 до p, p - количество признаков),
        intercept_ - оценённое значение для theta_0
        """
        X = X_train.copy()
        X.insert(0, "Ones", np.ones(len(X)))
        t = X.T
        self.theta = np.zeros(X.shape[1])
        m = y_train.size
        for i in range(1, self.max_iter):
            """
            цикл, внутри которого будем высчитывать значения теты, сохранять значения целевой функции
            """
            # формула градиентного спуска, для подсчёта значений теты
            self.theta -= self.alpha * (1 / m) * (np.dot(t, (np.dot(X, self.theta) - y_train)))
            # записываем старые значения теты
            self.theta_history[i] = self.theta
            # записываем старые значения целевой функции
            self.cost_history[i] = np.sum((self.theta * X.as_matrix() - y_train.reshape((m, 1))) ** 2) / (2 * m)

        self.coef_ = self.theta[1]
        self.intercept_ = self.theta[0]

        return self.coef_, self.intercept_

    def predict(self, X_test):
        """
        :param X_test: тестовая выборка
        :return: вектор прогнозов для новых данных (произведение тестовой выборки на вектор весов)
        """
        self.pred = self.intercept_ + self.coef_ * X_test

        return self.pred


def rmse(y_hat, y):
    """
    Считаем среднеквадратичную ошибку
    :param y_hat:
    :param y: вектор прогнозов, сформированный в predict
    :return: среднеквадратичная ошибка
    """
    m = y.size  # считаем размер выборки
    RMSE = 0  # будущая среднеквадратичная ошибка
    for i in range(m):
        """
        Считаем среднеквадратичную ошибку
        """
        RMSE = ((sum(y_hat.iloc[i] - y.iloc[i]) ** 2) / m) ** 0.5
    return RMSE


def r_squared(y_hat, y):
    """
    Считаем коэффициент детерминации
    :param y_hat: изначальный вектор
    :param y: вектор прогнозов, сформированный в predict
    :return: коэффициент детерминации
    """
    m = y.size  # считаем размкр выборки
    DETERMINATION_COEF = 0  # будущий коэффициент детерминации
    for i in range(m):
        """
        Считаем коэффициент детерминцаии
        """
        DETERMINATION_COEF = 1 - (np.sum((y.iloc[i] - y_hat.iloc[i]) ** 2) / (np.sum((y.iloc[i] - y.mean()) ** 2)))
    return DETERMINATION_COEF


if __name__ == '__main__':
    df = pd.read_csv('brain_size.csv')
    X = df.iloc[:, 1:2]
    Y = df['VIQ']
    model = GDRegressor()
    print(model.fit(X, Y))
    y_pred = model.predict(X)
    rmse(y_pred, Y)
    r_squared(y_pred, Y)
    df.plot(kind='scatter', x="FSIQ", y="VIQ")
    plt.plot(X, model.coef_ * X + model.intercept_, 'r')
    plt.show()
