import wx
import xml.sax.handler
from xml import sax
from ovi import Panel
from ovi.xml import reader


class VentanaPrincipal(wx.Frame):
    "Ventana principal del programa"
    def __init__(self,parent,id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800,600))

        #panel principal
        panel = wx.Panel(self, -1);

        #Se crean los paneles de la izquierda y derecha
        panelIzq = Panel.Izquierdo(panel, -1);
        panelDer = Panel.Derecho(panel, -1);

        #Se crea el menu
        menuArchivo = wx.Menu();

        #Los menues de salir y de acerca de son proporcionados por wxWidgets
        menuAbout = menuArchivo.Append(wx.ID_ABOUT, "&Acerca de", "Informacion");
        menuExit = menuArchivo.Append(wx.ID_EXIT, "&Salir", "Sale del programa")


        #Se crea la barra de menues
        menuBar = wx.MenuBar();
        menuBar.Append(menuArchivo, "&File");#Se agrega el menu archivo
        #self.SetMenuBar(menuBar)

        hbox = wx.BoxSizer();
        hbox.Add(panelIzq, 0, wx.LEFT, 5);
        hbox.Add(panelDer, 1, wx.RIGHT, 5);

        panel.SetSizer(hbox);

        readerHandlerContenidos = reader.ContenidosReader();
        parser = sax.make_parser();
        parser.setContentHandler(readerHandlerContenidos);
        parser.parse(open('contenidosIxtli.xml'));

        readerHandlerEquipos = reader.EquiposOVI();
        parser2 = sax.make_parser();
        parser2.setContentHandler(readerHandlerEquipos);
        parser2.parse(open('equiposIxtli.xml'));

        panelDer.setInfoXML(readerHandlerContenidos);
        
        #Establece el lanzador para el panel izquierdo
        panelIzq.setLanzador(panelDer);
            
        self.Centre()
        self.Show(True)

        
        

if __name__=="__main__":
    app = wx.App()
    VentanaPrincipal(None, -1, 'Administrador Proyectos')
    app.MainLoop()
