import random
import string
from itertools import groupby
from tkinter import *
from tkinter import Text, Tk, ttk
from tkinter import filedialog
from PIL import Image, ImageTk
  
# class to contain data and variables so I'm not goofing around with
# global variables every 2 seconds
# Should've used multiple classes to keep things pretty, but that would take a lot of effort and re-debugging at this point
class data_cont():
    def __init__(self):
        self.text = ""
        self.qgrev = ""
        self.ci_chars = ""
        self.ci_ints = ""
        self.dataCheck = ""
        # Strangeness for NTL/Frontier support
        self.blueGrad = ""
        self.ntl_blueGrad = "4relj0kc"
        self.fro_blueGrad = "ukjge-f2"
        
        self.redGrad = ""
        self.ntl_redGrad = "521,m"
        self.fro_redGrad = "vsr76"
        
        self.purpleGrad = ""
        self.ntl_purpleGrad = "t-8aqz"
        self.fro_purpleGrad = "l/y8h0"
        
        self.greenGrad = ""
        self.ntl_greenGrad = "ho9pv"
        self.fro_greenGrad = "dpzq3"
        
        self.yellowGrad = ""
        self.ntl_yellowGrad = "6gbw"
        self.fro_yellowGrad = "wc4i"
        
        self.earthyGrad = ""
        self.ntl_earthyGrad = "hf7ngi"
        self.fro_earthyGrad = "dbx5co"       
        # List needs re-initialized later. 
        self.grad_list = [self.blueGrad,self.redGrad,self.purpleGrad,self.greenGrad,self.yellowGrad,self.earthyGrad]
        
        self.colorchar = ""
        # More support strangeness
        self.ntl_colors = string.digits + "-" + string.ascii_lowercase + ","
        self.fro_colors = string.digits + "-" + string.ascii_lowercase + "/"
        
        self.counter = 0
        self.imDict ={}
        self.imList = []
        self.shuff_str = ""
        self.shuff_lst = []
        self.shuff_dict = {}
        self.cust_pat_list = []
        self.boo = True
        self.result = ""
        self.pat_choice = 0
        self.rep1_choice = 1
        self.rep2_choice = 1
        self.rep3_choice = 1
        self.rep4_choice = 1
        self.char1_choice = ""
        self.char1_choice = ""
        self.char1_choice = ""
        self.char1_choice = ""
        self.cp1 = ""
        self.cp2 = ""
        self.cp3 = ""
        self.cp4 = ""
        self.image_dict = {}
        self.image_list = []
        self.image_xcor = 10
        self.ntl_dict = {}
        self.fro_dict = {}
data = data_cont()




# After checking if has pyfiglet and found not guilty, run this to switch text
def switch_text():
    data.text ="**Advanced Slither.io**\n**Skin Pattern Generator**\n**By Cursed Pellets**"
# Checking if has pyfiglet    
try:
    import pyfiglet as PYF
    data.text = PYF.figlet_format(text="Cursed\n   Pellets\n       Skin\n          Generator")
except ModuleNotFoundError:
    switch_text()

# Action! Functions, patterns defined here

# Random Pattern Generator
def quick_grad_one():
    check_platform()
    data.result = ""
    for i in range(random.randrange(1,6,1)):
        data.result += random.choice(data.grad_list)
    rp_textField.delete('1.0', END)    
    rp_textField.insert(END, data.result)
    
def quick_grad_two():
    check_platform()
    data.result = random.choice(data.grad_list)
    data.qgrev = "".join(reversed(data.result))
    data.result += data.qgrev
    rp_textField.delete('1.0', END)    
    rp_textField.insert(END, data.result)
    
