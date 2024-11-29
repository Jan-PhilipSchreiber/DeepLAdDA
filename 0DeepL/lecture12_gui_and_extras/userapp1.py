# Import the tkinter module
import tkinter
import pandas as pd
import numpy as np
import tensorflow as tf
import keras

# load model
model = keras.saving.load_model("lecture12_gui_and_extras/mobilephonemodel.keras")

# category names for predictions
categories = ['1: Cheap', '2: Avg-', '3: Avg+', '4: Expensive']

# these are the fields we need to get from the UI
# in order to use our model
# tester_row = {
#     'battery_power': 800, 
#     'fc': 12, 
#     'int_memory': 2,  
#     'mobile_wt': 300, 
#     'n_cores': 4, 
#     'pc': 36,
#     'px_width': 1890,
#     'px_height': 1222, 
#     'ram': 8096,
#     'sc_h': 13, 
#     'sc_w': 4, 
#     'talk_time': 19
# }

# quickly test that the model works as in the Jupyter
# convert to pandas-format
# this works okay!
# tester_row = pd.DataFrame([tester_row])
# result = model.predict(tester_row)[0]
# result_text = categories[np.argmax(result)]
# print(result_text)

# Creating the GUI window.
window = tkinter.Tk()
window.title("Mobilephone Price Predicterator v.1.03456bc")
window.geometry("500x700")
window.option_add( "*font", "lucida 12 bold" )

# Creating our text widget.
sample_text = tkinter.Entry(window)
sample_text.pack()
 
# Creating the function to set the text 
# with the help of button
def set_prediction_result():
 
    # Delete is going to erase anything
    # in the range of 0 and end of file,
    # The respective range given here
    sample_text.delete(0,"end")
     
    # Insert method inserts the text at
    # specified position, Here it is the
    # beginning
    sample_text.insert(0, "Text set by button")
 
# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = tkinter.Button(window, height=1, width=10, text="Predict", 
                    command=set_prediction_result)
 
set_up_button.pack()
 
window.mainloop()