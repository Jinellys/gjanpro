import logging

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логирование информации о запросе, тут по умолчанию(before)
        logger.info(f"Request: {request.method} {request.path}")

        # Передача запроса дальше по цепочке middleware
        response = self.get_response(request)

        return response