def generate_random_pattern():
    check_platform()
    # Clearing results so that we don't add pattern to existing pattern when hitting button
    data.result = ""
    # This will decide which set of for loops.
    data.pat_choice = random.randrange(0,4,1)
    # How many loops
    data.rep1_choice = random.randrange(1,5,1)
    data.rep2_choice = random.randrange(1,5,1)
    data.rep3_choice = random.randrange(1,5,1)
    data.rep4_choice = random.randrange(1,5,1)
    # Choosing character codes
    data.char1_choice = random.choice(data.colorchar)
    data.char2_choice = random.choice(data.colorchar)
    data.char3_choice = random.choice(data.colorchar)
    data.char4_choice = random.choice(data.colorchar)
    if data.pat_choice == 0:
        for i in range(data.rep1_choice):
            data.result += data.char1_choice
            for i in range(data.rep2_choice):
                data.result += data.char2_choice
    if data.pat_choice == 1:
        for i in range(data.rep1_choice):
            data.result += data.char1_choice
            for i in range(data.rep2_choice):
                data.result += data.char2_choice
                for i in range(data.rep3_choice):
                    data.result += data.char3_choice
    if data.pat_choice == 2:
        for i in range(data.rep1_choice):
            data.result += data.char1_choice
            for i in range(data.rep2_choice):
                data.result += data.char2_choice
            for i in range(data.rep3_choice):
                    data.result += data.char3_choice
    if data.pat_choice == 3:
        for i in range(data.rep1_choice):
            data.result += data.char1_choice
            for i in range(data.rep2_choice):
                data.result += data.char2_choice
                for i in range(data.rep3_choice):
                    data.result += data.char3_choice
                    for i in range(data.rep4_choice):
                        data.result += data.char4_choice
                    for i in range(data.rep2_choice):
                            data.result += data.char2_choice
    rp_textField.delete('1.0', END)    
    rp_textField.insert(END, data.result)
    
def reverse_pattern():
    data.result = rp_textField.get('1.0',END)
    data.result = data.result.strip('\n')
    data.result = "".join(reversed(data.result))
    rp_textField.delete('1.0', END)    
    rp_textField.insert(END, data.result)

# Using itertools 'groupby' to group pattern, then iterate through after unpacking
def shuffle_pattern():
    data.result = rp_textField.get('1.0',END)
    data.result = data.result.strip('\n')
    data.shuff_str = groupby(data.result)
    for key, item in data.shuff_str:
        data.shuff_dict[key] = list(item)
    data.result = ""
    for key in data.shuff_dict:
        data.shuff_lst.append(key)
    random.shuffle(data.shuff_lst)
    for key in data.shuff_lst:
        for items in data.shuff_dict[key]:
            data.result += items
    rp_textField.delete('1.0', END)    
    rp_textField.insert(END, data.result)
    data.shuff_str = ""
    data.shuff_lst = []
    data.shuff_dict = {}
       
def copyIt():    
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    textcopy = rp_textField.get('1.0',END)
    r.clipboard_append(textcopy)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

