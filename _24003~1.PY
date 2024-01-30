import tkinter as tk
from tkinter import *
import pandas
import random

#1----------------- Variables and Constants Start ---------------------------#
NAME_OF_PROGRAM_TITLE_WINDOW = "FlaShi"
PATH_TO_CSV_FILE_TO_READ = "data/editable_top_200_Spanish_words_by_Freq_w_TitleRows.csv"   # converted to DataFrame
PATH_TO_CSV_FILE_TO_WRITE_TO = "data/updated_words_to_learn_csv"
FRONT_CARD_BACKGROUND_COLOR = "#FFFC93"
BACK_CARD_BACKGROUND_COLOR2 = "#BCC1EA"
TEAL_BACKGROUND_FRONT_OF_CARD = "#CFFFFD"
PURPLE_BACK_OF_CARD_BACKGROUND2 = "#BCC1EA"
FONT_OF_LANGUAGE_TITLE_USED = "Arial", 40, 'italic'
FONT_OF_WORD_USED = "Arial", 50, 'bold'
TIME_WAIT_DELAY = 3600

# Global Variables
# global key, value
key = ""
value = ""
random_number_for_dict_chosen = []
global r2_Value_English_word_on_back
r2_Value_English_word_on_back = []
flip_timer = None

#1----------------- Variables and Constants End ---------------------------#


#2----------------- UI Setup Start ------------------------------------------#
window = Tk()
window.title(NAME_OF_PROGRAM_TITLE_WINDOW)
window.config(padx=50, pady=50, bg=FRONT_CARD_BACKGROUND_COLOR)

