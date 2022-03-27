from QLabelClickable import clickable
import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "CambioImagen.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.dial.setMinimum(0)
        self.dial.setMaximum(10)
        self.dial.setValue(0)
        self.dial.setSingleStep(1)
        self.dial.valueChanged.connect(self.cambioImg)
        clickable(self.img).connect(self.clicImage)
        self.BtnLimpiar.clicked.connect(self.Limpiar)
        self.lista_imagenes = [":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_Phx.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_Jett.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_Viper.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_ALL_Sova_2.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_Cypher.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_Brimstone.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_sage.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_Omen.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_Breach.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_ALL_Raze_2.png",
                          ":/Imagenes/Imagenes/Agents png/V_AGENTS_587x900_Reyna.png"]

        self.info_imagenes = [["Phoenix","Phoenix es un personaje que brilla por su estilo de combate, donde incendia el campo de batalla con luces y fuego","UK","Duelista",],
                              ["Jett ","Jet es un personaje ágil y con un estilo de combate evasivo para poder tomar riesgos que otros no pueden. Puede correr en círculos alrededor de escaramuzas y cortar enemigos antes de que sepan quién ha sido.","Corea","Duelista",],
                              ["Viper ","Personaje con distintos dispositivos químicos que sirven para controlar el campo de batalla y mermar la visión de los enemigos.","USA","Controlador",],
                              ["Sova ","Personaje que busca, encuentra y elimina enemigos al estilo ruso, con eficiencia y precisión.","Rusia","Iniciador",],
                              ["Cypher ","Ningún secreto está a salvo de este personaje, que siempre está vigilante y controla cualquier movimiento enemigo.","Marruecos","Centinela",],
                              ["Brimstone ","Un personaje que tiene un gran arsenal para tomar ventaja en el campo de batalla y que sirve para dirigir al equipo hasta la victoria.","USA","Contenedor",],
                              ["Sage ","Un seguro de vida para el equipo allá donde vaya, capaz de revivir amigos caídos y ofrecer calma en el campo de batalla.","China","Centinela",],
                              ["Omen ","Un personaje que caza desde las sombras, con teleports y como si de un fantasma se tratara.","?","Contenedor",],
                              ["Breach ","Breach, noveno agente confirmado de Valorant. Es un personaje ofensivo con herramientas de asalto y cargas explosivas, y su papel en el juego es iniciar ataques, coger puntos y despistar a los enemigos.","Suecia","Iniciador",],
                              ["Raze ","Estamos ante una agente de clase duelista que domina las armas explosivas y es perfecta para destrozar grupos de enemigos","Brasil","Duelista",],
                              ["Reyna ","Reyna es la última agente que ha llegado con el parche 1.0 del juego, estamos ante una agente de clase duelista, experta en combates uno contra uno y gran poder ofensivo","Mexico","Duelista",]]

        self.img.setPixmap(QtGui.QPixmap(self.lista_imagenes[0]))
    def cambioImg(self):
        valor = self.dial.value()
        self.img.setPixmap(QtGui.QPixmap(self.lista_imagenes[valor]))

        print(str(valor))

    def clicImage(self):
        valor = self.dial.value()
        if valor == 0:
            self.LeNombre.setText(str(self.info_imagenes[0][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[0][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[0][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[0][3]))
        elif valor == 1:
            self.LeNombre.setText(str(self.info_imagenes[1][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[1][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[1][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[1][3]))
        elif valor == 2:
            self.LeNombre.setText(str(self.info_imagenes[2][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[2][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[2][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[2][3]))
        elif valor == 3:
            self.LeNombre.setText(str(self.info_imagenes[3][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[3][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[3][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[3][3]))
        elif valor == 4:
            self.LeNombre.setText(str(self.info_imagenes[4][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[4][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[4][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[4][3]))
        elif valor == 5:
            self.LeNombre.setText(str(self.info_imagenes[5][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[5][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[5][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[5][3]))
        elif valor == 6:
            self.LeNombre.setText(str(self.info_imagenes[6][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[6][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[6][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[6][3]))
        elif valor == 7:
            self.LeNombre.setText(str(self.info_imagenes[7][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[7][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[7][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[7][3]))
        elif valor == 8:
            self.LeNombre.setText(str(self.info_imagenes[8][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[8][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[8][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[8][3]))
        elif valor == 9:
            self.LeNombre.setText(str(self.info_imagenes[9][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[9][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[9][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[9][3]))
        else:
            self.LeNombre.setText(str(self.info_imagenes[10][0]))
            self.LeDescripcion.setText(str(self.info_imagenes[10][1]))
            self.LeNacionalidad.setText(str(self.info_imagenes[10][2]))
            self.LeOcupacion.setText(str(self.info_imagenes[10][3]))


    def Limpiar (self):
        self.LeNombre.setText("")
        self.LeDescripcion.setText("")
        self.LeNacionalidad.setText("")
        self.LeOcupacion.setText("")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