def custom_pattern_generator():
    check_platform()
    # How many reps
    data.rep1_choice = r_row1.get('1.0', END)
    data.rep1_choice = data.rep1_choice.strip('\n')
    data.cust_pat_list.append(data.rep1_choice)
    data.rep2_choice = r_row2.get('1.0', END)
    data.rep2_choice = data.rep2_choice.strip('\n')
    data.cust_pat_list.append(data.rep2_choice)
    data.rep3_choice = r_row3.get('1.0', END)
    data.rep3_choice = data.rep3_choice.strip('\n')
    data.cust_pat_list.append(data.rep3_choice)
    data.rep4_choice = r_row4.get('1.0', END)
    data.rep4_choice = data.rep4_choice.strip('\n')
    data.cust_pat_list.append(data.rep4_choice)
    
    # Get character color codes
    data.char1_choice = c_row1.get('1.0', END)
    data.char1_choice = data.char1_choice.strip('\n')
    data.char2_choice = c_row2.get('1.0', END)
    data.char2_choice = data.char2_choice.strip('\n')
    data.char3_choice = c_row3.get('1.0', END)
    data.char3_choice = data.char3_choice.strip('\n')
    data.char4_choice = c_row4.get('1.0', END)
    data.char4_choice = data.char4_choice.strip('\n')
    
    # Check input - intergers only in rep boxes, color code chars only in color code boxes
    data.dataCheck = data.rep1_choice + data.rep2_choice + data.rep3_choice + data.rep4_choice

    for char in data.dataCheck:
        if char not in string.digits:
            data.boo = False
            
    data.dataCheck = data.char1_choice + data.char2_choice + data.char3_choice + data.char4_choice
    # data.colorchar, string.digits
    for char in data.dataCheck:
        if char not in data.colorchar:
            data.boo = False
            
    # All good? Run the rest of the script        
    if data.boo:
        if len(data.rep1_choice) >= 1:
            data.rep1_choice = int(data.rep1_choice)
            data.cp1 = str(data.char1_choice*data.rep1_choice)
        if len(data.rep2_choice) >= 1:
            data.rep2_choice = int(data.rep2_choice)
            data.cp2 = str(data.char2_choice*data.rep2_choice)
        if len(data.rep3_choice) >= 1:
            data.rep3_choice = int(data.rep3_choice)
            data.cp3 = str(data.char3_choice*data.rep3_choice)
        if len(data.rep4_choice) >= 1:
            data.rep4_choice = int(data.rep4_choice)
            data.cp4 = str(data.char4_choice*data.rep4_choice)
        
        data.result = data.cp1+data.cp2+data.cp3+data.cp4
        #data.result = data.result.replace('\n','')
            
        rp_textField.delete('1.0', END)    
        rp_textField.insert(END, data.result)
    else:
        data.boo = True
        rp_textField.delete('1.0', END)    
        rp_textField.insert(END, "Sorry, something didn't work.\nPlease check color code accuracy in color box.\nPlease ensure no non-integers in repetiton box.")

# Select Gradient and reversed gradient functions
 
def blue_grad():
    check_platform()
    rp_textField.insert(END, data.blueGrad)
def blue_grad_rev():
    check_platform()
    rp_textField.insert(END, "".join(reversed(data.blueGrad)) ) 
def green_grad():
    check_platform()
    rp_textField.insert(END, data.greenGrad)
def green_grad_rev():
    check_platform()
    rp_textField.insert(END, "".join(reversed(data.greenGrad)))
def red_grad():
    check_platform()
    rp_textField.insert(END, data.redGrad)
def red_grad_rev():
    check_platform()
    rp_textField.insert(END, "".join(reversed(data.redGrad)))
def purple_grad():
    check_platform()
    rp_textField.insert(END, data.purpleGrad)
def purple_grad_rev():
    check_platform()
    rp_textField.insert(END, "".join(reversed(data.purpleGrad)) )
def yellow_grad():
    check_platform()
    rp_textField.insert(END,  data.yellowGrad)
def yellow_grad_rev():
    check_platform()
    rp_textField.insert(END, "".join(reversed(data.yellowGrad)))
def earthy_grad():
    check_platform()
    rp_textField.insert(END, data.earthyGrad)
def earthy_grad_rev():
    check_platform()
    rp_textField.insert(END, "".join(reversed(data.earthyGrad)) )

def clear_field():
    rp_textField.delete('1.0', END)

def character_inserter():
    check_platform()
     # data.colorchar, string.digits
     #Set boolean value in case we missed it somewhere.
    data.boo = True
    data.result = rp_textField.get('1.0',END)
    data.result = data.result.strip('\n')
    data.ci_chars = ins_chars.get('1.0', END)
    data.ci_chars = data.ci_chars.strip('\n')
    data.ci_ints = ins_int.get('1.0', END)
    data.ci_ints = data.ci_ints.strip('\n')
    
    # Check for non-intergers in interger box
        # Check for non color code characters in color code character box
        
    for char in data.ci_chars:
        if char not in data.colorchar:
            data.boo = False
            rp_textField.delete('1.0', END)
            rp_textField.insert(END, "Something didn't work.\nPlease check color code characters.")
            
    for dig in data.ci_ints:
        if dig not in string.digits:
            data.boo = False
            rp_textField.delete('1.0', END)
            rp_textField.insert(END, "Something didn't work.\nPlease check for non integers in 'Times' box.")
            
    if data.boo:        
        data.result = data.ci_chars.join(data.result[i:i+int(data.ci_ints)] for i in range(0, len(data.result), 3))   
        rp_textField.delete('1.0', END)
        rp_textField.insert(END, data.result)
        
    # Reset boolean value for other functions.    
    data.boo = True
    

