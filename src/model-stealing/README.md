# Model Stealing Adversarial Attack

The definition of a [Model Stealing](https://github.com/fclesio/pycon-africa-2020-security-ml/tree/master/src/model-stealing) can be defined as: "_The attackers recreate the underlying model by legitimately querying the model. The functionality of the new model is same as that of the underlying model._[1]"

In our example, we're going to use a REST API as a endpoint like any vanilla implementation that we can see in web.

However, I'll expose how a potencial attacker can use queries not only to recreate your model based on each data provided in the queries, but it's possible to catch only some cases (in our Layman's Brothers bank, the unlikely to default status (`DEFAULT=0`)) that can be explored afterwards.

## Steps to generate the example
In our example we'll need to use two terminal tabs. One will be to start the API, and another one to run the queries against the model.

#### Terminal Tab # 1
```bash
$ model-stealing git:(master) ✗ python3.6  api.py
```

#### Terminal Tab # 2
###### Call Testing # 1:

```bash
$ curl -d '[
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
```

###### Call Testing # 2:
```bash
$ curl -d '[
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
```

### Attacks
###### Search # 1: Fixed parameters, changing only the `AGE` feature:

```bash
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
```

###### Search # 2: Fixed parameters, changing only the `AGE` and `SEX` features:
```bash
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
```


###### Search # 3: Fixed parameters, changing only the `AGE`, `SEX_1` and `LIMIT_BAL` features:
```bash
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
```


###### Search # 3: Fixed parameters, changing only the `AGE`, `SEX_1`, `SEX_2`, `PAY_0`, `PAY_2`, and `PAY_3` features:
```bash
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
```


## Countermeasures
- Never open your model to the external world query it
- Monitor sequential requests can help to get those cases
- Restrict the information sent by the API
- Differential Privacy can protect the data and avoid privacy violations if an attack happens [1]
- Ensembling can put an extra layer of difficulty to the attackers since the attackers will only be able to obtain relatively coarse approximations of the target function [1]  

## References
[1] - [Tramèr, Florian, et al. "Stealing Machine Learning Models via Prediction APIs." USENIX Security Symposium. 2016.](https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_tramer.pdf)
