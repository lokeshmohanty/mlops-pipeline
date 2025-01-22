# ClearML Model Serving and Monitoring

  - Install dependencies
  ```
	pip install -r requirements.txt
  ```

  - Create a serving service controller
  ```
	clearml-serving create --name <model-serving-name>
  ```

  - Train model
  ```
	python train-sklearn.py
  ```

  - Register model
  ```
	clearml-serving --id <service_id> model add \
	                --engine sklearn \
					--endpoint <endpoint-name> \
					--preprocess "preprocess.py" \
					--name <model-name> \
					--project <project-name>
  ```
  
  - Update the environment variables in `example.env`

  - Start the serving and monitoring containers
  ```
    docker compose --env-file example.env up
  ```
  
  - Test the serving container (or visit <http://localhost:8080/docs> to test)
  ```
	curl -X POST "http://localhost:8080/serve/<endpoint-name>" \
	     -H "accept: application/json" \
		 -H "Content-Type: application/json" \
		 -d '{"x0": -8, "x1": -3}'
  ```
  
  - Visit the grafana container for model monitoring at <http://localhost:3000/>

  - Add metrics to prometheus and visualize them in grafana
  ```
	clearml-serving --id <service_id> metrics add \
	                --endpoint <endpoint-name> \
					--variable-scalar \
					x0=0,0.1,0.5,1,10 \
					x1=0,0.1,0.5,1,10 \
					y=0,0.1,0.5,0.75,1
  ```
