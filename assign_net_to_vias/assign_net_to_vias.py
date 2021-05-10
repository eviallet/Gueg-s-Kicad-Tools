
import pcbnew
from .assign_net_to_vias_dialog import AssignNetToViasDialog


class AssignNetToVias(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = "Assign net to vias"
        self.category = "Vias"
        self.description = "Assign a net to every un-netted vias of the schematic"


    def Run(self):
        dialog = AssignNetToViasDialog()
        dialog.Show(True)
        return dialog


