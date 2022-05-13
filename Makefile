PORT ?= 8082
NUM_WORKERS ?= 1
SIMPLE_SETTINGS ?= api.settings.development

run:
	@gunicorn api:app --bind 0.0.0.0:${PORT} --workers ${NUM_WORKERS} --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS=${SIMPLE_SETTINGS}

run-with-parameter:
	@gunicorn api:app --bind 0.0.0.0:${PORT} --workers ${NUM_WORKERS} --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS=${SIMPLE_SETTINGS} -e DEFAULT_REPORT_BACKEND='fake-report'