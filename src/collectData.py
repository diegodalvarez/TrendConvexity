# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:37:59 2023

@author: Diego
"""

import os
import pandas as pd
import datetime as dt

from blp import blp

class DataCollector():
    
    def __init__(self):
        
        self.end_date = dt.date.today()
        self.start_date = dt.date(year = 1980, month = 1, day = 1)
        
        self.end_date_input  = self.end_date.strftime("%Y%m%d")
        self.start_date_input = self.start_date.strftime("%Y%m%d")
        
        self.parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        self.data_path = os.path.join(self.parent_path, "data")
        
        self.tickers = {
            "Commodities": ["CL", "GC", "C", "HG", "S"],
            "Equities"   : ["ES", "VG", "Z", "NK"],
            "FX"         : ["EUR", "JPY", "GBP", "CHF"],
            "Bonds"      : ["TY", "RX", "G", "JB"]}
        
        self.fut_path = r"C:\Users\Diego\Desktop\app_prod\BBGFuturesManager\data\PXFront"
        self.bbg_path = r"C:\Users\Diego\Desktop\app_prod\BBGData\data"
        
    def _collect_data(self, start_date, end_date, tickers, path):
        
        self.end_date_input  = self.end_date.strftime("%Y%m%d")
        self.start_date_input = self.start_date.strftime("%Y%m%d")
        
        bquery = blp.BlpQuery().start()
        df_tmp = (bquery.bdh(
            securities = tickers,
            fields = ["PX_LAST"],
            start_date = self.start_date_input,
            end_date = self.end_date_input))
        
        df_tmp.to_parquet(path = path, engine = "pyarrow")
        
    def collect_hf_indices(self, start_date = None, end_date = None):
        
        print("Collecting HF Indices")
        
        if start_date != None: self.start_date = start_date
        if end_date != None: self.end_date = end_date
        
        tickers = ["HFRIFWI Index", "BARCBTOP Index", "NEIXCTA Index"]
        out_path = os.path.join(self.data_path, "hf_indices.parquet")
        self._collect_data(start_date = self.start_date, end_date = self.end_date, tickers = tickers, path = out_path)
        
        print("Collected HF Indices")
        
    def collect_spx(self, start_date = None, end_date = None):
        
        print("Collecting SPX related indices")
        if start_date != None: self.start_date = start_date
        if end_date != None: self.end_date = end_date
        
        tickers = ["SPX Index", "ES1 Index"]
        out_path = os.path.join(self.data_path, "spx.parquet")
        self._collect_data(start_date = self.start_date, end_date = self.end_date, tickers = tickers, path = out_path)
        
        print("Collected SPX and SPX Futures")
        
    def collect_futures(self, verbose: bool = False) -> pd.DataFrame:
        
        file_path = os.path.join(self.data_path, "FuturesData.parquet")
        try:
            
            if verbose == True: print("Trying to find the futures data")
            df_out = pd.read_parquet(path = file_path, engine = "pyarrow")
            if verbose == True: print("Found data\n")
            
        except: 
            
            if verbose == True: print("Couldn't find data, now collecting it")
            
            tickers = [
                os.path.join(self.fut_path, item + ".parquet") 
                for key, val in self.tickers.items() 
                if key != "FX" for item in val]
    
            df_out = (pd.read_parquet(
                path = tickers, engine = "pyarrow"))
            
            if verbose == True: print("Saving data\n")
            df_out.to_parquet(path = file_path, engine = "pyarrow")
            
        return df_out
    
    def collect_fx(self, verbose: bool = False) -> pd.DataFrame:
        
        file_path = os.path.join(self.data_path, "FXData.parquet")
        try:
            
            if verbose == True: print("Trying to find FX data")
            df_out = pd.read_parquet(path = file_path, engine = "pyarrow")
            if verbose == True: print("Found data\n")
            
        except:
            
            if verbose == True: print("Couldn't find FX Data, now collecting it")
            tickers = ([
                os.path.join(self.bbg_path, ticker + ".parquet") 
                for ticker in self.tickers["FX"]])
            
            df_out = (pd.read_parquet(
                path = tickers, engine = "pyarrow").
                drop(columns = ["variable"]))
            
            if verbose == True: print("Saving data\n")
            df_out.to_parquet(path = file_path, engine = "pyarrow")
            
        return df_out

def main() -> None: 
    
    data_collector = DataCollector()
    data_collector.collect_hf_indices()
    data_collector.collect_spx()
    data_collector.collect_futures(verbose = True)
    DataCollector().collect_fx(verbose = True)
    
if __name__ == "__main__": main()
    
