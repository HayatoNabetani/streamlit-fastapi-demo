# おまじない構文
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

# 基盤の定義
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# データベースの一連の流れ
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 継承すべき設定
Base = declarative_base()