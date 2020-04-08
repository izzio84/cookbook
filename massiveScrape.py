import psycopg2
import os
def db(filename: str):
    try:
        connection = psycopg2.connect(user="spadam",password="spadam",host="localhost",port="5432",database="cookbook")
        cursor = connection.cursor()
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("\nYou are connected to - ", record,"\n")
        cursor.execute("INSERT INTO itwork(work2) VALUES ('"+filename+"')");
        #print("Record inserted successfully")
        #postgres_insert_query = """ INSERT INTO itwork(work) VALUES (%s)"""
        #record_to_insert = ('works!!!')
        #cursor.execute(postgres_insert_query, filename)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    #db("test")
    #os.system('python scrapeImages.py -s "Charlotte Con Ricotta" -o "C:\dev\django\cookbook\media/\/recipe" --limit 1')
    try:
        connection = psycopg2.connect(user="spadam",password="spadam",host="localhost",port="5432",database="cookbook")
        # Create a connection instance for the PostgreSQL and fetch data from the table
        cursor = connection.cursor()
        pg_select = "SELECT * FROM recipes_recipe"

        cursor.execute(pg_select)
        # Execute and print the output
        #print("Selected rows from book table")
        recipe = cursor.fetchall()

        #print("Records of recipe in the table")
        for row in recipe:
            print("name = ", row[1])
            os.system('python scrapeImages.py -s "'+row[1]+'" -o "C:\dev\django\cookbook\media/\/recipe" --limit 1')
           # print("\nid = ", row[0])
            

    except (Exception, psycopg2.Error) as error:
        print("Error selecting data from table book", error)

    # Close the connection to the PostgreSQL database
    finally:
        if (connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is now closed")