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
        columns = ['Latitude', 'Longitude', 'Date','Unique_Squirrel_ID', 'Shift', 'Data', 'Age', 'Primary_Fur_Color', 'Location', 'Specific_Location', 'Running', 'C
hasing', 'Climbing', 'Eating', 'Foraging', 'Other_Activities', 'Kuks', 'Quaaa', 'Moans','Tail_flags', 'Approaches', 'Indifferent', 'Runs_from']
        conn = sqlite3.connect(dbpath)
        outpath = options['csvpath']
        self.sql2csv(conn, table_name, columns, outpath)
        conn.commit()
        conn.close()

    def sql2csv(self, conn, table_name, columns, outpath):

        cursor = conn.cursor()
        cols = ','.join(columns)
        res = cursor.execute("select {} from {}".format(cols,table_name))
        df = pd.DataFrame(columns=columns)
        for row in res:
            new_row = {}
            for idx, col in enumerate(columns):
                new_row[col] = row[idx]
            df = df.append(new_row, ignore_index=True)
        df.to_csv('./out.csv', index=False)

