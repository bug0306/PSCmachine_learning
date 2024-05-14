import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QLabel,QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import pandas as pd
import joblib

font = QFont()
font.setPointSize(18)
font1 = QFont()
font1.setPointSize(28)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 创建顶部布局
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.move(0,self.y())
        # 创建主布局
        main_layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()

        # 创建图片标签并添加到顶部布局
        image_label = QLabel()
        pixmap = QPixmap('triplePCE\perovskiite.jpg') 
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(image_label)

        text_label = QLabel('三阳离子钙钛矿组分以及制备条件预测光电转换效率')
        text_label.setFont(font1)
        text_label.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(text_label)

        main_layout.addLayout(top_layout)

        # 创建顶层布局
        second_layout = QVBoxLayout()

        row1_layout = QHBoxLayout()
        self.cs_input = QLineEdit()
        self.fa_input = QLineEdit()
        self.i_input = QLineEdit()

        label1 = QLabel("组分条件")
        label1.setFont(font)
        label1.setAlignment(Qt.AlignCenter)
        row1_layout.addWidget(label1)

        cs_layout = QVBoxLayout()
        cs_layout.addWidget(QLabel('Cs含量(0-1)'))
        cs_layout.addWidget(self.cs_input)
        row1_layout.addLayout(cs_layout)

        fa_layout = QVBoxLayout()
        fa_layout.addWidget(QLabel('FA含量(0-1)'))
        fa_layout.addWidget(self.fa_input)
        row1_layout.addLayout(fa_layout)

        i_layout = QVBoxLayout()
        i_layout.addWidget(QLabel('I含量(0-3)'))
        i_layout.addWidget(self.i_input)
        row1_layout.addLayout(i_layout)

        row2_layout = QHBoxLayout()
        label1 = QLabel("制备条件")
        label1.setFont(font)
        label1.setAlignment(Qt.AlignCenter)
        row2_layout.addWidget(label1)

        self.Device_structure_input = QLineEdit()
        Device_structure_layout = QVBoxLayout()
        Device_structure_layout.addWidget(QLabel('器件结构(正置:1,倒置:0)'))
        Device_structure_layout.addWidget(self.Device_structure_input)
        row2_layout.addLayout(Device_structure_layout)

        self.BG_input = QLineEdit()
        BG_layout = QVBoxLayout()
        BG_layout.addWidget(QLabel('带隙值'))
        BG_layout.addWidget(self.BG_input)
        row2_layout.addLayout(BG_layout)

        substrate_layout = QVBoxLayout()
        substrate_layout.addWidget(QLabel("衬底"))
        self.input_field1 = QComboBox()
        self.input_field1.addItem("ITO")
        self.input_field1.addItem("FTO")
        substrate_layout.addWidget(self.input_field1)
        row2_layout.addLayout(substrate_layout)

        options = ['BCP/C60', 'C60', 'CMC/BCP', 'c-TiO2', 'c-TiO2/mp-TiO2',
                'c-TiO2/mp-TiO2/SnO2', 'c-TiO2/SnO2', 'Li-TiO2', 'mpTiO2', 'PCBM',
                'PCBM/BCP', 'PCBM/C60', 'PCBM/C60/BCP', 'PCBM/ZnO', 'PlanarTiO2',
                'SnO2', 'SnO2/C60', 'TiO2', 'TiO2/Al2O3', 'ZnO', 'ZnO2']
        ETL_layout = QVBoxLayout()
        ETL_layout.addWidget(QLabel("电子传输层"))
        self.input_field2 = QComboBox()
        for option in options:
            self.input_field2.addItem(option)
        ETL_layout.addWidget(self.input_field2)
        row2_layout.addLayout(ETL_layout)

        options = ['NiOx', '2PACz', 'NiOx/PTAA', 'PTAA', 'SAMs', 'SAMs/NiOx', 'TaTm',
       'spiro', 'P3HT', 'RCP–BTT', 'spiro/Gual', 'TBTA[6]H/TBPHTFSI',
       'unused', 'PEDOT:PSS', 'ployTPD:F4-TCNQ', 'SAMs/Al2O3',
       'D4TBP/spiro', 'PeRyLene/P3HT/MoO3', 'TPFPB/spiro', 'CuSCN', 'ClS']
        HTL_layout = QVBoxLayout()
        HTL_layout.addWidget(QLabel("空穴传输层"))
        self.input_field3 = QComboBox()
        for option in options:
            self.input_field3.addItem(option)
        HTL_layout.addWidget(self.input_field3)
        row2_layout.addLayout(HTL_layout)

        options = ['Ag', 'Au', 'Cu', 'PEIE/Ag', 'Al', 'C']
        electrode_layout = QVBoxLayout()
        electrode_layout.addWidget(QLabel("电极"))
        self.input_field4 = QComboBox()
        for option in options:
            self.input_field4.addItem(option)
        electrode_layout.addWidget(self.input_field4)
        row2_layout.addLayout(electrode_layout)

        options = ['two-step', 'one-step']
        depositionProcedure_layout = QVBoxLayout()
        depositionProcedure_layout.addWidget(QLabel("沉积程序"))
        self.input_field5 = QComboBox()
        for option in options:
            self.input_field5.addItem(option)
        depositionProcedure_layout.addWidget(self.input_field5)
        row2_layout.addLayout(depositionProcedure_layout)

        options = ['spin', 'Inkjet-Printed', 'Vacuum Deposited', 'R2R',
       'slot-die-coating', 'CAGQ']
        depositionMethod_layout = QVBoxLayout()
        depositionMethod_layout.addWidget(QLabel("沉积方法"))
        self.input_field6 = QComboBox()
        for option in options:
            self.input_field6.addItem(option)
        depositionMethod_layout.addWidget(self.input_field6)
        row2_layout.addLayout(depositionMethod_layout)

        options = ['CB', 'unused', 'ANI', 'anisole', 'EA', 'toluene', 'diethyl ether',
       'chloroform ', 'tBuOH/EA', 'EA/HEX', 'EA/Hex']
        Anti_solvent_layout = QVBoxLayout()
        Anti_solvent_layout.addWidget(QLabel("反溶剂"))
        self.input_field7 = QComboBox()
        for option in options:
            self.input_field7.addItem(option)
        Anti_solvent_layout.addWidget(self.input_field7)
        row2_layout.addLayout(Anti_solvent_layout)

        options = ['DMF/DMSO/GBL', 'DMF/DMSO', 'DMF/DMSO/4F-PEAI/Pb(SCN)2',
       'DMF/DMSO/BMIM:BF4', 'DMF/DMSO/BMIM:BF4/4F-PEAI/Pb(SCN)2',
       'DMF:DMSO:NMP', 'DMF', 'DMF/NMP', 'unused', 'DMSO',
       'DMF/DMSO/DmmimCl', 'GBL/DMF', 'DMF/DMSO/APL']
        PrecursorSolvent_layout = QVBoxLayout()
        PrecursorSolvent_layout.addWidget(QLabel("钙钛矿前驱体溶剂"))
        self.input_field8 = QComboBox()
        for option in options:
            self.input_field8.addItem(option)
        PrecursorSolvent_layout.addWidget(self.input_field8)
        row2_layout.addLayout(PrecursorSolvent_layout)

        self.AnnealingTem_input = QLineEdit()
        AnnealingTem_layout = QVBoxLayout()
        AnnealingTem_layout.addWidget(QLabel('退火温度'))
        AnnealingTem_layout.addWidget(self.AnnealingTem_input)
        row2_layout.addLayout(AnnealingTem_layout)        

        self.AnnealingTime_input = QLineEdit()
        AnnealingTime_layout = QVBoxLayout()
        AnnealingTime_layout.addWidget(QLabel('退火时间'))
        AnnealingTime_layout.addWidget(self.AnnealingTime_input)
        row2_layout.addLayout(AnnealingTime_layout)      

        second_layout.addLayout(row1_layout)
        second_layout.addSpacing(30)
        second_layout.addLayout(row2_layout)

        second_layout.addSpacing(30)

        predict_button = QPushButton('预测')
        second_layout.addWidget(predict_button)
        predict_button.clicked.connect(self.predict)
        self.predict_output = QLineEdit()
        second_layout.addWidget(self.predict_output)

        second_layout.addSpacing(30)
        feedback_input_layout = QHBoxLayout()
        feedback_input_layout.addWidget(QLabel('反馈:'))

        self.feedback_input = QLineEdit()
        feedback_input_layout.addWidget(self.feedback_input)

        feedback_input_layout.addLayout(feedback_input_layout)

        feedback_button = QPushButton('发送反馈')
        feedback_input_layout.addWidget(feedback_button)

        second_layout.addLayout(feedback_input_layout)

        feedback_button.clicked.connect(self.send_feedback)
        main_layout.addLayout(second_layout)
    def send_feedback(self):
        feedback = self.feedback_input.text()
        print(f"发送反馈: {feedback}")
    
    def predict(self):
        try:
            cs_value = self.cs_input.text()
            fa_value = self.fa_input.text()
            i_value = self.i_input.text()
            Device_structure_value = self.Device_structure_input.text()
            BG_value = self.BG_input.text()
            substrate_value = self.input_field1.currentText()
            ETL_value = self.input_field2.currentText()
            HTL_value = self.input_field3.currentText()
            electrode_value = self.input_field4.currentText()
            depositionProcedure_value = self.input_field5.currentText()
            depositionMethod_value = self.input_field6.currentText()
            Anti_solvent_value = self.input_field7.currentText()
            PrecursorSolvent_value = self.input_field8.currentText()
            AnnealingTem_value = self.AnnealingTem_input.text()
            AnnealingTime_value = self.AnnealingTime_input.text()
            data = {'Cs': [cs_value], 'FA': [fa_value], 'I': [i_value],'structure':[Device_structure_value],
                    'bandgap':[BG_value],'substrate':[substrate_value],'ETL':[ETL_value],'HTL':[HTL_value],
                    'electrode':[electrode_value],'depositionProcedure':[depositionProcedure_value],
                    'depositionMethod':[depositionMethod_value],'Anti-solvent':[Anti_solvent_value],
                    'PrecursorSolvent':[PrecursorSolvent_value],'AnnealingTemperature':[AnnealingTem_value],
                    'AnnealingTime':[AnnealingTime_value]}

            df = pd.DataFrame(data)
            print(df)
            df.iloc[:, [0, 1,2, 4]] = df.iloc[:, [0, 1,2, 4]].astype('float64')
            df.iloc[:, [3, 13, 14]] = df.iloc[:, [3, 13, 14]].astype('int64')
            df.iloc[:, [5,6,7,8,9,10,11,12]] = df.iloc[:, [5,6,7,8,9,10,11,12]].astype('object')

            encoder = joblib.load('encoder_fold_5.joblib')
            encoded_columns = encoder.transform(df.iloc[:, [5,6,7,8,9,10,11,12]])

            encoded_df = pd.DataFrame(encoded_columns, columns=encoder.get_feature_names_out(df.columns[5:13]))

            df = pd.concat([df.iloc[:, :5], df.iloc[:, 13:],encoded_df], axis=1)
            model = joblib.load('model_fold_5.joblib')

            prediction = model.predict(df)

            self.predict_output.setText(str(prediction))
        except Exception as e:
            print(f"预测过程中出现错误: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())