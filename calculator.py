'''
A simple calculator DEMO on GTK3

This is a practise of python on GTK3

Author: lixshnew@gmail.com
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class op:
    NONE = 0
    PLUS = 1
    MINUS= 2
    MUL  = 3
    DIV  = 4

class calculator:
    '''
    Private functions
    ''' 

    def __init__(self):
        self.builder=Gtk.Builder()
        self.builder.add_from_file("calculator.glade")
        self.builder.connect_signals(self)
        self.ent_disp=self.builder.get_object("ent_disp")

        self.__clear_all()

       

    def __clear_all(self):
        self.disp_str="0"
        self.ent_disp.set_text(self.disp_str)
        
        self.op=op.NONE  # operation
        self.reinput=0   # 1: display need to clear first;   0: No need
        
        self.op1=0.0     # operator 1
        self.op2=0.0     # operator 2 

    def __add_figure(self, n):
        if self.reinput==1:
            self.disp_str='0'
            self.reinput=0

        if '.' in self.disp_str and n=='.':
            pass
        elif self.disp_str=="0" and n!='.':
            self.disp_str=n
        else:
            self.disp_str+=n

        self.ent_disp.set_text(self.disp_str)

    def __update_float(self,f):

        if f>1.0e+99:        # set a max value to avoid Gtk.Entry text overflow
            self.__show_error("OUT OF RANGE!")    
            return

        s=str(f)
          
        if 'e' not in s:
            l=s.split('.')
            if int(l[1])==0:
                self.disp_str=l[0]
            else:
                self.disp_str=s
        else:
            self.disp_str=s

        self.ent_disp.set_text(self.disp_str)
        self.reinput=1
    
    def __show_error(self,s):  # The error msg must with '!' at the end which was used as a flag of msg.
        self.disp_str=s
        self.ent_disp.set_text(self.disp_str)
        self.reinput=1
    
    def __toggle_sign(self):
        s=self.disp_str
        if s[0]=='-':
            self.disp_str=s[1:len(s)]
        else:
            self.disp_str='-'+s
        self.ent_disp.set_text(self.disp_str)

    def __backspace(self):
        s=self.disp_str

        if s!='0' and len(s)>1:
            self.disp_str=s[0:len(s)-1]
        elif s!='0':
            self.disp_str='0'
        self.ent_disp.set_text(self.disp_str)

    def __plus(self):
        self.op1=float(self.disp_str)
        self.op=op.PLUS
        self.reinput=1

    def __minus(self):
        self.op1=float(self.disp_str)
        self.op=op.MINUS
        self.reinput=1

    def __mul(self):
        self.op1=float(self.disp_str)
        self.op=op.MUL
        self.reinput=1

    def __div(self):
        self.op1=float(self.disp_str)
        self.op=op.DIV
        self.reinput=1

    def __equ(self):
        if '!' in self.disp_str:  # check if the error is on display
            return

        self.op2=float(self.disp_str)
        '''
        print(self.op1)
        print(self.op2)
        '''
        if self.op==op.PLUS:
            sum=self.op1+self.op2
            self.op1=sum
            self.__update_float(sum)

           
        elif self.op==op.MINUS:
            delta=self.op1-self.op2
            self.op1=delta
            self.__update_float(delta)

        elif self.op==op.MUL:
            prod=self.op1*self.op2
            self.op1=prod
            self.__update_float(prod)

        elif self.op==op.DIV:
            if self.op2!=0.0:
                quot=self.op1/self.op2
                self.op1=quot
                self.__update_float(quot)
            else:
                self.__show_error("DIV BY 0!")

    '''
    Public functions
    '''        
 
    def on_btn_c_clicked(self, *args):
        self.__clear_all()

    def on_btn_ce_clicked(self, *args):
        self.__clear_all()

    def on_btn_bk_clicked(self, *args):
        self.__backspace()

    def on_btn_0_clicked(self,*args):
        self.__add_figure("0")

    def on_btn_1_clicked(self,*args):
        self.__add_figure("1")

    def on_btn_2_clicked(self,*args):
        self.__add_figure("2")

    def on_btn_3_clicked(self,*args):
        self.__add_figure("3")

    def on_btn_4_clicked(self,*args):
        self.__add_figure("4")

    def on_btn_5_clicked(self,*args):
        self.__add_figure("5")

    def on_btn_6_clicked(self,*args):
        self.__add_figure("6")

    def on_btn_7_clicked(self,*args):
        self.__add_figure("7")

    def on_btn_8_clicked(self,*args):
        self.__add_figure("8")

    def on_btn_9_clicked(self,*args):
        self.__add_figure("9")

    def on_btn_dot_clicked(self,*args):
        self.__add_figure(".")

    def on_btn_plus_clicked(self,*args):
        self.__plus()

    def on_btn_minus_clicked(self,*args):
        self.__minus()

    def on_btn_mul_clicked(self,*args):
        self.__mul()

    def on_btn_div_clicked(self,*args):
        self.__div()
 
    def on_btn_equ_clicked(self,*args):
        self.__equ()

    def on_btn_sign_clicked(self,*args):
        self.__toggle_sign()

    def on_win_destroy(self, *args):
        Gtk.main_quit()



'''
Main function
'''

cal=calculator()
win=cal.builder.get_object("win")
win.set_title("Calculator")
win.show_all()

Gtk.main()
