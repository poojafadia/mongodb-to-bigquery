import apache_beam as beam 
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.io.external.mongodb import ReadFromMongoDB


class TransformData(beam.DoFn):
    def process(self, element):
        # Perform any transformations if needed
        return [element]


def run():
    # Define pipeline options
    options = PipelineOptions()
    options.view_as(PipelineOptions).save_main_session = True

    # BigQuery table details
    table_spec = 'skilful-asset-442412-i5:sample_mflix.users'

    # MongoDB connection details
    mongodb_uri = "mongodb+srv://appUser:appUser123@cluster0.1zo5e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    mongodb_database = "sample_mflix"
    mongodb_collection = "users"

    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | 'Read from MongoDB' >> ReadFromMongoDB(
                uri=mongodb_uri,
                db_name=mongodb_database,
                coll_name=mongodb_collection
            )
            | 'Transform Data' >> beam.ParDo(TransformData())
            | 'Write to BigQuery' >> WriteToBigQuery(
                table_spec,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )
        )


if __name__ == "__main__":
    run()
