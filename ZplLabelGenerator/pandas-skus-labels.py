import pandas as pd
import numpy as np

skusDf = pd.read_csv("C:\\Users\\Back-Warehouse\\Documents\\Python\\skuReprints.csv", dtype=object)

notNullDf = skusDf.dropna()


#start label zpl string
zpl_str = "${ ^XA \n\n"
#start the label 50 on the y_axis
y_axis=50

for index, row in notNullDf.iterrows():
      #check y_axis value, if greater than 1500 
      if y_axis>1500:
            #start new label in ZPL string
            y_axis = 50
            zpl_str += "^XZ\n^XA\n\n"


      #add sku to label
      zpl_str += "^CF0,40\n^^FO50,"+str(y_axis)+"^FD" + str(row["Sku"]) + "^FS\n\n"
      #increment y_axis for 100 sku to barcode
      y_axis+=100
      #barcode string
      zpl_str += "^BY4,2,60\n^FO80," + str(y_axis) + "\n^BC^FD"+ str(row["UPC"]) + "^FS\n\n"
      #increment y_axis 100 for barcode to line
      y_axis += 100
      #line string
      zpl_str += "^FO50," + str(y_axis) + "^GB720,1,3^FS\n\n"
      #increment y_axis 50 for line to next item
      y_axis +=50
#end for loop

#end zpl file
zpl_str +="\n\n^XZ}$"
#write the text file to print
label_file = open("sku-upc-labels_results.txt", "w")
label_file.write(zpl_str)
label_file.close()
