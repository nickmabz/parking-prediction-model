import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from . import (
    ValueErrorException,
    ResourceNotFoundException,
    DBConnectionError,
    PermissionNotFoundException,
    RoleNotFoundException,
    AssociationNotFoundException,
    CampaignCategoryNotFoundException
)
from .models import ErrorResponse

logger = logging.getLogger(__name__)


def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(ValueErrorException)
    async def value_error_handler(request: Request, exc: ValueErrorException):
        logger.exception(f"ValueErrorException caught: {exc.message}")
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(error="Value Error", message=exc.message).dict(),
        )

    @app.exception_handler(ResourceNotFoundException)
    async def resource_not_found_handler(request: Request, exc: ResourceNotFoundException):
        logger.exception(f"ResourceNotFoundException caught: {exc.message}")
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(error="Resource Not Found", message=exc.message).dict(),
        )

    @app.exception_handler(DBConnectionError)
    async def db_connection_error_handler(request: Request, exc: DBConnectionError):
        logger.exception(f"DBConnectionError caught: {exc.detail}")
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(error="Database Connection Error", message=exc.detail).dict(),
        )

    @app.exception_handler(PermissionNotFoundException)
    async def permission_not_found_handler(request: Request, exc: PermissionNotFoundException):
        logger.exception(f"PermissionNotFoundException caught: {exc.message}")
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(error="Permission Not Found", message=exc.message).dict(),
        )

    @app.exception_handler(RoleNotFoundException)
    async def role_not_found_handler(request: Request, exc: RoleNotFoundException):
        logger.exception(f"RoleNotFoundException caught: {exc.message}")
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(error="Role Not Found", message=exc.message).dict(),
        )

    @app.exception_handler(AssociationNotFoundException)
    async def association_not_found_handler(request: Request, exc: AssociationNotFoundException):
        logger.exception(f"AssociationNotFoundException caught: {exc.message}")
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(error="Association Not Found", message=exc.message).dict(),
        )

    @app.exception_handler(CampaignCategoryNotFoundException)
    async def campaign_category_not_found_handler(request: Request, exc: CampaignCategoryNotFoundException):
        logger.exception(f"CampaignCategoryNotFoundException caught: {exc.message}")
        return JSONResponse(
            status_code=404,
            content=ErrorResponse(error="Campaign Category Not Found", message=exc.message).dict(),
        )
