USE ODS_CPS_STAGING
GO

UPDATE DAT.TEKS
SET grade_levels = 0
WHERE grade_levels = 'KG';

UPDATE DAT.TEKS
SET grade_levels = 1
WHERE grade_levels = '01';

UPDATE DAT.TEKS
SET grade_levels = 2
WHERE grade_levels = '02';

UPDATE DAT.TEKS
SET grade_levels = 3
WHERE grade_levels = '03';

UPDATE DAT.TEKS
SET grade_levels = 4
WHERE grade_levels = '04';

UPDATE DAT.TEKS
SET grade_levels = 5
WHERE grade_levels = '05';

UPDATE DAT.TEKS
SET grade_levels = 6
WHERE grade_levels = '06';

UPDATE dat.TEKS
SET grade_levels = 7
WHERE grade_levels = '07';

UPDATE dat.TEKS 
SET grade_levels = 8
WHERE grade_levels = '08';

UPDATE dat.TEKS
SET grade_levels = '9, 10, 11, 12'
WHERE grade_levels = '09, 10, 11, 12';

UPDATE dat.TEKS
SET grade_levels = NULL
WHERE grade_levels = '';

SELECT * FROM dat.TEKS