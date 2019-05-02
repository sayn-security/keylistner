#!/usr/bin/env python
# coding: utf-8

# In[61]:


from pynput import keyboard
import time
import decimal
import xlsxwriter
import Login as lo
def keylis():
    a = []
    tim = []
    pr = []
    rl = []
    prt = []
    rlt = []
    hold = []
    flight = []
    master = []
    ngram = []
    

    def on_press(key):
        try:
            if key == keyboard.Key.enter:
            # Stop listener
                return False
        
            value = str(key)
            value = value.replace("'", "")
            if value[0] is "K":
                value = value.replace("Key.", "Pressed :\t")
            if value[0] is "u":
                value = value[1:]
                value = "Pressed :\t"+value
            pr.append(value)
            prt.append(decimal.Decimal(time.time()))
            a.append(value)
            tim.append(decimal.Decimal(time.time()))
        except AttributeError:
            if key == keyboard.Key.enter:
            # Stop listener
                return False
        
            value = str(key)
            value = value.replace("Key.", "Pressed :\t")
            pr.append(value)
            prt.append(decimal.Decimal(time.time()))
            a.append(value)
            tim.append(decimal.Decimal(time.time()))
        

    def on_release(key):
        if key == keyboard.Key.enter:
            # Stop listener
            return False
    
        value = str(key)
        value = str(key)
        value = value.replace("'", "")
        if value[0] is "K":
            value = value.replace("Key.", "Released :\t")
        if value[0] is "u":
            value = value[1:]
            value = "Released :\t"+value
        rl.append(value)
        rlt.append(decimal.Decimal(time.time()))
        a.append(value)
        tim.append(decimal.Decimal(time.time()))
    


    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    # ...or, in a non-blocking fashion:
    #listener.start()

    i = 0
    while i < len(prt):
        hold.append(decimal.Decimal(rlt[i]-prt[i]))
        i+=1

    i = 1
    while i < len(prt):
        flight.append(decimal.Decimal(prt[i]-rlt[i-1]))
        i+=1

    i = 0
    while i < len(prt)-3:
        ngram.append(decimal.Decimal(rlt[i+3]-prt[i]))
        i+=1
    tt = []
    tt.append(decimal.Decimal(rlt[len(rlt)-1]-prt[0]))
    bla = []
    bla.append("sub00")
    master = master+bla+hold+flight+ngram+tt

    i = 0
    '''while i < len(master):
        print master[i]
        i+=1
        '''

    wb = xlsxwriter.Workbook("DataCollected.xlsx")
    worksheet = wb.add_worksheet()
    # add_sheet is used to create sheet. 
 
    i = 0
    while i < len(master):
        worksheet.write(0, i, master[i])
        i+=1
    wb.close()
    print ("done")
if __name__ == "__main__":
    work = keylis()