# Create canvas and card images
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card_img = PhotoImage(file='card_front_tealblue_CFFFFD_2.png')
back_card_img = PhotoImage(file='card_back_purpleBCC1EA_2.png')
canvas.create_image(400, 263, image=front_card_img)
card_image = canvas.create_image(400, 263, image=front_card_img)
canvas.config(bg=FRONT_CARD_BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

# Fix: you shouldn't create two Language labels and have them display simultaneously: stick with one of each: language title, and word
language_label = Label(window, font=FONT_OF_LANGUAGE_TITLE_USED)
language_label.place(x=300, y=130)
word_label = Label(window, font=FONT_OF_WORD_USED)
word_label.place(x=300, y=243)

#2----------------- UI Setup End ------------------------------------------#

# Data Reading:
editable_dataframe = pandas.read_csv(PATH_TO_CSV_FILE_TO_READ)

#3-------------------- Testing Area Start / Reading and Understanding Keys and Values Start --------------------#

print(f"The length of the pandas DataFrame at the beginning is: {len(editable_dataframe)}")
r1_random_number_picked_for_next_spanish_word_on_front = random.randint(0, len(editable_dataframe) - 1)
specific_row_by_random_gen_num = editable_dataframe.iloc[r1_random_number_picked_for_next_spanish_word_on_front]
print(f"The language lable is: {language_label}")
print(f"The word lable is: {word_label}")

for column in editable_dataframe.columns:
    r2_Value_English_word_on_back = specific_row_by_random_gen_num[column]
    print(
        f"The Key-Value of Index #{r1_random_number_picked_for_next_spanish_word_on_front} is: {r2_Value_English_word_on_back}")

remaining_words_card_index = editable_dataframe.drop(
    editable_dataframe.index[r1_random_number_picked_for_next_spanish_word_on_front])

key2 = r1_random_number_picked_for_next_spanish_word_on_front
value = r2_Value_English_word_on_back
key = editable_dataframe.iloc[r1_random_number_picked_for_next_spanish_word_on_front, 0]

# print(f"The old key was: {key2}")
# print(f"The standard KEY is: {key}")
print(f"The official Key is: {key}")
# print(f"The new official KEY is: {key}")
print(f"The official value is: {value}")
print(f"The length of the Spanish dictionary is NOW: {len(remaining_words_card_index)}")
r1_random_number_picked_for_next_spanish_word_on_front = random.randint(0, len(editable_dataframe) - 1)
key = editable_dataframe.iloc[r1_random_number_picked_for_next_spanish_word_on_front, 0]
value = editable_dataframe.iloc[r1_random_number_picked_for_next_spanish_word_on_front, 1]

#3-------------------- Testing Area End / Reading and Understanding Keys and Values End --------------------#


#4--------------------- Functionality Start ----------------------------#
def update_front_word_label_position():
    window.update_idletasks()
    label_width = word_label.winfo_reqwidth()
    window_width = window.winfo_width()
    x_center = (window_width - label_width) / 2
    word_label.place(x=x_center-50, y=243)

def show_card(is_front):
    if is_front:
        canvas.itemconfig(card_image, image=front_card_img)
        language_label.config(text="Spanish", bg=TEAL_BACKGROUND_FRONT_OF_CARD)
        print(f"This is the show card function, and the key is: {key}")
        print(f"This is the show card function, and the value is: {value}")
        word_label.config(text=key, bg=TEAL_BACKGROUND_FRONT_OF_CARD)
    else:
        canvas.itemconfig(card_image, image=back_card_img)
        language_label.config(text="English", bg=PURPLE_BACK_OF_CARD_BACKGROUND2)
        print(f"This is the show card function, and the key is: {key}")
        print(f"This is the show card function, and the value is: {value}")
        word_label.config(text=value, bg=PURPLE_BACK_OF_CARD_BACKGROUND2)
    update_front_word_label_position()

def flip_card():
    global value, flip_timer
    canvas.itemconfig(card_image, image=back_card_img)
    language_label.config(text="English", bg=PURPLE_BACK_OF_CARD_BACKGROUND2)
    word_label.config(text=value, bg=PURPLE_BACK_OF_CARD_BACKGROUND2)
    update_front_word_label_position()
    flip_timer = None  # Reset flip timer

# Functions for rotating to new word and rotating card
def rotating_to_new_word():
    global key, value, flip_timer

    # cancel the flip timer
    if flip_timer:
        window.after_cancel(flip_timer)

    random_row = random.randint(0, len(editable_dataframe) - 1)
    key = editable_dataframe.iloc[random_row, 0]  # the Spanish word
    value = editable_dataframe.iloc[random_row, 1]  # the English word
    language_label.config(text="Spanish", bg=TEAL_BACKGROUND_FRONT_OF_CARD)
    word_label.config(text=key, bg=TEAL_BACKGROUND_FRONT_OF_CARD)
    update_front_word_label_position()
    show_card(True)
    # reset and start the flip timer over again
    flip_timer = window.after(TIME_WAIT_DELAY, flip_card)
rotating_to_new_word()

# TODO: MORE TESTING (DELETE LATER)
print(f"Before I press the left or right button, the key is: {key} and the value is: {value}")

# dataframe_row_index_number = editable_dataframe[(editable_dataframe['Spanish'] == key).index  # & (editable_dataframe['English'] == value)].index
# dataframe_row_index_number2 = editable_dataframe[(editable_dataframe['English'] == value)].index
# print(dataframe_row_index_number)
# print(dataframe_row_index_number2)




# Button functionality
def right_button_press():
    global editable_dataframe

    dataframe_row_index_number = editable_dataframe[(editable_dataframe['Spanish'] == key) & (editable_dataframe['English'] == value)].index
    for index_number in dataframe_row_index_number:   # if you just want the index number itself and not that PLUS the datatype, you would iterate through it.
        print(f"The official Index Number is: {index_number}")
    # print(dataframe_row_index_number)

    editable_dataframe.drop(dataframe_row_index_number, inplace=True)   # editable_dataframe.index[dataframe_row_index_number]
    print(f"The entry removed was: {key}")
    editable_dataframe.to_csv(PATH_TO_CSV_FILE_TO_WRITE_TO, index=True)    # index=True means indexing is ON and numbers show up in the csv file, final version. # do NOT use as the Read location: 'updated_words_to_learn_csv.csv' to read from, unless you are ready for another Full go around through the program.
    #
    # new_df = df.drop(df.index [random row])
    # df_s1 = df_s1.drop(df_s1.query('sepal_length==5.0').index)
    # window.after(TIME_WAIT_DELAY, flip_card)  #do not use time.sleep() function within a window.mainloop() function. It will break.
                # can always use window.after_cancel() Method to stop it.
    rotating_to_new_word()
        # once done with this button func 1st

'''
# ... [Previous code]

# Global variable for the DataFrame
spanish_word_pandas_DataFrame = pandas.read_csv(PATH_TO_CSV_FILE_TO_READ)

def rotating_to_new_word():
    global key, value, flip_timer, spanish_word_pandas_DataFrame

    if flip_timer:
        window.after_cancel(flip_timer)

    random_row = random.randint(0, len(spanish_word_pandas_DataFrame) - 1)
    key = spanish_word_pandas_DataFrame.iloc[random_row, 0]  # the Spanish word
    value = spanish_word_pandas_DataFrame.iloc[random_row, 1]  # the English word
    language_label.config(text="Spanish", bg=TEAL_BACKGROUND_FRONT_OF_CARD)
    word_label.config(text=key, bg=TEAL_BACKGROUND_FRONT_OF_CARD)
    update_front_word_label_position()
    show_card(True)
    flip_timer = window.after(TIME_WAIT_DELAY, flip_card)

    # Remove the displayed word from the DataFrame
    spanish_word_pandas_DataFrame = spanish_word_pandas_DataFrame.drop(spanish_word_pandas_DataFrame.index[random_row])
    # Save the updated DataFrame
    spanish_word_pandas_DataFrame.to_csv('editable_Spanish_database.csv', index=False)

# ... [Rest of the code]
'''


def wrong_button_press():
    rotating_to_new_word()
    # window.after(TIME_WAIT_DELAY, flip_card)

left_button_img = PhotoImage(file='wrong_button_icon_Yellow-FFFC93.png')
left_wrong_button = tk.Button(image=left_button_img, command=wrong_button_press, highlightthickness=0, borderwidth=0)
left_wrong_button.grid(padx=0, pady=(25, 0), row=2, column=0)

right_button_img = PhotoImage(file='right_button_icon_Yellow-FFFC93.png')
right_correct_button = tk.Button(image=right_button_img, command=right_button_press, highlightthickness=0, borderwidth=0)
right_correct_button.grid(padx=0, pady=(25, 0), row=2, column=1)
#4--------------------- Functionality End ----------------------------#


window.mainloop()