from app import app, cel


@cel.task()
def print_hello():
    #logger = print_hello.get_logger()
    #logger.info("Hello")
    app.logger.info('My task running...')
