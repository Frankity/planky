from gi.repository import Gtk
import os

class MWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self,title="Planky")

    self.set_size_request(400, 300)    
    self.set_position(Gtk.WindowPosition.CENTER)
    self.set_border_width(0)

    btnref = Gtk.ToolButton(Gtk.STOCK_REFRESH)
    btnref.connect("clicked", self.load_file)
  		
    btnadd = Gtk.ToolButton(Gtk.STOCK_ADD)
    btnadd.connect("clicked", self.but_call)
  		
    btndel = Gtk.ToolButton(Gtk.STOCK_DELETE)
    #btndel.connect("clicked", on_btndel_clicked)

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(vbox)

    toolbar = Gtk.Toolbar()
    toolbar.insert(btnref, 0)
    toolbar.insert(btnadd, 1)
    toolbar.insert(btndel, 2)
    vbox.pack_start(toolbar, expand=False, fill=True, padding=0)

    grid = Gtk.Grid()
    grid.set_column_spacing(20)
    grid.set_row_spacing(20)
    grid.set_column_homogeneous(True)
    vbox.pack_start(grid, expand=False, fill=True, padding=0)
   
    scroller = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
    scroller.set_border_width(1)
    scroller.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    grid.add(scroller)
   
    self.treeview = Gtk.TreeView()  
    renderer = Gtk.CellRendererText()    
    column = Gtk.TreeViewColumn("Tracks", renderer, text=0)  
    self.treeview.append_column(column)
    scroller.add(self.treeview)
   
    self.model = Gtk.ListStore(str)             

    self.treeview.set_model(self.model)
   
    self.tree_selection = self.treeview.get_selection()     
    self.tree_selection.connect("changed", self.on_tree_selection_changed)

    self.label = Gtk.Label("")
    vbox.pack_end(self.label, expand=False, fill=True, padding=0)
    #grid.attach_next_to(label, scroller, Gtk.PositionType.BOTTOM, 1, 1)
  
    self.label.set_text(os.path.expanduser('~')) 

  def on_tree_selection_changed(self,tree_selection):
   model, treeiter = self.tree_selection.get_selected()
   if treeiter != None: 
    self.label.set_text(model[treeiter][0])
   
  def load_file(self, widget):
    self.model.clear()
    file_list = os.listdir(os.path.expanduser('~')+'/.config/plank/dock1/launchers')

    for line in file_list:
      self.model.append([line])
    self.label.set_text("")

  def but_call(self, widget):
      dialog = Gtk.FileChooserDialog("Select an Application", self,
              Gtk.FileChooserAction.OPEN,
              (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
               Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
      
      path = '/usr/share/applications'
      self.add_filters(dialog)
      
      dialog.add_shortcut_folder(path)
      response = dialog.run()
      if response == Gtk.ResponseType.OK:
        print("Open clicked")
        print("File selected: " + dialog.get_filename())
      elif response == Gtk.ResponseType.CANCEL:
        print("Cancel clicked")

      dialog.destroy()

  def add_filters(self, dialog):
    self.filter_any = Gtk.FileFilter()
    self.filter_any.set_name("Plank Files")
    self.filter_any.add_pattern("*.desktop")
    dialog.add_filter(self.filter_any)

  def on_btnref_clicked(widget):
    print("Refresh clicked")

  def on_btnadd_clicked(widget):
    print("Add clicked")

  def on_btndel_clicked(widget):
    path = os.path.expanduser('~')+'/.config/plank/dock1/launchers'
    model, treeiter = tree_selection.get_selected()
    if treeiter is not None:
                  print "%s has been removed" %(model[treeiter][0])
                  model.remove(treeiter)
                  os.remove(path + "/" + label.get_text())

wins = MWindow()
wins.connect("delete-event", Gtk.main_quit)
wins.show_all()
Gtk.main()