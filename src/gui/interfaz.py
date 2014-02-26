import gtk
import pygtk


pygtk.require('2.0')

class VentanaPrincipal:

   def delete_event(self, widget,event,data = None):
      print "Cerrando..."
      return false
      
   def destroy(self,widget,data = None):
      gtk.main_quit()
   
   def __init__(self):
      self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
      self.window.connect("delete_event", self.delete_event)
      self.window.connect("destroy", self.destroy)
      self.window.show()
      gtk.main()
      
if __name__ == "__main__":
   ventana = VentanaPrincipal()
