import wx
import os
from ovi.xml import reader

#Tiene la informacion para ejecutar los comandos(remota o localmente) y dar la informacion sobre el proyecto
class Izquierdo(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self, parent, id, size=(200,600), style=wx.BORDER_SUNKEN)
        botonRun = wx.Button(self, -1, "Ejecutar", (10,10))
        botonInfo = wx.Button(self, -1, "Ver Info", (10, 60))

        #se agregan los eventos para los botones
        self.Bind(wx.EVT_BUTTON, self.OnEjecutar, id=botonRun.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnInfo, id=botonInfo.GetId())
        
        self.host="132.248.124.90"

        #El lanzador de aplicaciones es una lista que contiene 2 elementos(la aplicacion, y argumentos)
        self.lanzadorAplicaciones = "";
        
    def OnEjecutar(self, event):
        print(os.getcwd());
        os.system("source /home/ixtli/.bashrc");
        comandoFinal = self.lanzadorAplicaciones.getLanzador() + self.lanzadorAplicaciones.getArgumentos();
        os.system(comandoFinal+" &");
    
    
    def OnInfo(self, event):
        dlgInfo = wx.Dialog(self, -1, "Informacion Proyectos")
        dlgInfo.ShowModal()

    #Establece el lanzador de aplicaciones
    def setLanzador(self, lanz):
        self.lanzadorAplicaciones = lanz;

#Contiene otros controles avanzados como la lista de imagenes de proyectos y el combo box de proyectos a elegir
class Derecho(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self, parent, id, size=(300,300));
        
        mainSizer = wx.BoxSizer(wx.HORIZONTAL);
        self.comboEquipos = wx.ComboBox(self, -1, "HP wx4900", wx.Point(0,0), wx.Size(250,100));
        self.comboEquipos.Insert("HP wx4900",0);
        self.comboEquipos.Insert("SGI Onyx 350",1);
        self.comboEquipos.Insert("Cluster SUN Ultra 40",2);
        #Se une con la funcion para manejar en el cambio del combo box
        self.Bind(wx.EVT_COMBOBOX, self.OnComboElementoClicked, id=self.comboEquipos.GetId())

        #Lista que contiene las imagenes de los proyectos
        self.listProyectos = wx.ListCtrl(self,-1,wx.Point(0,0),wx.Size(150,600));
        
        #Se enlaza el evento para saber cuando se ha dado click
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnElementoClicked, id=self.listProyectos.GetId())
        
        self.listaImagenes = wx.ImageList(110, 110);
        self.listProyectos.SetImageList(self.listaImagenes,wx.IMAGE_LIST_NORMAL); 

        #Sizer para acomodar todos los controles en un layout
        mainSizer.Add(self.comboEquipos, 0, wx.EXPAND, 5);
        mainSizer.Add(self.listProyectos, 1, wx.EXPAND, 5);
        self.SetSizer(mainSizer);

        #Declaracion del lanzador o aplicacion que se va a ejecutar
        self.lanzadorApps = "";
        self.pathLanzador = ""#Ruta al lanzador de aplicaciones
        #argumentos para la aplicacion que se va a ejecutar
        self.argsApp = "";
        self.equipoActual = "HP wx4900";

    def recargarThumbs(self):
          self.listaImagenes.RemoveAll();
          self.listProyectos.DeleteAllItems();
          indImgs = 0;
          for ix in range(0,self.infoXML.numProyectos):
            equipoXML = self.infoXML.listaElementos[ix][6];
            if equipoXML == self.equipoActual:
                print(self.infoXML.listaElementos[ix][3]);
                item1 = wx.ListItem();
                imagenTemp = wx.Image(self.infoXML.listaElementos[ix][0]);
                imagenTemp = imagenTemp.Scale(110,110);
                bitElement = wx.BitmapFromImage(imagenTemp);
                self.listaImagenes.Add(bitElement);
                item1.SetText(self.infoXML.listaElementos[ix][3]);
                item1.SetImage(indImgs);
                self.listProyectos.InsertItem(item1);
                indImgs = indImgs + 1;
                
        
    def setInfoXML(self, xmlDatos):
        self.infoXML = xmlDatos;
        self.recargarThumbs();
                

    def OnElementoClicked(self,event):
        i = event.GetIndex();
        strNomProyecto = self.listProyectos.GetItemText(i)
        
        for ix in range(0,len(self.infoXML.listaElementos)):
            if self.infoXML.listaElementos[ix][3] == strNomProyecto:
                self.pathLanzador = str(self.infoXML.listaElementos[ix][1]);
                self.lanzadorApps= str(self.infoXML.listaElementos[ix][4]);

    def OnComboElementoClicked(self, event):
        cadComboBox = self.comboEquipos.GetValue();
        self.equipoActual = cadComboBox;
        self.recargarThumbs();
       
        

    

            

#Regresa el lanzador de aplicaciones (es decir la aplicacion que se va a ejecutar
    def getLanzador(self):
        return self.pathLanzador+"/"+self.lanzadorApps;
    
    def getArgumentos(self):
        return self.argsApp;

    def getPathProyecto(self):
        return self.pathLanzador;



        
        
