#!/bin/bash
CUC_Report_by_Requests_daily_log=$(tail -n 5 /root/CUC_Report_by_Requests/log.txt)
SICNU_Report_Epidemic_daily_log=$(tail -n 14 /root/SICNU_Report_Epidemic/log.txt)
time=$(date "+%Y-%m-%d")
if [[ $CUC_Report_by_Requests_daily_log == *'"check_code":0'*"今日健康日报数据提交成功"*'"check_code":0'* ]]
then
	email_subject_CUC="[Success]"
else
	email_subject_CUC="[Failure]"
fi
if [[ $SICNU_Report_Epidemic_daily_log == *'2020xxxxxx-succeed'*'2020xxxxxx-succeed'* ]]
then
	email_subject_SICNU="[Success]"
else
	email_subject_SICNU="[Failure]"
fi
mail -s ${email_subject_SICNU}"SICNU_Report_Epidemic" xxxxxxx@xx.com -A /root/SICNU_Report_Epidemic/${time}-2020xxxxxx.png -A /root/SICNU_Report_Epidemic/${time}-2020xxxxxx.png <<< $SICNU_Report_Epidemic_daily_log
mail -s ${email_subject_CUC}"CUC_Report_by_Requests" xxxxxxxx@xx.com <<< $CUC_Report_by_Requests_daily_log