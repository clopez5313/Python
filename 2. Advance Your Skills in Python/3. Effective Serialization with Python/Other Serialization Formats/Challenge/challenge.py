"""ETL FROM UFO data in XML into SQLite database"""
import sqlite3
import xml.etree.ElementTree as xml
from dateutil import parser

def etl(xml_file, db_file):
    num_records = 0
    db = sqlite3.connect(db_file)

    # Create the table
    with open('schema.sql') as fp:
        schema_sql = fp.read()
    db.executescript(schema_sql)
    db.commit()

    # Initialize the DB cursor and create the INSERT statement.
    cursor = db.cursor()
    insert = "INSERT INTO sighting (time, lat, lng, shape) values (?, ?, ?, ?)"

    # de-serialize the XML file.
    tree = xml.parse(xml_file)
    root = tree.getroot()

    # Initialize elements that go to the DB.
    time = None
    lat = 0.0
    lng = 0.0
    shape = ""

    # Iterate through the XML and get the sighting records.
    for sightings in root:
        num_records += 1

        for sighting in sightings:
            if (sighting.tag == "time"):
              time = parser.parse(sighting.text)
            elif (sighting.tag == "lat"):
                lat = float(sighting.text)
            elif (sighting.tag == "lng"):
                lng = float(sighting.text)
            else:
                shape = sighting.text
                cursor.execute(insert, (time, lat, lng, shape))

    db.commit()

    # Query the database
    db.row_factory = sqlite3.Row
    query = 'SELECT * FROM sighting'
    for row in cursor.execute(query):
        print(dict(row))

    return num_records


if __name__ == '__main__':
    count = etl('ufo.xml', 'ufo.db')
    print(f'{count} records loaded')
