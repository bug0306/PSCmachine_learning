from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QLabel, QLineEdit, QPushButton,QMainWindow)
from joblib import load
import pandas as pd

# 加载你的训练好的模型
model = load('TCP_ML\catboost_model.joblib')


class PredictorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("三阳离子钙钛矿带隙预测")
        self.resize(800, 600)
    def initUI(self):
        layout = QVBoxLayout()

        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.input3 = QLineEdit(self)
        self.input4 = QLineEdit(self)
        self.input5 = QLineEdit(self)
        self.predict_btn = QPushButton('预测', self)
        self.result_label = QLabel('结果将显示在这里', self)

        layout.addWidget(QLabel('输入 Cs含量(0-1):'))
        layout.addWidget(self.input1)
        layout.addWidget(QLabel('输入 FA含量(0-1):'))
        layout.addWidget(self.input2)
        layout.addWidget(QLabel('输入 MA含量(0-1):'))
        layout.addWidget(self.input3)
        layout.addWidget(QLabel('输入 I含量(0-3):'))
        layout.addWidget(self.input4)
        layout.addWidget(QLabel('输入 Br含量(0-3):'))
        layout.addWidget(self.input5)
        layout.addWidget(self.predict_btn)
        layout.addWidget(self.result_label)

        self.predict_btn.clicked.connect(self.predict)

        self.setLayout(layout)

    def predict(self):
        try:
            Cs_value = float(self.input1.text())
            FA_value = float(self.input2.text())
            MA_value = float(self.input3.text())
            I_value = float(self.input4.text())
            Br_value = float(self.input5.text())

            if not (0 <= Cs_value <= 1 and 0 <= FA_value <= 1 and 0 <= MA_value <= 1 and 0 <= I_value <= 3 and 0 <= Br_value <= 3):
                self.result_label.setText('超出范围，请重新输入一个在范围内的值')
                return
            elif (Cs_value+FA_value+MA_value) > 1:
                self.result_label.setText('Cs, FA, MA 三者之和不能大于1,请重新输入')
                return
            elif (I_value+Br_value) > 3:
                self.result_label.setText('I, Br 两者之和不能大于3,请重新输入')
                return
            else:
                input_values = pd.DataFrame({
                    'Cs': [Cs_value],
                    'FA': [FA_value],
                    'MA': [MA_value],
                    'I': [I_value],
                    'Br': [Br_value]
                })

            prediction = model.predict(input_values)
            self.result_label.setText(f'预测结果: {prediction[0]:.4f}')
        except Exception as e:
            self.result_label.setText(f'预测过程中出现错误: {str(e)}')
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = PredictorApp()
    ex.show()
    sys.exit(app.exec_())