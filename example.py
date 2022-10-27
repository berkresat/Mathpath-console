import kivy
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatIconButton, MDFlatButton, MDIconButton
from kivy.uix.widget import Widget 
from kivy.properties import NumericProperty 
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
import sympy
from sympy import *
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.segmentedcontrol import MDSegmentedControl, MDSegmentedControlItem
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

x,y,z=symbols("x y z")

kivyy=Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
   
<MenuScreen>:
    id:menuscreen
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                md_bg_color: 1, 1, 1, 1
                MDBoxLayout:
                    id:box_layout
                    orientation:'vertical'
                    pos_hint: {"top": 1}
                    adaptive_height:True
                    md_bg_color: 1, 1, 1, 1
                    MDTopAppBar:
                        id:toolbar
                        title: "Example interface"
                        anchor_title:'center'
                        opposite_colors:True
                        elevation: 10
                        md_bg_color: get_color_from_hex("#7A89EC")

                    MDTextField:
                        id:txt1
                        text:""
                        multiline:True
                        font_size:'22dp'
                        max_height: "120dp"
                        hint_text:'Type an expressions'
                        helper_text:""
                        helper_text_mode: "persistent"
                        active_line:False
                        hint_text_color_focus:'#6B6B6B'
                        on_text:root.follow()
                               
                    AnchorLayout:
                        anchor_x: 'right'
                        anchor_y: 'top'   
                        
                        MDBottomNavigation:
                            panel_color: "#ffffff"
                            size_hint_y:None
                            pos_hint:{'top':1}
                            selected_color_background: "#F6F6F6"
                            
                            MDBottomNavigationItem:
                                id:change_language
                                text: "Lang."
                                icon:"translate-variant"
                                
                            MDBottomNavigationItem:
                                text: "2D"
                                icon:"chart-bell-curve-cumulative"
                                                    
                            MDBottomNavigationItem:
                                text: "3D"
                                icon:"cube-outline"
                        
                
                            MDBottomNavigationItem:
                                id:delete
                                text: "Clear"
                                icon:"delete-forever"

                AnchorLayout:
                    pos_hint:{'top':1}
                    Label:
                        id:lbl
                        text:''
                        color:'black'
                        size_hint_y:None
                        
                    
            
                                 
""")

class MenuScreen(Screen):

    def follow(self):
        try:
            turn=sympify(self.ids.txt1.text)
            self.ids.lbl.text=str(turn)
        except(SympifyError, Exception):
            pass
        


class ExampleApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        screenm = ScreenManager()
        screenm.add_widget(MenuScreen(name='menu'))
        return screenm

kv=ExampleApp().run()
