from django.core.management.base import BaseCommand, CommandError
from django.db import models
import pandas as pd
import sqlite3



class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--csvpath', type=str, default=False)

    def handle(self, *args, **options):
        dbpath = '/home/sd3416/Final_Project/project/db.sqlite3'
        table_name = 'squirrel_squirrel'
        columns = 'Latitude,Longitude, Unique_Squirrel_ID, Shift,Date, Age, Primary_Fur_Color, Location, Specific_Location, Running, Chasing, Climbing, Eating, Foraging, Other_Activities, Kuks, Quaas, Moans, Tail_flags,Tail_twitches, Approaches, Indifferent, Runs_from'
        datapath = options['csvpath']
        
        df = pd.read_csv(datapath, usecols=[0, 1, 2, 4, 5, 7, 8, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
        df = df[:5]
        conn = sqlite3.connect(dbpath)
        self.csv2sql(conn, df, table_name, columns)
        conn.commit()
        conn.close()
    
    def csv2sql(self, conn, df, table_name, columns):
        df['Date'] = df['Date'].astype('str')
        values = df.values.tolist()
        values = [tuple(_) for _ in values]
        s = ','.join(['?' for _ in df.columns])
        cursor = conn.cursor()
        #print('INSERT INTO {}({}) VALUES ({})'.format(table_name, columns, s))
        cursor.executemany('INSERT INTO {}({}) VALUES ({})'.format(table_name, columns, s), values)


