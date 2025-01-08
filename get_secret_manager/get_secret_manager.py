import boto3
import os

from logging import getLogger, INFO, Formatter, StreamHandler

logger = getLogger(__name__)

logger.setLevel(INFO)

formatter = Formatter('%(asctime)s - %(levelname)s : %(name)s : %(message)s - %(filename)s: %(lineno)d')

st_handler = StreamHandler()
st_handler.setFormatter(formatter)

logger.addHandler(st_handler)


def get_secret(secret_name: str) -> str:
    """
    AWS Secrets Managerからシークレットを取得
    """
    try:
        client = boto3.client("secretsmanager", region_name=os.getenv("REGION", "ap-northeast-1"))
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        logger.info("Secret retrieved successfully.")
        return get_secret_value_response["SecretString"]
    except client.exceptions.ResourceNotFoundException:
        msg = f"The requested secret {secret_name} was not found."
        logger.info(msg)
        return msg
    except Exception as e:
        logger.error(f"An unknown error occurred: {str(e)}.")
        raise e
