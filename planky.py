from gi.repository import Gtk
import os
 
def on_tree_selection_changed(tree_selection):
 model, treeiter = tree_selection.get_selected()
 if treeiter != None: 
  label.set_text(model[treeiter][0])
 
def load_file(widget):
  model.clear()
  file_list = os.listdir('/home/frankity/.config/plank/dock1/launchers')

  for line in file_list:
   model.append([line])
  label.set_text("")

def but_call(widget,data=None):
    window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
    window.set_size_request(400, 100)
    window.set_title("Add a new Application")
    window.set_position(Gtk.WindowPosition.CENTER)
    window.set_border_width(0)
    window.show()

def on_btnref_clicked(widget):
  print("Refresh clicked")

def on_btnadd_clicked(widget):
  print("Add clicked")

def on_btndel_clicked(widget):
  path = '/home/frankity/.config/plank/dock1/launchers'
  model, treeiter = tree_selection.get_selected()
  if treeiter is not None:
                print "%s has been removed" %(model[treeiter][0])
                model.remove(treeiter)
                os.remove(path + "/" + label.get_text())

win = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
win.set_size_request(450, 300)
win.set_title("Planky")
win.set_position(Gtk.WindowPosition.CENTER)
win.set_border_width(0)
win.connect("delete-event", Gtk.main_quit)
 
vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
win.add(vbox)

btnref = Gtk.ToolButton(Gtk.STOCK_REFRESH)
btnref.connect("clicked", load_file)
		
btnadd = Gtk.ToolButton(Gtk.STOCK_ADD)
btnadd.connect("clicked", but_call)
		
btndel = Gtk.ToolButton(Gtk.STOCK_DELETE)
btndel.connect("clicked", on_btndel_clicked)

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
 
treeview = Gtk.TreeView()  
renderer = Gtk.CellRendererText()    
column = Gtk.TreeViewColumn("Tracks", renderer, text=0)  
treeview.append_column(column)
scroller.add(treeview)
 
model = Gtk.ListStore(str)             

treeview.set_model(model)
 
tree_selection = treeview.get_selection()     
tree_selection.connect("changed", on_tree_selection_changed)

label = Gtk.Label("")
vbox.pack_end(label, expand=False, fill=True, padding=0)
#grid.attach_next_to(label, scroller, Gtk.PositionType.BOTTOM, 1, 1)

label.set_text("asd") 

win.show_all()
Gtk.main()