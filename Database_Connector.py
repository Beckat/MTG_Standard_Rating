from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData
import Env


Environment = Env.Environment()
engine = Environment.get_database_engine()

meta = MetaData(engine)
engine.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
engine.execute("INSERT INTO films (title, director, year) VALUES ('Test', 'Scott Test', '2017')")


print(meta)