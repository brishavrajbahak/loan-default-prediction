SELECT count(*)  AS total_rows
FROM analytics.loan_modeling;


SELECT 
	default_flag,
	COUNT(*) AS loan_count,
	ROUND(
		count(*) * 100.0 /
		sum(count(*)) OVER (),
		2
	) AS percentage
FROM analytics.loan_modeling
GROUP BY default_flag
ORDER BY default_flag;

SELECT 
	count(*) FILTER (WHERE loan_amnt IS NULL) AS missing_loan_amnt,
	count(*) FILTER (WHERE annual_inc IS NULL) AS missing_annula_inc,
	count(*) FILTER (WHERE dti IS NULL) AS missing_dti,
	count(*) FILTER (WHERE grade IS NULL) AS missing_grade,
	count(*) FILTER (WHERE default_flag IS NULL) AS missing_target
FROM analytics.loan_modeling;