# Get selection from dropdown and determine which function to call.
def get_selection():
    if dropdown.get() == "Random Pattern":
        generate_random_pattern()
    if dropdown.get() == "Custom Pattern":
        custom_pattern_generator()
    if dropdown.get() == "Character Inserter":
        character_inserter()

# Match every result for preview on button press.

def skin_preview():
    check_platform()
    # Clear preview_canvas before setting up images.
    preview_canvas.delete('all')
    
    data.result = rp_textField.get('1.0',END)
    data.result = data.result.strip('\n')
    
    for skinCode in data.result:
        data.image_list.append(data.image_dict[skinCode])
            
    for images in data.image_list:       
        preview_canvas.create_image(data.image_xcor,30,anchor=W,image=images)
        data.image_xcor += 10
    #At end of function clear image list so we're not appending to the previous run.
    data.image_xcor = 10    
    data.image_list.clear()

def check_platform():
    if nt_fr_dropdown.get() == "NTL":
        data.colorchar = data.ntl_colors
        data.image_dict = data.ntl_dict
        data.blueGrad = data.ntl_blueGrad
        data.regGrad = data.ntl_redGrad
        data.purpleGrad = data.ntl_purpleGrad 
        data.greenGrad = data.ntl_greenGrad
        data.yellowGrad = data.ntl_yellowGrad
        data.earthyGrad = data.ntl_earthyGrad
        data.grad_list.clear()
        data.grad_list = [data.blueGrad,data.redGrad,data.purpleGrad,data.greenGrad,data.yellowGrad,data.earthyGrad]
    else:
        data.colorchar = data.fro_colors
        data.image_dict = data.fro_dict
        data.blueGrad = data.fro_blueGrad
        data.regGrad = data.fro_redGrad
        data.purpleGrad = data.fro_purpleGrad 
        data.greenGrad = data.fro_greenGrad
        data.yellowGrad = data.fro_yellowGrad
        data.earthyGrad = data.fro_earthyGrad
        data.grad_list.clear()
        data.grad_list = [data.blueGrad,data.redGrad,data.purpleGrad,data.greenGrad,data.yellowGrad,data.earthyGrad]

root = Tk()

root.title("Advanced Slither.io Skin Pattern Generator by Cursed Pellets")
##root.geometry("520x550")
root.configure(bg="#161c22")


