SELECT * FROM `statistics` as a INNER JOIN results as b ON  b.stat_id = a.id  WHERE a.id BETWEEN 1 and 50000 

SELECT AVG(time) FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id WHERE a.id BETWEEN 1 and 50000
-- average time ---
-- dataset1 117 miliseconds --
-- dataset2 140 ms --
-- dataset3 159 ms --
SELECT AVG(time) FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id WHERE a.id BETWEEN 1 and 50000
SELECT MAX(time)FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id WHERE a.id BETWEEN 1 and 50000 

SELECT count(time)/50000 FROM `statistics` WHERE id BETWEEN 1 and 50000 and time not between 0.110 and 0.124
-- 13.1% --

-- max time --
-- dataset1 178 miliseconds --
-- dataset2 442 miliseconds --
-- dataset3 579 ms --

SELECT MIN(time)FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id WHERE a.id BETWEEN 1 and 50000

-- min time --
-- dataset1 100 miliseconds --
-- dataset2 120 milisecnods --
-- dataset3 144 milseconds --

SELECT STDDEV(time) FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id WHERE a.id BETWEEN 1 and 50000

-- standard deviation --
-- 7 miliseconds --
-- 13 miliseconds --
-- 7ms --


SELECT * FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id INNER JOIN val_mapping as c ON c.id = a.id   WHERE a.id BETWEEN 1 and 50000

SELECT * FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id INNER JOIN val_mapping as c ON c.id = a.id   WHERE a.id BETWEEN 1 and 50000 and c.val = b.guess_column

SELECT count(a.id)/50000 FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id INNER JOIN val_mapping as c ON c.id = a.id  WHERE a.id BETWEEN 1 and 50000 and c.val = b.guess_column
-- top 5 --
-- dataset1 50.8 % --

SELECT id - 57925 FROM `results`

SELECT id - 57925 FROM `results` WHERE (id-57925)%5=1

SELECT (id - 57925)/5 FROM `results` WHERE (id-57925)%5=0 

SELECT COUNT(a.id) FROM results as a INNER JOIN val_mapping as b on (a.id - 57925)/5 = b.id WHERE a.guess_column = b.val

SELECT count(a.id)/50000 FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id INNER JOIN val_mapping as c ON c.id = a.id WHERE a.id BETWEEN 1 and 50000 and c.val = b.guess_column and (b.id-57925)%5 = 1
-- top 1 ---
-- dataset1 : 27.9 % ---
