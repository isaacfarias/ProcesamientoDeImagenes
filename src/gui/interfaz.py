import gtk
import pygtk


pygtk.require('2.0')

class VentanaPrincipal:

   def delete_event(self, widget,event,data = None):
      print "Bye..."
      return False
      
   def destroy(self,widget,data = None):
      gtk.main_quit()
      
   def selectFile(self,widget,data):
      return None
   
   def __init__(self):
      self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
      self.window.connect("delete_event", self.delete_event)
      self.window.connect("destroy", self.destroy)
      self.window.set_title("Vision x computadoras")
      self.window.set_default_size(640,480)
      
      self.hbox = gtk.HBox(False, 0)
      self.vbox = gtk.VBox(False, 0)
      
      self.boton1SeleccionarArchivo = gtk.FileChooserButton('Selecciona un archivo')
      self.videoViewPort = gtk.ViewPort()
      
      self.hbox.pack_start(self.vbox,True,True,0)
      self.vbox.pack_start(self.boton1SeleccionarArchivo,True,True, 0)
      self.vbox.pack_end(self.videoViewPort,True,True,0)
      self.vbox.show()
      self.hbox.show()
      self.fileChooser.show()
      self.window.add(self.hbox)
      self.window.show()
      gtk.main()
      
if __name__ == "__main__":
   ventana = VentanaPrincipal()
