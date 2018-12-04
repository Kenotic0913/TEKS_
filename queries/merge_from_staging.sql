MERGE ODS_CPS.DAT.TEKS AS t
USING ODS_CPS_STAGING.DAT.TEKS AS s
ON t.teks_number = s.teks_number

WHEN MATCHED
	AND t.tac_chapter        != s.tac_chapter
	 OR t.academic_subject   != s.academic_subject
	 OR t.reporting_category != s.reporting_category
	 OR t.teks_number        != s.teks_number
	 OR t.teks_text          != s.teks_text
	 OR t.grade_levels       != s.grade_levels
	 OR t.TEA_last_updated   != s.TEA_last_updated
THEN
	UPDATE SET
		t.tac_chapter         = s.tac_chapter
		,t.academic_subject   = s.academic_subject
		,t.reporting_category = s.reporting_category
		,t.teks_number        = s.teks_number
		,t.teks_text          = s.teks_text
		,t.grade_levels       = s.grade_levels
		,t.TEA_last_updated   = s.TEA_last_updated

WHEN NOT MATCHED THEN
	INSERT (
		tac_chapter
		,academic_subject
		,reporting_category
		,teks_number
		,teks_text
		,grade_levels
		,TEA_last_updated
	) VALUES (
		s.tac_chapter
		,s.academic_subject
		,s.reporting_category
		,s.teks_number
		,s.teks_text
		,s.grade_levels
		,s.TEA_last_updated
	);