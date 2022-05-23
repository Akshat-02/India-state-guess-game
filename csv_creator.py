"""Do not run this file, it's task is already done.
   
   Multiple runtime will overwrite the India_states & UTs.csv file 
"""

#from turtle import Screen, shape, st
# import turtle
# import pandas

# #Setting the PATH of image
# image = "F:\Python programs\India state guess game\india.gif"

# #Creating screen object
# screen = Screen()

# #Adding our image on screen
# screen.addshape(image)
# shape(image)

# #Get the mouse click coordinates of turtle screen
# #-------------------------------------------
# X = []
# Y = []
# def get_mouse_click_coor(x, y):
#     X.append(x)
#     Y.append(y)


# turtle.onscreenclick(get_mouse_click_coor)
# #-------------------------------------------

# screen.mainloop()                        #Keeps the screen active, use when exitonclick() is not enough


# #Creating a string of all Indian states and uts.
# indian_states_uts = "Andhra Pradesh . Arunachal Pradesh . Assam . Bihar . Chhattisgarh . Goa . Gujarat . Haryana . Himachal Pradesh . Jharkhand . Karnataka . Kerala . Madhya Pradesh . Maharashtra . Manipur . Meghalaya . Mizoram . Nagaland . Odisha . Punjab . Rajasthan . Sikkim . Tamil Nadu . Telangana . Tripura . Uttar Pradesh . Uttarakhand . West Bengal . Andaman and Nicobar . Chandigarh . Daman and Diu . Dadar and Nagar Haveli . Delhi . Jammu and Kashmir . Ladakh . Lakshadweep . Puducherry"

# state_uts_list = indian_states_uts.split(". ")     #Converting string to list using split() method.


# #Creating a dictionary so that we can convert it into Dataframe.
# coor_dict = {
#         "Name" : state_uts_list,
#         "X" : X,
#         "Y" : Y
#     }


# #Converting dictionary into Dataframe.
# coords = pandas.DataFrame(coor_dict)

# #Creatinf a csv file from the generated Dataframe.
# coords.to_csv("F:\Python programs\India state guess game\India_states & UTs.csv")