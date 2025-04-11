#Dashboard to follow the personal progress in the studies of Artificial Intelligene B.Sc.
##Github as Version Control will be used to track the changes and to have a fallback option in case of issues
###My SQL will be used to store data in a database to ensure availability in case the personal computer crashes

#Establishing connection between mysql and pycharm

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Hochzeit2309",
)

mycursor = mydb.cursor()