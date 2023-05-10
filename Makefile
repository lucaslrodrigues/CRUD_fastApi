run-server:
	@echo "esperando para iniciar uvicorn..."
	sleep 5
	@echo "Done!"
	uvicorn main:app --reload --port 8000 --host 0.0.0.0