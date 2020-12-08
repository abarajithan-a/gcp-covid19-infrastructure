def GenerateConfig(context):
  # Create all the table definitions
  resources = [
    {
      'name': 'daily_ingest_covid19_raw',
      'type': 'bigquery.v2.table',
      'properties': {
        'datasetId': context.properties['datasetId'],
        'tableReference': {
          'tableId': 'daily_ingest_covid19_raw'
        },
        'type': 'TABLE',
        'schema': {
          'fields': [
            {'name': 'fips', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'city', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'state', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'country', 'type': 'STRING', 'mode': 'REQUIRED'},
            {'name': 'last_updated', 'type': 'TIMESTAMP', 'mode': 'NULLABLE'},
            {'name': 'lat', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'long', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'confirmed_cases', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'deaths', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'recovered_cases', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'active_cases', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'combined_key', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'incident_rate', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'case_fatality_ratio', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'ingestion_timestamp', 'type': 'TIMESTAMP', 'mode': 'REQUIRED'},
            {'name': 'file_name', 'type': 'STRING', 'mode': 'REQUIRED'}                                                                                                                                                            
          ]
        },
        'timePartitioning': {
          'type': 'DAY',
          'field': 'last_updated'
        },
        'clustering': {
          'fields': ['country', 'state', 'city']        
        }      
      }
    }
  ]
  return {'resources': resources}