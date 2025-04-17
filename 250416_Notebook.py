import tkinter as tk
from tkinter import ttk
import toplevel_report_info

# 建立一個 dictionary 裝所有的 report
dict_reports = {}
dict_reportinfo = {"no":"", "name":"", "type":"", "sample":""}

window = tk.Tk()
window.title("Notebook 練習")
window.geometry("480x400")
label_main = ttk.Label(text="測試報告書")
label_main.pack()
nb = ttk.Notebook(window)

frame_add = tk.Frame()
frame_list = tk.Frame()
nb.add(frame_add, text="新增資料")
nb.add(frame_list, text="報告資料")
nb.pack(padx=5, pady=5, fill="x")

# 新增資料頁籤
frame_add_1 = tk.Frame(frame_add)
frame_add_1.pack()
label_no = ttk.Label(frame_add_1, text="報告編號")
label_no.grid(row=0, column=0)
entry_no = ttk.Entry(frame_add_1, width=20)
entry_no.grid(row=0, column=1, pady=2, padx=2)
label_name = ttk.Label(frame_add_1, text="報告名稱")
label_name.grid(row=1, column=0)
entry_name = ttk.Entry(frame_add_1, width=20)
entry_name.grid(row=1, column=1, pady=2)
label_type = ttk.Label(frame_add_1, text="報告類型")
label_type.grid(row=2, column=0)
reporttypeList = ["力學測試","生物相容性","清洗確效","滅菌確效","風險管理","包裝確效","包材生物相容性"]
combobox_type = ttk.Combobox(frame_add_1, value=reporttypeList, width=17, state="readonly")
combobox_type.grid(row=2, column=1, pady=2, padx=2)
label_sample = ttk.Label(frame_add_1, text="樣品類型")
label_sample.grid(row=3, column=0)
a = tk.StringVar()
a.set(combobox_type.get())
label_sample_type = ttk.Label(frame_add_1, textvariable=a)
label_sample_type.grid(row=3, column=1)
def on_combobox_change(event):
    a.set(combobox_type.get())
    sampleType_btn_add(combobox_type.get())

sampleType_materials = ["PEEK", "Ti-6Al-4V"]
sampleType_surface = ["噴砂處理", "微孔製程", "陽極上色"]
sampleType_sterilization = ["Gamma", "EO", "Moist-heat", "non-sterile"]
packageType = ["Tyvek", "紙袋", "PE", "PE/Nylon"]

frame_add_2 = tk.Frame(frame_add) # 放樣品類型按鈕
frame_add_2.pack()
def sampleType_btn_add(reportType): 
    for widget in frame_add_2.winfo_children():
            widget.destroy()   
    match reportType:
        case "力學測試":
            btnAddList = sampleType_materials
        case "生物相容性":
            btnAddList = sampleType_materials + sampleType_surface
        case "清洗確效":
            btnAddList = sampleType_materials + sampleType_surface
        case "滅菌確效":
            btnAddList = sampleType_sterilization
        case "風險管理":
            btnAddList = sampleType_materials + sampleType_surface + sampleType_sterilization
        case "包裝確效":
            btnAddList = packageType + sampleType_sterilization
        case "包材生物相容性":
            btnAddList = packageType + sampleType_sterilization
    btn_i = 0
    for i in btnAddList:
        btn_y = btn_i//5
        btn_x = btn_i%5
        btn_sampletype = ttk.Button(frame_add_2, text=i)
        btn_sampletype.grid(row=btn_y, column=btn_x)
        btn_i+=1
            
combobox_type.bind("<<ComboboxSelected>>", on_combobox_change)

# btn_sampleType

frame_add_3 = tk.Frame(frame_add)
frame_add_3.pack()
    
label_other = ttk.Label(frame_add_3, text="...尚未規劃...")
label_other.grid(row=0, column=0)

def confirm():
    # report_no = entry_no.get() # str
    
    dict_reportinfo["no"] = entry_no.get()
    dict_reportinfo["name"] = entry_name.get()
    dict_reportinfo["type"] = combobox_type.get()
    
    dict_reports.update({entry_no.get():entry_no.get()})
    # 還要收集 sampleType (透過 toggle button)
    def info():
        b_title = btn_title.cget("text")
        toplevel_report_info.run(window, b_title, dict_reportinfo)
    
    # 放入 frame_list
    reportTitle = entry_no.get()+" "+entry_name.get()
    btn_title= ttk.Button(frame_list, text=reportTitle, command=info)
    btn_title.pack(fill="x")
    
button_confirm = ttk.Button(frame_add, text="新增", command=confirm)
button_confirm.pack()

window.mainloop()