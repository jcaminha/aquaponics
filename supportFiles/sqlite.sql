CREATE TABLE readings(id INTEGER PRIMARY KEY AUTOINCREMENT, device TEXT, kind TEXT, dataread NUMERIC,timeread TEXT, processed INTEGER)

INSERT INTO  readings(device, kind, dataread, timeread, processed) VALUES ("tank0", "water.level", 90, datetime('now'),0)

DROP TABLE readings

SELECT * from readings