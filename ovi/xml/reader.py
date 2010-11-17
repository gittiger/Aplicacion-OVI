import xml.sax.handler

class ContenidosReader(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.listaElementos = [];
        self.numProyectos = 0;
        self.bProyecto = False;
        self.bPath = False;#indica si se encontro la ruta
        self.thumbnail = "";
        self.pathProyecto = "";
        self.idVer = "";
        self.nickname = "";
        self.comandoEje = "";
        self.descripcion = "";
    
    def startElement(self, name, attrs):
        if name == 'ListaContenidos':
          numProyectos = int(attrs.get('numProyectos',""));
          fechaAct = attrs.get('fecha',"")
        elif name == 'Proyecto':
          self.bProyecto = True;
          idPro = attrs.get('id',"")
          nombrePro = attrs.get('nombre',"")
          areaConoc = attrs.get('area',"")
        if self.bProyecto == True:
            if name == 'img':
              self.thumbnail = attrs.get('src',"");
            elif name == 'proyectPath':
              self.equipo = attrs.get('equipo', "");
              self.os = attrs.get('os', "");
            elif name == 'path':
              self.bPath = True;
            elif name == 'version':
              self.idVer = attrs.get('id',"")
              self.nickname = attrs.get('name',"")
              self.comandoEje = attrs.get('script',"")
              self.despcripcion = attrs.get('data',"")
            elif name == 'tag':
              ListTags = []
              ListTags.append(attrs.get('id'))          
          
    def endElement(self, name):
        if name == 'Proyecto':
            self.listaElementos.append([self.thumbnail,self.pathProyecto,self.idVer,self.nickname,self.comandoEje,self.descripcion,self.equipo,self.os]);
            self.numProyectos = self.numProyectos+1;
            self.bProyecto = False;

    def characters(self, ch):
        if self.bPath == True:
            self.pathProyecto = ch;
            self.bPath = False;
            

class EquiposOVI(xml.sax.handler.ContentHandler):
    def __init__(self):
        pass

    def startElement(self, name, attrs):
        if name == 'ListaContenidos':
            numContenidos = int(attrs.get('numContenidos',""));
            fechaActualizacionCont = attrs.get('fechaActualizacion', "");
        elif name == 'Equipo':
            nombreEq = attrs.get('nombre',"");
            nombreEq = attrs.get('modelo',"");
            nombreEq = attrs.get('IP',"");
        elif name == 'RefProyecto':
            ListContenidos = [];
            ListContenidos.append(attrs.get('nickname',""));
        elif name == 'ListaSoftware':
            numAplicaciones = int(attrs.get('numAplicaciones',""));
            fechaActualizacionApp = attrs.get('fechaActualizacion', "");
        elif name == 'Software':
            pass;
        elif name == 'UsuarioConexionRemota':
            self.ListUsr = [];
            self.ListUsr.append([attrs.get('nombre',""),attrs.get('password',""),attrs.get('puerto',"")]);

    def characters(self, ch):
        pass;
            
        
