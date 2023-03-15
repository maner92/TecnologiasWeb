from sqlalchemy import create_engine


def connect_to_db(user, pass_, db="test", plugin_db="mysql+mysqldb"):
    string_db = f"mysql+mysqldb://{user}:{pass_}@localhost:3306/{db}"
    engine = create_engine(string_db, echo=True)
    return engine
