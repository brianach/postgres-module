import psycopg2


# connect to chinook database
connection = psycopg2.connect(database="chinook")


# build a cursor object of the database
cursor = connection.cursor()


# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')


# Query 2 - select "Name" from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')


# Query 3 - select "Pearl Jam"" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Pearl Jam"])


# Query 4 - select using "ArtistId" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [118])


# Query 5 - select all records for "Pearl Jam" "Artist Id" from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [118])


# Query 6 - select all records from "Track" table where the composer is "Pearl Jam"
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Pearl Jam"])


# fetch the results (multiple)
results = cursor.fetchall()


# fetch the results (single)
# results = cursor.fetchone()


# close the connection
connection.close()


# print results
for result in results:
    print(result)
