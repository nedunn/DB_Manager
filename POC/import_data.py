# Create connection to database
def db_conn():
    pass

for stuff in csv:
    # parse parse parse
    db.session.add(SampleInfo(filename=filename,link_id=link_id,date=me_date)) # Add data to first table

    # 
    data = pd.fromCSV(csv)
    db.session.add(Measurements(link_id=link_id,intensity=data.intensity,shift=data.ramanshift) # Add data to second table

