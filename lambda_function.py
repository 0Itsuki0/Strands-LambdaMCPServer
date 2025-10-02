import boto3

region = "us-east-1"
logs = boto3.client("logs", region_name=region)

def lambda_handler(event, context):
    # tool descriptions
    """AWS Lambda function to list Cloudwatch logs.

    Args:
        event (dict): The Lambda event object containing parameters for logs to be retrieved.
            Following keys are avaialbe.
            - nextToken: The token for the next set of items to return. (You received this token from a previous call.). String or None.
            - logGroupNamePattern: Specify this to return only log groups that have names that match the string based on a case-sensitive substring search. String or None. If None, will return all logs.

        context (dict): AWS Lambda context object

    Returns:
        dict: Retreived logs
              Success format: {'logGroups': [...], 'nextToken': 'string'}
              Error format: {"error": "Error message"}
    """
    try:
        request_dict = dict()

        nextToken = event.get("nextToken", None)
        if nextToken is not None:
            request_dict["nextToken"] = nextToken

        logGroupNamePattern = event.get("logGroupNamePattern", None)
        if logGroupNamePattern is not None:
            request_dict["logGroupNamePattern"] = logGroupNamePattern

        response = logs.describe_log_groups(
            **request_dict
        )
        return {
            "logGroups": response.get("logGroups"),
            "nextToken": response.get("nextToken")
        }
    except Exception as e:
        return {'error': str(e)}