# Load all images to be used for preview.
# Must be initialized after root. 
img_1 = ImageTk.PhotoImage(Image.open("assets/swatches/1.png"))
img_2 = ImageTk.PhotoImage(Image.open("assets/swatches/2.png"))
img_3 = ImageTk.PhotoImage(Image.open("assets/swatches/3.png"))
img_4 = ImageTk.PhotoImage(Image.open("assets/swatches/4.png"))
img_5 = ImageTk.PhotoImage(Image.open("assets/swatches/5.png"))
img_6 = ImageTk.PhotoImage(Image.open("assets/swatches/6.png"))
img_7 = ImageTk.PhotoImage(Image.open("assets/swatches/7.png"))
img_8 = ImageTk.PhotoImage(Image.open("assets/swatches/8.png"))
img_9 = ImageTk.PhotoImage(Image.open("assets/swatches/9.png"))
img_10 = ImageTk.PhotoImage(Image.open("assets/swatches/0.png"))
img_11 = ImageTk.PhotoImage(Image.open("assets/swatches/-.png"))
img_12 = ImageTk.PhotoImage(Image.open("assets/swatches/q.png"))
img_13 = ImageTk.PhotoImage(Image.open("assets/swatches/w.png"))
img_14 = ImageTk.PhotoImage(Image.open("assets/swatches/e.png"))
img_15 = ImageTk.PhotoImage(Image.open("assets/swatches/r.png"))
img_16 = ImageTk.PhotoImage(Image.open("assets/swatches/t.png"))
img_17 = ImageTk.PhotoImage(Image.open("assets/swatches/y.png"))
img_18 = ImageTk.PhotoImage(Image.open("assets/swatches/u.png"))
img_19 = ImageTk.PhotoImage(Image.open("assets/swatches/i.png"))
img_20 = ImageTk.PhotoImage(Image.open("assets/swatches/o.png"))
img_21 = ImageTk.PhotoImage(Image.open("assets/swatches/p.png"))
img_22 = ImageTk.PhotoImage(Image.open("assets/swatches/a.png"))
img_23 = ImageTk.PhotoImage(Image.open("assets/swatches/s.png"))
img_24 = ImageTk.PhotoImage(Image.open("assets/swatches/d.png"))
img_25 = ImageTk.PhotoImage(Image.open("assets/swatches/f.png"))
img_26 = ImageTk.PhotoImage(Image.open("assets/swatches/g.png"))
img_27 = ImageTk.PhotoImage(Image.open("assets/swatches/h.png"))
img_28 = ImageTk.PhotoImage(Image.open("assets/swatches/j.png"))
img_29 = ImageTk.PhotoImage(Image.open("assets/swatches/k.png"))
img_30 = ImageTk.PhotoImage(Image.open("assets/swatches/l.png"))
img_31 = ImageTk.PhotoImage(Image.open("assets/swatches/z.png"))
img_32 = ImageTk.PhotoImage(Image.open("assets/swatches/x.png"))
img_33 = ImageTk.PhotoImage(Image.open("assets/swatches/c.png"))
img_34 = ImageTk.PhotoImage(Image.open("assets/swatches/v.png"))
img_35 = ImageTk.PhotoImage(Image.open("assets/swatches/b.png"))
img_36 = ImageTk.PhotoImage(Image.open("assets/swatches/n.png"))
img_37 = ImageTk.PhotoImage(Image.open("assets/swatches/m.png"))
img_38 = ImageTk.PhotoImage(Image.open("assets/swatches/comma.png"))

data.ntl_dict = {"1":img_1,
                   "2":img_2,
                   "3":img_3,
                   "4":img_4,
                   "5":img_5,
                   "6":img_6,
                   "7":img_7,
                   "8":img_8,
                   "9":img_9,
                   "0":img_10,
                   "-":img_11,
                   "q":img_12,
                   "w":img_13,
                   "e":img_14,
                   "r":img_15,
                   "t":img_16,
                   "y":img_17,
                   "u":img_18,
                   "i":img_19,
                   "o":img_20,
                   "p":img_21,
                   "a":img_22,
                   "s":img_23,
                   "d":img_24,
                   "f":img_25,
                   "g":img_26,
                   "h":img_27,
                   "j":img_28,
                   "k":img_29,
                   "l":img_30,
                   "z":img_31,
                   "x":img_32,
                   "c":img_33,
                   "v":img_34,
                   "b":img_35,
                   "n":img_36,
                   "m":img_37,
                   ",":img_38}
data.fro_dict = {"r":img_1,
                   "s":img_2,
                   "t":img_3,
                   "u":img_4,
                   "v":img_5,
                   "w":img_6,
                   "x":img_7,
                   "y":img_8,
                   "z":img_9,
                   "-":img_10,
                   "/":img_11,
                   "h":img_12,
                   "i":img_13,
                   "j":img_14,
                   "k":img_15,
                   "l":img_16,
                   "m":img_17,
                   "n":img_18,
                   "o":img_19,
                   "p":img_20,
                   "q":img_21,
                   "8":img_22,
                   "9":img_23,
                   "a":img_24,
                   "b":img_25,
                   "c":img_26,
                   "d":img_27,
                   "e":img_28,
                   "f":img_29,
                   "g":img_30,
                   "0":img_31,
                   "1":img_32,
                   "2":img_33,
                   "3":img_34,
                   "4":img_35,
                   "5":img_36,
                   "6":img_37,
                   "7":img_38}

