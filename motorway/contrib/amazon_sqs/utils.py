import json
from motorway.contrib.amazon_sqs.exceptions import SQSMessageToLarge

SQS_MESSAGE_MAXIMUM_SIZE = 262144  # The maximum is 262,144 bytes (256 KB).
# https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-messages.html


def encode_to_json(value):
    s = json.dumps(value)
    message_size = len(s.encode('utf-8'))
    if message_size > SQS_MESSAGE_MAXIMUM_SIZE:
        raise SQSMessageToLarge('Message size of %sB exceeds the maximum SQS message size of %sB' % (message_size, SQS_MESSAGE_MAXIMUM_SIZE))
    return s
