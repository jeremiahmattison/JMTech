class Config:
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://jmtechlogin:jmtechpassword@DESKTOP-91RK47F/jmtech_db?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False