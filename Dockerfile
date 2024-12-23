# Use Apache Beam Python SDK image as the base
FROM apache/beam_python3.9_sdk:latest

# Set environment variables
ENV FLEX_TEMPLATE_PYTHON_PY_FILE=/pipeline/mongo-to-bigquery.py

# Copy pipeline code, metadata, and requirements into the image
COPY mongo-to-bigquery.py /pipeline/
COPY metadata.json /pipeline/
COPY requirements.txt /pipeline/

# Install required Python dependencies
RUN pip install -r /pipeline/requirements.txt

# Set entrypoint to run the Python script
ENTRYPOINT ["python", "/pipeline/mongo-to-bigquery.py"]
