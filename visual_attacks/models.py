from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, backref, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///main.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Connection(Base):
    __tablename__ = 'connection'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    source_ip = Column(String)
    destination_port = Column(Integer)


class Credential(Base):
    __tablename__ = 'credential'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    connection_id = Column(Integer, ForeignKey('connection.id'))
    connection = relationship(
        Connection,
        backref=backref('credentials',
                        uselist=True,
                        cascade='delete,all'))


class ShellCommand(Base):
    __tablename__ = 'shell_command'
    id = Column(Integer, primary_key=True)
    command = Column(String)
    connection_id = Column(Integer, ForeignKey('connection.id'))
    connection = relationship(
        Connection,
        backref=backref('shell_commands',
                        uselist=True,
                        cascade='delete,all'))


class HTTPCommand(Base):
    __tablename__ = 'http_command'
    id = Column(Integer, primary_key=True)
    request = Column(String)
    connection_id = Column(Integer, ForeignKey('connection.id'))
    connection = relationship(
        Connection,
        backref=backref('http_commands',
                        uselist=True,
                        cascade='delete,all'))
