from sqlalchemy import create_engine,text

#sqlalchemy is a database toolkit(library) for python
db_connect_string = "mysql+pymysql://x1egxfk3olgi4qean9ds:pscale_pw_25iwqISmwoYQ8OF1qLkkdDtRj0by3Ac2gBCdKcKKams@ap-southeast.connect.psdb.cloud/cybernetwork_website_jobs?charset=utf8mb4"
ssl = {
   "ca": "/etc/ssl/certs/ca-certificates.crt"
  }
engine = create_engine(db_connect_string, connect_args={"ssl": ssl})

joblists   = []
jobs_dicts = []
keys       = []
with engine.connect() as connection:
    result = connection.execute(text("Select *from networkData"))
keys    = result.keys()
joblist = result.all()
print(joblist)
    # for row in result.all():
    #   joblists.append(row)
    #   print(joblists)