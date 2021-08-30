#!/bin/bash
CUC_Report_by_Requests_daily_log=$(tail -n 5 /root/CUC_Report_by_Requests/log.txt)
SICNU_Report_Epidemic_daily_log=$(tail -n 14 /root/SICNU_Report_Epidemic/log.txt)
time=$(date "+%Y-%m-%d")
echo $CUC_Report_by_Requests_daily_log
echo $SICNU_Report_Epidemic_daily_log
mail -s "Report from SICNU_Report_Epidemic" xxxxxxx@xx.com -A /root/SICNU_Report_Epidemic/${time}-20200208802.png -A /root/SICNU_Report_Epidemic/${time}-20200204801.png <<< $SICNU_Report_Epidemic_daily_log
mail -s "Report from CUC_Report_by_Requests" xxxxxxx@xx.com <<< $CUC_Report_by_Requests_daily_log
