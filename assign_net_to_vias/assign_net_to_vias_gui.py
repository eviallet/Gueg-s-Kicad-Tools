# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 May 10 2021)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class AssignNetToViasGui
###########################################################################

class AssignNetToViasGui ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainLayout = wx.BoxSizer( wx.VERTICAL )

		m_comboBoxChoices = []
		self.m_comboBox = wx.ComboBox( self, wx.ID_ANY, u"Nets...", wx.DefaultPosition, wx.DefaultSize, m_comboBoxChoices, 0 )
		self.m_comboBox.SetMinSize( wx.Size( 200,-1 ) )

		mainLayout.Add( self.m_comboBox, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_viaCount = wx.StaticText( self, wx.ID_ANY, u"Found 0 vias waiting for a net.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_viaCount.Wrap( -1 )

		mainLayout.Add( self.m_viaCount, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_btnLayout = wx.StdDialogButtonSizer()
		self.m_btnLayoutApply = wx.Button( self, wx.ID_APPLY )
		m_btnLayout.AddButton( self.m_btnLayoutApply )
		self.m_btnLayoutCancel = wx.Button( self, wx.ID_CANCEL )
		m_btnLayout.AddButton( self.m_btnLayoutCancel )
		m_btnLayout.Realize();

		mainLayout.Add( m_btnLayout, 1, wx.EXPAND, 5 )


		self.SetSizer( mainLayout )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