options = ["Random Pattern", "Custom Pattern","Character Inserter"]
clicked = StringVar()
clicked.set("Random Pattern")
platform = ["NTL","Frontier"]

# Set up random pattern widgets
    # canvas to put textfield on for the pretty

tf_canvas = Canvas(root, bg='#111111', width=65, height=24, highlightthickness=1, highlightbackground='#000000')
tf_canvas.grid(row=0, rowspan=1, column=0, columnspan=4, padx=5, pady=5)

rp_textField = Text(tf_canvas,
                     bg='#444444',
                     fg='#ffffff',
                     width=60,
                     height=23,
                     borderwidth=1,
                     highlightthickness=1)
rp_textField.grid(row=0, rowspan=1, column=0, columnspan=4, padx=5, pady=5)
rp_textField.config(highlightbackground ='#161c22', highlightcolor='#161c22')
rp_textField.insert(END, data.text)

# drowpdown just chillin here

dropdown = ttk.Combobox(root, value=options, width=15)
dropdown.grid(row=1, column=0, columnspan=2, padx=5, pady=15)
dropdown.current(0)

nt_fr_dropdown = ttk.Combobox(root, value=platform, width=15)
nt_fr_dropdown.grid(row=1, column=2, columnspan=2, padx=5, pady=15)
nt_fr_dropdown.current(0)

# random pattern buttons
rp_btn_gen = Button(root,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Generate",
                  padx=5, pady=5,
                  command=lambda: get_selection())
rp_btn_gen.grid(row=2, column=0, padx=5, pady=5)

rp_btn_shu = Button(root,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Shuffle Code",
                  padx=5, pady=5,
                  command=lambda: shuffle_pattern())
rp_btn_shu.grid(row=2, column=1, padx=5, pady=5)

rp_btn_rev = Button(root,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Reverse",
                  padx=5, pady=5,
                  command=lambda: reverse_pattern())
rp_btn_rev.grid(row=2, column=2, padx=5, pady=5)

rp_btn_cpy = Button(root,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Copy Code",
                  padx=5, pady=5,
                  command=lambda: copyIt())
rp_btn_cpy.grid(row=2, column=3, padx=5, pady=5)

clear_btn = Button(root,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Clear Text Field",
                  padx=5, pady=5,
                  command=lambda: clear_field())
clear_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

preview_btn = Button(root,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Preview Skin",
                  padx=5, pady=5,
                  command=lambda: skin_preview())
preview_btn.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# custom pattern options start here
    #custom pattern canvas for the pretty
cpo_canvas = Canvas(root, bg='#111111', width=50, height=60, highlightthickness=1, highlightbackground='#000000')
cpo_canvas.grid(row=0, rowspan=5, column=4, columnspan=4, padx=5, pady=5, sticky="N")



textLabel = Label(cpo_canvas, bg='#222222', fg='#ffffff', text="Custom Pattern Options", width=50, height=1, padx=5, pady=5)
textLabel.grid(row=0, column=4, columnspan=4, padx=5, pady=5)

textLabel2= Label(cpo_canvas, bg='#111111', fg='#ffffff', text="↓↓↓ Colors ↓↓↓", width=20, height=1)
textLabel2.grid(row=1, column=4, columnspan=4, padx=5, pady=5)
# color row inputs
c_row1 = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
c_row1.grid(row=2, rowspan=1, column=4, padx=1, pady=10)
c_row1.config(highlightbackground ='#161c22', highlightcolor='#161c22')
c_row1.insert(END, 'a')

