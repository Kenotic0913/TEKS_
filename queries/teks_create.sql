USE ODS_CPS

CREATE TABLE DAT.TEKs (
	row_id INT IDENTITY(1,1)
	,tac_chapter BIGINT NULL
	,academic_subject NVARCHAR(100) NULL
	,reporting_category NVARCHAR(MAX) NULL
	,teks_number VARCHAR(50) NULL
	,teks_text NVARCHAR(MAX) NULL
	,grade_levels VARCHAR(100) NULL
	,TEA_last_updated DATE NULL
)

