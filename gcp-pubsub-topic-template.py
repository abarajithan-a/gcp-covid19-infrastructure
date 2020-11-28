def GenerateConfig(context):
  # Creates a PubSub Topic with the topic name passed in from the YAML file
  resources = [{
      'name': context.env['name'], 
      'type': 'pubsub.v1.topic',
      'properties': {
          'topic': context.env['name']
      }
  }]
  return {'resources': resources}