c_row2 = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
c_row2.grid(row=2, rowspan=1, column=5, padx=0, pady=10)
c_row2.config(highlightbackground ='#161c22', highlightcolor='#161c22')
c_row2.insert(END, 'a')

c_row3 = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
c_row3.grid(row=2, rowspan=1, column=6, padx=1, pady=10)
c_row3.config(highlightbackground ='#161c22', highlightcolor='#161c22')
c_row3.insert(END, 'a')

c_row4 = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
c_row4.grid(row=2, rowspan=1, column=7, padx=1, pady=10)
c_row4.config(highlightbackground ='#161c22', highlightcolor='#161c22')
c_row4.insert(END, 'a')

textLabel3= Label(cpo_canvas, bg='#111111', fg='#ffffff', text="↓↓↓ Repetitions ↓↓↓", width=20, height=1)
textLabel3.grid(row=3, column=4, columnspan=4, padx=5, pady=5)
# rep row inputs
r_row1 = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
r_row1.grid(row=4, rowspan=1, column=4, padx=1, pady=5)
r_row1.config(highlightbackground ='#161c22', highlightcolor='#161c22')
r_row1.insert(END, '1')

r_row2 = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
r_row2.grid(row=4, rowspan=1, column=5, padx=0, pady=5)
r_row2.config(highlightbackground ='#161c22', highlightcolor='#161c22')
r_row2.insert(END, '1')

r_row3 = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
r_row3.grid(row=4, rowspan=1, column=6, padx=1, pady=5)
r_row3.config(highlightbackground ='#161c22', highlightcolor='#161c22')
r_row3.insert(END, '1')

r_row4 = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
r_row4.grid(row=4, rowspan=1, column=7, padx=1, pady=5)
r_row4.config(highlightbackground ='#161c22', highlightcolor='#161c22')
r_row4.insert(END, '1')

#row 5 and 6, column 4
# quick rainbow generator

textLabel5 = Label(cpo_canvas, bg='#222222', fg='#ffffff', text="Character Inserter", width=50, height=1, padx=5, pady=5)
textLabel5.grid(row=5, column=4, columnspan=4, padx=5, pady=5)

ins_chars = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
ins_chars.grid(row=6, rowspan=1, column=4, columnspan=1, padx=5, pady=5)
ins_chars.config(highlightbackground ='#161c22', highlightcolor='#161c22')
ins_chars.insert(END, 'abc')

ciLabel2 = Label(cpo_canvas, bg='#222222', fg='#ffffff', text="Insert Characters, Every: ",padx=5, pady=5)
ciLabel2.grid(row=6, column=5, columnspan=1, padx=5, pady=5)

ins_int = Text(cpo_canvas,
             bg='#444444',
             fg='#ffffff',
             width=5,
             height=1,
             borderwidth=1,
             highlightthickness=1)
ins_int.grid(row=6, rowspan=1, column=6, columnspan=1, padx=5, pady=5)
ins_int.config(highlightbackground ='#161c22', highlightcolor='#161c22')
ins_int.insert(END, '3')

ciLabel3 = Label(cpo_canvas, bg='#222222', fg='#ffffff', text=" Times. ",padx=5, pady=5)
ciLabel3.grid(row=6, column=7, columnspan=1, padx=5, pady=5)


#gradient pattern selection starts here
    #canvas for the pretty

gps_canvas = Canvas(root, bg='#111111', width=60, height=60, highlightthickness=1, highlightbackground='#000000')
gps_canvas.grid(row=0, rowspan=1, column=8, columnspan=4, padx=5, pady=5, sticky="N")



textLabel4 = Label(gps_canvas, bg='#222222', fg='#ffffff', text="Gradient Pattern Selections By Color Grouping", width=60, height=1, padx=5, pady=5)
textLabel4.grid(row=1, column=8, columnspan=4, padx=5, pady=5)

# 1st button row gradient pattern selection
# blue
b_btn_grad = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Blue",
                  padx=5, pady=5,
                  command=lambda: blue_grad())
b_btn_grad.grid(row=2, column=8, padx=5, pady=5)

