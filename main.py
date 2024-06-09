from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QLineEdit,QFrame,QLabel,QSplashScreen,QProgressBar,QDialog,QVBoxLayout
import sys,time
from PyQt5 import uic
from PyQt5.QtGui import QIcon,QPixmap
import joblib
from PyQt5.QtCore import QFile
from PyQt5.QtCore import Qt
from sklearn import preprocessing
import numpy as np
import os
basedir = os.path.dirname(__file__)
class GraphDialog(QDialog):
    def __init__(self,filepath):
        super(QDialog, self).__init__()
        # Set window title
        self.setWindowTitle("Accuracy Metrics")
        self.setWindowIcon(QIcon("./concrete256x256.png"))
        layout = QVBoxLayout()
        self.image_label = QLabel()
        layout.addWidget(self.image_label)
        self.setLayout(layout)
        pixmap = QPixmap(filepath)
        # Set the image to the QLabel widget
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        #Load UI File
        uic.loadUi("design.ui")
        self.show()
        #Styling elements
        self.apply_stylesheet("MaterialDark.qss")
         #Model Imports
        self.rac_model =joblib.load("./RAC Strength Prediction.pkl")
        self.cs_model =joblib.load("./NAC Strength Prediction.pkl")
        self.c_model = joblib.load("./RAC Carbonization Prediction.pkl")
        self.cl_model =joblib.load("./RAC Chloride Ion Prediction.pkl")
        self.sf_model = joblib.load("./RAC Sulfate Corrosion Prediction.pkl")
        #Transform Imports
        self.transform_sf = joblib.load('./transform_X_sulfate.pkl')
        self.transform_cl = joblib.load('./transform_X_chloride.pkl')  
        self.transform_c = joblib.load('./transform_X_carbonization.pkl')  
        self.transform_cs = joblib.load('./transform_X_cs.pkl') 
        self.transform_det = joblib.load('./transform_X_detailed.pkl') 
    def apply_stylesheet(self, path):
        style_file = QFile(path)
        style_file.open(QFile.ReadOnly | QFile.Text)
        stream = style_file.readAll()
        self.setStyleSheet(str(stream, encoding='utf-8'))
        #Add Main Window Icon
        self.setWindowIcon(QIcon("./concrete256x256.png"))
        self.setFixedWidth(731)
        self.setFixedHeight(860)
        #Referencing to the GUI File Widgets
        self.button_rac = self.findChild(QPushButton,"rac_button")
        self.button_rac.setIcon(QIcon("./data_model.png"))
        self.button_cs = self.findChild(QPushButton,"./cs_button")
        self.button_cs.setIcon(QIcon("./data_model.png"))
        self.button_c = self.findChild(QPushButton,"./c_button")
        self.button_c.setIcon(QIcon("./data_model.png"))
        self.button_cl = self.findChild(QPushButton,"./cl_button")
        self.button_cl.setIcon(QIcon("./data_model.png"))
        self.button_sf = self.findChild(QPushButton,"./sf_button")
        self.button_sf.setIcon(QIcon("./data_model.png"))
        self.rac_fitness_xgb = self.findChild(QPushButton,"./rac_fitness_xgb")
        self.rac_acc_xgb = self.findChild(QPushButton,"./rac_acc_xgb")
        self.rac_residual_xgb = self.findChild(QPushButton,"./rac_residual_xgb")
        self.rac_corr_matrix = self.findChild(QPushButton,"./rac_corr_matrix")
        self.cs_fitness_xgb = self.findChild(QPushButton,"./cs_fitness_xgb")
        self.cs_residual_xgb = self.findChild(QPushButton,"./cs_residual_xgb")
        self.cs_acc_xgb = self.findChild(QPushButton,"./cs_acc_xgb")
        self.cs_corr_matrix = self.findChild(QPushButton,".//cs_corr_matrix")
        self.c_fitness_xgb = self.findChild(QPushButton,"./c_fitness_xgb")
        self.c_residual_xgb = self.findChild(QPushButton,"./c_residual_xgb")
        self.c_acc_xgb = self.findChild(QPushButton,"./c_acc_xgb")
        self.c_corr_matrix = self.findChild(QPushButton,"./c_corr_matrix")
        self.cl_fitness_xgb = self.findChild(QPushButton,"./cl_fitness_xgb")
        self.cl_residual_xgb = self.findChild(QPushButton,"./cl_residual_xgb")
        self.cl_acc_xgb = self.findChild(QPushButton,"./cl_acc_xgb")
        self.cl_corr_matrix = self.findChild(QPushButton,"./cl_corr_matrix")
        self.sf_fitness_xgb = self.findChild(QPushButton,"./sf_fitness_xgb")
        self.sf_residual_xgb = self.findChild(QPushButton,"./sf_residual_xgb")
        self.sf_acc_xgb = self.findChild(QPushButton,"./sf_acc_xgb")
        self.sf_corr_matrix = self.findChild(QPushButton,"./sf_corr_matrix")
        #RAC Data Imports
        ##RAC Strength Prediction Imports
        self.rac_water = self.findChild(QLineEdit,"./rac_water")
        self.rac_cement = self.findChild(QLineEdit,"./rac_cement")
        self.rac_sand = self.findChild(QLineEdit,"./rac_sand")
        self.rac_nca = self.findChild(QLineEdit,"./rac_nca")
        self.rac_rca = self.findChild(QLineEdit,"./rac_rca")
        self.rac_sp = self.findChild(QLineEdit,"./rac_sp")
        self.rac_dia_max = self.findChild(QLineEdit,"./rac_dia_max")
        self.rac_density = self.findChild(QLineEdit,"./rac_density")
        self.rac_water_absorption = self.findChild(QLineEdit,"./rac_water_absorption")
        self.rac_prediction =self.findChild(QLineEdit,"./rac_str_prediction_xgb")
        ##NAC Strength Prediction Imports
        self.cs_cement = self.findChild(QLineEdit,"./cs_cement")
        self.cs_slag = self.findChild(QLineEdit,"./cs_slag")
        self.cs_fly_ash = self.findChild(QLineEdit,"./cs_fly_ash")
        self.cs_water = self.findChild(QLineEdit,"./cs_water")
        self.cs_SP = self.findChild(QLineEdit,"./cs_SP")
        self.cs_cAgg = self.findChild(QLineEdit,"./cs_cAgg")
        self.cs_fAgg = self.findChild(QLineEdit,"./cs_fAgg")
        self.cs_age = self.findChild(QLineEdit,"./cs_age")
        self.cs_prediction = self.findChild(QLineEdit,"./cs_str_prediction_xgb")
        ##Carbonization Prediction Imports
        self.c_water_content = self.findChild(QLineEdit,"./c_water_content")
        self.c_cement = self.findChild(QLineEdit,"./c_cement")
        self.c_CO2 = self.findChild(QLineEdit,"./c_CO2")
        self.c_temperature = self.findChild(QLineEdit,"./c_temperature")
        self.c_relative_humidity = self.findChild(QLineEdit,"./c_relative_humidity")
        self.c_exposure = self.findChild(QLineEdit,"./c_exposure")
        self.c_RCA = self.findChild(QLineEdit,"./c_RCA")
        self.c_fAgg_size = self.findChild(QLineEdit,"./c_fAgg_size")
        self.c_cAgg_size = self.findChild(QLineEdit,"./c_cAgg_size")
        self.c_SP = self.findChild(QLineEdit,"./c_SP")
        self.c_Cstr = self.findChild(QLineEdit,"./c_Cstr")
        self.c_wat_absorption = self.findChild(QLineEdit,"./c_wat_absorption")
        self.c_curing_age = self.findChild(QLineEdit,"./c_curing_age")
        self.c_depth_prediction = self.findChild(QLineEdit,"./c_depth_prediction_xgb")
        ##Chloride Ion Erosion Prediction Imports
        self.cl_curing_age = self.findChild(QLineEdit,"./cl_curing_age")
        self.cl_water_content = self.findChild(QLineEdit,"./cl_water_content")
        self.cl_sand_content = self.findChild(QLineEdit,"./cl_sand_content")
        self.cl_cement_content = self.findChild(QLineEdit,"./cl_cement_content")
        self.cl_NCA = self.findChild(QLineEdit,"./cl_NCA")
        self.cl_RCA = self.findChild(QLineEdit,"./cl_RCA")
        self.cl_water_absorb = self.findChild(QLineEdit,"./cl_water_absorb")
        self.cl_density = self.findChild(QLineEdit,"./cl_density")
        self.cl_fly_ash = self.findChild(QLineEdit,"./cl_fly_ash")
        self.cl_slag = self.findChild(QLineEdit,"./cl_slag")
        self.cl_silica_fume = self.findChild(QLineEdit,"./cl_silica_fume")
        self.cl_fAgg_size = self.findChild(QLineEdit,"./cl_fAgg_size")
        self.cl_cAgg_size = self.findChild(QLineEdit,"./cl_cAgg_size")
        self.cl_SP = self.findChild(QLineEdit,"./cl_SP")
        self.cl_Cstr = self.findChild(QLineEdit,"./cl_Cstr")
        self.cl_charge_prediction = self.findChild(QLineEdit,"./cl_charge_prediction_xgb")
        ## Sulfate Corrosion Prediction Imports
        self.sf_cement = self.findChild(QLineEdit,"./sf_cement")
        self.sf_water = self.findChild(QLineEdit,"./sf_water")
        self.sf_NCA = self.findChild(QLineEdit,"./sf_NCA")
        self.sf_RCA = self.findChild(QLineEdit,"./sf_RCA")
        self.sf_SP = self.findChild(QLineEdit,"./sf_SP")
        self.sf_silica_fume = self.findChild(QLineEdit,"./sf_silica_fume")
        self.sf_water_absorb = self.findChild(QLineEdit,"./sf_water_absorb")
        self.sf_density = self.findChild(QLineEdit,"./sf_density")
        self.sf_cation = self.findChild(QLineEdit,"./sf_cation")
        self.sf_sulfate_conc = self.findChild(QLineEdit,"./sf_sulfate_conc")
        self.sf_immersion = self.findChild(QLineEdit,"./sf_immersion")
        self.sf_wetting_time = self.findChild(QLineEdit,"./sf_wetting_time")
        self.sf_cAgg_size = self.findChild(QLineEdit,"./sf_cAgg_size")
        self.sf_drying_time = self.findChild(QLineEdit,"./sf_drying_time")
        self.sf_drying_temp = self.findChild(QLineEdit,"./sf_drying_temp")
        self.sf_no_cycles = self.findChild(QLineEdit,"./sf_no_cycles")
        self.sf_fAgg_size = self.findChild(QLineEdit,"./sf_fAgg_size")
        self.sf_Cstr = self.findChild(QLineEdit,"./sf_Cstr")
        self.sf_prediction = self.findChild(QLineEdit,"./sf_prediction_xgb")
        #Functionality Connection
        self.button_rac.clicked.connect(self.rac_pred)
        self.button_cs.clicked.connect(self.cs_pred)
        self.button_c.clicked.connect(self.c_pred)
        self.button_cl.clicked.connect(self.cl_pred)
        self.button_sf.clicked.connect(self.sf_pred)
        self.rac_fitness_xgb.clicked.connect(self.rac_fitness_xgb_graph)
        self.rac_acc_xgb.clicked.connect(self.rac_acc_xgb_graph)
        self.rac_residual_xgb.clicked.connect(self.rac_residual_xgb_graph)
        self.rac_corr_matrix.clicked.connect(self.rac_corr_matrix_graph)
        self.cs_fitness_xgb.clicked.connect(self.cs_fitness_xgb_graph)
        self.cs_residual_xgb.clicked.connect(self.cs_residual_xgb_graph)
        self.cs_acc_xgb.clicked.connect(self.cs_acc_xgb_graph)
        self.cs_corr_matrix.clicked.connect(self.cs_corr_matrix_graph)
        self.c_fitness_xgb.clicked.connect(self.c_fitness_xgb_graph)
        self.c_residual_xgb.clicked.connect(self.c_residual_xgb_graph)
        self.c_acc_xgb.clicked.connect(self.c_acc_xgb_graph)
        self.c_corr_matrix.clicked.connect(self.c_corr_matrix_graph)
        self.cl_fitness_xgb.clicked.connect(self.cl_fitness_xgb_graph)
        self.cl_residual_xgb.clicked.connect(self.cl_residual_xgb_graph)
        self.cl_acc_xgb.clicked.connect(self.cl_acc_xgb_graph)
        self.cl_corr_matrix.clicked.connect(self.cl_corr_matrix_graph)
        self.sf_fitness_xgb.clicked.connect(self.sf_fitness_xgb_graph)
        self.sf_residual_xgb.clicked.connect(self.sf_residual_xgb_graph)
        self.sf_acc_xgb.clicked.connect(self.sf_acc_xgb_graph)
        self.sf_corr_matrix.clicked.connect(self.sf_corr_matrix_graph)
        #Adding Graph Functionality

    def rac_fitness_xgb_graph(self):
        filepath = "./graphs_data/goodness_rac.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def rac_acc_xgb_graph(self):
        filepath = "./graphs_data/prediction_actual_RAC.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def rac_residual_xgb_graph(self):
        filepath = "./graphs_data/RMSE_RAC.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()
    
    def rac_corr_matrix_graph(self):
        filepath = "./graphs_data/cor_matrix_rac.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()
    
    def cs_fitness_xgb_graph(self):
        filepath = "./graphs_data/nac_goodness.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()
    
    def cs_residual_xgb_graph(self):
        filepath = "./graphs_data/RMSE_NAC.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def cs_acc_xgb_graph(self):
        filepath = "./graphs_data/prediction_actual_NAC.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def cs_corr_matrix_graph(self):
        filepath = "./graphs_data/cor_matrix_nac.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()
    
    def c_fitness_xgb_graph(self):
        filepath = "./graphs_data/goodness carbonization.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()
    
    def c_residual_xgb_graph(self):
        filepath = "./graphs_data/RMSE_C.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def c_acc_xgb_graph(self):
        filepath = "./graphs_data/prediction_actual_Carbonization.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def c_corr_matrix_graph(self):
        filepath = "./graphs_data/cor_matrix_c.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def cl_fitness_xgb_graph(self):
        filepath = "./graphs_data/goodness_cl.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()
    
    def cl_residual_xgb_graph(self):
        filepath = "./graphs_data/RMSE_cl.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()
    
    def cl_acc_xgb_graph(self):
        filepath = "./graphs_data/prediction_actual_cl.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def cl_corr_matrix_graph(self):
        filepath = "./graphs_data/cor_matrix_cl.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def sf_fitness_xgb_graph(self):
        filepath = "./graphs_data/goodness_sf.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    def sf_residual_xgb_graph(self):
        filepath = "./graphs_data/RMSE_sf.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()
    
    def sf_acc_xgb_graph(self):
        filepath = "./graphs_data/prediction_actual_Sf.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()
    
    def sf_corr_matrix_graph(self):
        filepath = "./graphs_data/cor_matrix_sf.png"
        dialog = GraphDialog(filepath)
        dialog.exec_()

    #Functionality Definition
    def sf_pred(self):
        sf_cement = float(self.sf_cement.text())
        sf_water = float(self.sf_water.text())
        sf_NCA = float(self.sf_NCA.text())
        sf_RCA = float(self.sf_RCA.text())
        sf_SP = float(self.sf_SP.text())
        sf_silica_fume = float(self.sf_silica_fume.text())
        sf_water_absorb = float(self.sf_water_absorb.text())
        sf_density = float(self.sf_density.text())
        sf_cation = float(self.sf_cation.text())
        sf_sulfate_conc = float(self.sf_sulfate_conc.text())
        sf_immersion = float(self.sf_immersion.text())
        sf_wetting_time = float(self.sf_wetting_time.text())
        sf_cAgg_size = float(self.sf_cAgg_size.text())
        sf_drying_time = float(self.sf_drying_time.text())
        sf_drying_temp = float(self.sf_drying_temp.text())
        sf_no_cycles = float(self.sf_no_cycles.text())
        sf_fAgg_size = float(self.sf_fAgg_size.text())
        sf_Cstr = float(self.sf_Cstr.text())
        data = [[sf_cement,sf_water,sf_NCA,sf_RCA,sf_silica_fume,sf_water_absorb,sf_density,sf_cation,sf_sulfate_conc,sf_immersion,sf_wetting_time,sf_drying_time,sf_drying_temp,sf_no_cycles,sf_Cstr,sf_fAgg_size,sf_cAgg_size,sf_SP]]
        transformed_data = self.transform_sf.transform(data)
        prediction = self.sf_model.predict(transformed_data)
        self.sf_prediction.setText(str(prediction[0]))
    def cl_pred(self):
          
        cl_curing_age = float(self.cl_curing_age.text())
        cl_water_content = float(self.cl_water_content.text())
        cl_sand_content = float(self.cl_sand_content.text())
        cl_cement_content = float(self.cl_cement_content.text())
        cl_NCA = float(self.cl_NCA.text())
        cl_RCA = float(self.cl_RCA.text())
        cl_water_absorb = float(self.cl_water_absorb.text())
        cl_density = float(self.cl_density.text())
        cl_fly_ash = float(self.cl_fly_ash.text())
        cl_slag = float(self.cl_slag.text())
        cl_silica_fume = float(self.cl_silica_fume.text())
        cl_fAgg_size = float(self.cl_fAgg_size.text())
        cl_cAgg_size = float(self.cl_cAgg_size.text())
        cl_SP = float(self.cl_SP.text())
        cl_Cstr = float(self.cl_Cstr.text())
        data = [[cl_curing_age,cl_water_content,cl_sand_content,cl_cement_content,cl_NCA,cl_RCA,cl_water_absorb,cl_density,cl_fly_ash,cl_slag,cl_silica_fume,cl_fAgg_size,cl_cAgg_size,cl_SP,cl_Cstr]]
        transformed_data = self.transform_cl.transform(data)
        prediction = self.cl_model.predict(transformed_data)
        self.cl_charge_prediction.setText(str(prediction[0]))
    def c_pred(self):
             
        c_water_content = float(self.c_water_content.text())
        c_cement = float(self.c_cement.text())
        c_CO2 = float(self.c_CO2.text())
        c_temperature = float(self.c_temperature.text())
        c_relative_humidity = float(self.c_relative_humidity.text())
        c_exposure = float(self.c_exposure.text())
        c_wat_absorption = float(self.c_wat_absorption.text())
        c_RCA = float(self.c_RCA.text())
        c_curing_age = float(self.c_curing_age.text())
        c_fAgg_size = float(self.c_fAgg_size.text())
        c_cAgg_size = float(self.c_cAgg_size.text())
        c_SP = float(self.c_SP.text())
        c_Cstr = float(self.c_Cstr.text())
        data = [[c_water_content,c_cement,c_CO2,c_temperature,c_relative_humidity,c_exposure,c_wat_absorption,c_RCA,c_curing_age,c_fAgg_size,c_cAgg_size,c_SP,c_Cstr]]
        transformed_data = self.transform_c.transform(data)
        prediction = self.c_model.predict(transformed_data)
        self.c_depth_prediction.setText(str(prediction[0]))
    def cs_pred(self):
            
        cs_cement = float(self.cs_cement.text())
        cs_slag = float(self.cs_slag.text())
        cs_fly_ash = float(self.cs_fly_ash.text())
        cs_water = float(self.cs_water.text())
        cs_SP = float(self.cs_SP.text())
        cs_cAgg = float(self.cs_cAgg.text())
        cs_fAgg = float(self.cs_fAgg.text())
        cs_age = float(self.cs_age.text())
        data = [[cs_cement,cs_slag,cs_fly_ash,cs_water,cs_SP,cs_cAgg,cs_fAgg,cs_age]]
        transformed_data = self.transform_cs.transform(data)
        prediction = self.cs_model.predict(transformed_data)
        self.cs_prediction.setText(str(prediction[0]))
    def rac_pred(self):
         
        rac_water = float(self.rac_water.text())
        rac_cement = float(self.rac_cement.text())
        rac_sand = float(self.rac_sand.text())
        rac_nca = float(self.rac_nca.text())
        rac_rca = float(self.rac_rca.text())
        rac_sp = float(self.rac_sp.text())
        rac_dia_max = float(self.rac_dia_max.text())
        rac_density = float(self.rac_density.text())
        rac_water_absorption = float(self.rac_water_absorption.text())
        data = [[rac_water,rac_cement,rac_sand,rac_nca,rac_rca,rac_sp,rac_dia_max,rac_density,rac_water_absorption]]
        transformed_data = self.transform_det.transform(data)
        prediction = self.rac_model.predict(transformed_data)
        self.rac_prediction.setText(str(prediction[0]))

class splashscreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen,self).__init__()
        uic.loadUi("./splashscreen.ui",self)
        pixmap = QPixmap("./SplashScreen_actual.png")
        self.setPixmap(pixmap)
        self.progressBar = self.findChild(QProgressBar,"progressBar")
    def progress(self):
        for i in range(100): 
            time.sleep(0.1)
            self.progressBar.setValue(i)

app=QApplication(sys.argv)
splash = splashscreen()
splash.show()
splash.progress()
UIWindow = UI()
UIWindow.show()
splash.finish(UIWindow)
app.exec_()