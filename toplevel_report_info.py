import tkinter as tk
from tkinter import ttk

def run(window, b_title, dict_reportinfo):
    tl_report_info = tk.Toplevel(window)
    tl_report_info.title(b_title)
    tl_report_info.geometry("320x300")

    frame1 = tk.Frame(tl_report_info)
    frame1.pack(fill="x", padx=5, pady=5)
    info_no = ttk.Label(frame1, text="報告編碼:")
    info_no.grid(row=0, column=0, sticky="e")
    report_no = ttk.Label(frame1, text=dict_reportinfo["no"])
    report_no.grid(row=0, column=1, sticky="w")
    info_name = ttk.Label(frame1, text="報告名稱:")
    info_name.grid(row=1, column=0, sticky="e")
    report_name = ttk.Label(frame1, text=dict_reportinfo["name"])
    report_name.grid(row=1, column=1, sticky="w")
    info_type = ttk.Label(frame1, text="報告類型:")
    info_type.grid(row=2, column=0, sticky="e")
    report_type = ttk.Label(frame1, text=dict_reportinfo["type"])
    report_type.grid(row=2, column=1, sticky="w")
    info_sample = ttk.Label(frame1, text="樣品類型:")
    info_sample.grid(row=3, column=0, sticky="e")
    frame_sampletype = tk.Frame(frame1)
    frame_sampletype.grid(row=3, column=1)
    # report_title = 
    