b_btn_grad_rev = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Blue Rev",
                  padx=5, pady=5,
                  command=lambda: blue_grad_rev())
b_btn_grad_rev.grid(row=2, column=9, padx=5, pady=5)
# red
r_btn_grad = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Red",
                  padx=5, pady=5,
                  command=lambda: red_grad())
r_btn_grad.grid(row=2, column=10, padx=5, pady=5)

r_btn_grad_rev = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Red Rev",
                  padx=5, pady=5,
                  command=lambda: red_grad_rev())
r_btn_grad_rev.grid(row=2, column=11, padx=5, pady=5)

# 2nd button row gradient pattern selection
# green
g_btn_grad = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Green",
                  padx=5, pady=5,
                  command=lambda: green_grad())
g_btn_grad.grid(row=3, column=8, padx=5,pady=5)

g_btn_grad_rev = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Green Rev",
                  padx=5, pady=5,
                  command=lambda: green_grad_rev())
g_btn_grad_rev.grid(row=3, column=9, padx=5,pady=5)
#purple
pu_btn_grad = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Purple",
                  padx=5, pady=5,
                  command=lambda: purple_grad())
pu_btn_grad.grid(row=3, column=10, padx=5,pady=5)

pu_btn_grad_rev = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Purple Rev",
                  padx=5, pady=5,
                  command=lambda: purple_grad_rev())
pu_btn_grad_rev.grid(row=3, column=11, padx=5,pady=5)

# 3rd button row gradient pattern selection
# yellow
y_btn_grad = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Yellow",
                  padx=5, pady=5,
                  command=lambda: yellow_grad())
y_btn_grad.grid(row=4, column=8, padx=5,pady=5)

y_btn_grad_rev = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Yellow Rev",
                  padx=5, pady=5,
                  command=lambda: yellow_grad_rev())
y_btn_grad_rev.grid(row=4, column=9, padx=5,pady=5)
# Earthy
ea_btn_grad = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Earthy",
                  padx=5, pady=5,
                  command=lambda: earthy_grad())
ea_btn_grad.grid(row=4, column=10, padx=5,pady=5)

ea_btn_grad_rev = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Earthy Rev",
                  padx=5, pady=5,
                  command=lambda: earthy_grad_rev())
ea_btn_grad_rev.grid(row=4, column=11, padx=5,pady=5)


#row 5 and 6, column 8
# quick gradient label and buttons

textLabel6 = Label(gps_canvas, bg='#222222', fg='#ffffff', text="Quick Gradient", width=60, height=1, padx=5, pady=5)
textLabel6.grid(row=5, column=8, columnspan=4, padx=5, pady=5)

qg_btn_1 = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Misc Random Gradient",
                  padx=5, pady=5,
                  command=lambda: quick_grad_one())
qg_btn_1.grid(row=6, column=8, columnspan=2, padx=5, pady=5)

qg_btn_2 = Button(gps_canvas,
                  bg='#000000',
                  fg='#ffffff',
                  activebackground='#161c22',
                  activeforeground='#161c22',
                  text="Quick Random Gradient",
                  padx=5, pady=5,
                  command=lambda: quick_grad_two())
qg_btn_2.grid(row=6, column=10, columnspan=2, padx=5, pady=5)

textLabel7 = Label(root, bg='#161c22', width=60, height=1, padx=5, pady=10)
textLabel7.grid(row=10, column=0, columnspan=8, padx=5, pady=5, sticky="S")

textLabel8 = Label(root, bg='#222222', fg='#ffffff', text="Preview", width=60, height=1, padx=5, pady=5)
textLabel8.grid(row=11, column=2, columnspan=8, padx=5, pady=5, sticky="S")

preview_canvas = Canvas(root, bg='#222222', width=1350, height=65, highlightthickness=1, highlightbackground='#111111')
preview_canvas.grid(row=12, rowspan=1, column=0, columnspan=12, padx=1, pady=15, sticky="S")

root.mainloop()


