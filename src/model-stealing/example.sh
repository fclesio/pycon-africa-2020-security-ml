set -B
for age in {1..100}; do
	echo "Testing Age: $age"
	curl -d '[
	        {"LIMIT_BAL": 0,
	        "AGE": "'"$age"'",
	        "PAY_0": 2,
	        "PAY_2": 2,
	        "PAY_3": 2,
	        "BILL_AMT1": 0,
	        "BILL_AMT2": 0,
	        "PAY_AMT1": 0,
	        "SEX_1": 0,
	        "SEX_2": 1}
	        ]' -H "Content-Type: application/json" \
	     -X POST http://localhost:8080/predict &&
done




set -B
for age in {1..100}; do
	for sex_1 in {0..1}; do
		echo "Testing Age: $age - Sex_1: $sex_1"
		curl -d '[
		        {"LIMIT_BAL": 0,
		        "AGE": "'"$age"'",
		        "PAY_0": 2,
		        "PAY_2": 2,
		        "PAY_3": 2,
		        "BILL_AMT1": 0,
		        "BILL_AMT2": 0,
		        "PAY_AMT1": 0,
		        "SEX_1": "'"$sex_1"'",
		        "SEX_2": 1}
		        ]' -H "Content-Type: application/json" \
		     -X POST http://localhost:8080/predict &&
	done
done



set -B
for age in {20..100}; do
	for sex_1 in {0..1}; do
		for limit in `seq 1000 2000 100000`; do

			echo "Testing Age: $age - Sex_1: $sex_1 - Limit: $limit"
			curl -d '[
			        {"LIMIT_BAL": "'"$limit"'",
			        "AGE": "'"$age"'",
			        "PAY_0": 2,
			        "PAY_2": 2,
			        "PAY_3": 2,
			        "BILL_AMT1": 0,
			        "BILL_AMT2": 0,
			        "PAY_AMT1": 0,
			        "SEX_1": "'"$sex_1"'",
			        "SEX_2": 1}
			        ]' -H "Content-Type: application/json" \
			     -X POST http://localhost:8080/predict &&
		done
	done
done



set -B
for age in {20..100}; do
	for sex_1 in {0..1}; do
		for sex_2 in {0..1}; do
			for pay_0 in {0..1}; do
				for pay_2 in {0..1}; do
					for pay_3 in {0..1}; do

						echo "Testing Age: $age - Sex_1: $sex_1 - Sex_2: $sex_2 - Pay_0: $pay_0 - Pay_2: $pay_2 - Pay_3: $pay_3"
						curl -d '[
						        {"LIMIT_BAL": 3000,
						        "AGE": "'"$age"'",
						        "PAY_0": "'"$pay_0"'",
						        "PAY_2": "'"$pay_2"'",
						        "PAY_3": "'"$pay_3"'",
						        "BILL_AMT1": 0,
						        "BILL_AMT2": 0,
						        "PAY_AMT1": 0,
						        "SEX_1": "'"$sex_1"'",
						        "SEX_2": "'"$sex_2"'"}
						        ]' -H "Content-Type: application/json" \
						     -X POST http://localhost:8080/predict &&

					done
				done
			done
		done
	done
done
