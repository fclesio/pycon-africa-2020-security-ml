curl -d '[
	{"LIMIT_BAL": 100000,
	"AGE": 26,
	"PAY_0": -1,
	"PAY_2": -1,
	"PAY_3": -1,
	"BILL_AMT1": 1370,
	"BILL_AMT2": 4192,
	"PAY_AMT1": 4210,
	"SEX_1": 0,
	"SEX_2": 1}
	]' -H "Content-Type: application/json" \
     -X POST http://localhost:8080/predict && \
    echo -e "\n -> predict OK"



curl -d '[
    {"LIMIT_BAL": 0,
    "AGE": 30,
    "PAY_0": 2,
    "PAY_2": 2,
    "PAY_3": 2,
    "BILL_AMT1": 0,
    "BILL_AMT2": 0,
    "PAY_AMT1": 0,
    "SEX_1": 0,
    "SEX_2": 1}
    ]' -H "Content-Type: application/json" \
 -X POST http://localhost:8080/predict && \
echo -e "\n -> predict OK"  
