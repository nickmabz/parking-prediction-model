from typing import Union


class ValueErrorException(Exception):
    def __init__(self, value_error: str):
        self.message = value_error
        super().__init__(self.message)


class ResourceNotFoundException(Exception):
    def __init__(self, resource_type: str):
        self.message = f"{resource_type} not found."
        super().__init__(self.message)


class DBConnectionError(Exception):
    def __init__(self, detail: str = "Database connection error"):
        self.detail = detail
        super().__init__(self.detail)


class PermissionNotFoundException(Exception):
    def __init__(self, permission_identifier: Union[int, str]):
        self.message = f"Permission with ID/Name {permission_identifier} not found."
        super().__init__(self.message)


class RoleNotFoundException(Exception):
    def __init__(self, role_identifier: Union[int, str]):
        self.message = f"Role with ID/Name {role_identifier} not found."
        super().__init__(self.message)


class AssociationNotFoundException(Exception):
    def __init__(self, role_id: int, permission_id: int):
        self.message = f"No association found between Role with ID {role_id} and Permission with ID {permission_id}."
        super().__init__(self.message)


class OrganizationNotFoundException(Exception):
    def __init__(self, organization_identifier: Union[int, str]):
        self.message = f"Organization with ID/Name {organization_identifier} not found."
        super().__init__(self.message)


class CampaignCategoryNotFoundException(Exception):
    def __init__(self):
        self.message = f"Campaign category does not exist!"
        super().__init__(self.message)
