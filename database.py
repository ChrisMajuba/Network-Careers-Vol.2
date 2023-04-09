from sqlalchemy import create_engine,text
import os
def loadjobs():
  jobs = []
  #sqlalchemy is a database toolkit(library) for python
  db_connect_string = os.getenv("database_info")
  ssl = {
     "ca": "/etc/ssl/certs/ca-certificates.crt"
    }
  engine = create_engine(db_connect_string, connect_args={"ssl": ssl})
  
  with engine.connect() as connection:
      result = connection.execute(text("Select *from networkData"))
      for row in result.all():
        jobs.append(dict(row._mapping))
  return jobs