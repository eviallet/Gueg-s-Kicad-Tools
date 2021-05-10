
import pcbnew
import wx
from .assign_net_to_vias_gui import AssignNetToViasGui


class AssignNetToViasDialog(AssignNetToViasGui):

    def __init__(self):
        # Dialog setup
        super(AssignNetToViasDialog, self).__init__(None)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.m_btnLayoutApply.Bind(wx.EVT_BUTTON, self.onApply)
        self.m_btnLayoutCancel.Bind(wx.EVT_BUTTON, self.onClose)

        # Getting the pcbnew board handle
        self.board = pcbnew.GetBoard()

        # Update dialog according to board state
        self.populateNets()
        
        self.vias, self.netlessVias = self.findVias()
        self.m_viaCount.SetLabelText('Found ' + str(len(self.netlessVias)) + ' netless vias.')

        
    def populateNets(self):
        self.board.BuildListOfNets()

        self.nets = self.board.GetNetsByName()
        netnames = self.nets.keys()

        self.m_comboBox.Clear()

        for net in netnames:
            if (net != None) and (net != ""):
                self.m_comboBox.Append(str(net))
    

    def findVias(self):
        tracks = self.board.GetTracks()
        vias = []
        netlessVias = []

        for item in tracks:
            if type(item) is pcbnew.VIA:
                vias.append(item)

                if item.GetNet().GetNetname() == '':
                    netlessVias.append(item)
                    item.SetBrightened()

        return vias, netlessVias
        
    
    def updateVias(self, netname):
        netcode = self.nets[netname].GetNet()

        for via in self.vias:
            viaNetname = via.GetNet().GetNetname()
            if viaNetname in [netname, '']:
                via.SetNetCode(netcode)
        
        pcbnew.Refresh()


    def unhighlightVias(self):
        for via in self.netlessVias:
            via.ClearBrightened()


    def onApply(self, event):
        netname = self.m_comboBox.GetStringSelection()
        self.updateVias(netname)
        self.onClose(event)


    def onClose(self, event):
        self.unhighlightVias()
        self.Destroy()
    

