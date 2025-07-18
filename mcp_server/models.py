# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:33:17+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    code: Optional[str] = Field(
        None, description='The status code associated with the error detail'
    )
    context: Optional[Dict[str, List[str]]] = Field(
        None,
        description='Context about the error condition',
        examples=[{'missingScopes': ['scope1', 'scope2']}],
    )
    in_: Optional[str] = Field(
        None,
        alias='in',
        description='The name of the field or parameter in which the error was found.',
    )
    message: str = Field(
        ...,
        description='A human readable message describing the error along with remediation steps where appropriate',
    )
    subCategory: Optional[str] = Field(
        None,
        description='A specific category that contains more specific detail about the error',
    )


class LegalBasis(Enum):
    LEGITIMATE_INTEREST_PQL = 'LEGITIMATE_INTEREST_PQL'
    LEGITIMATE_INTEREST_CLIENT = 'LEGITIMATE_INTEREST_CLIENT'
    PERFORMANCE_OF_CONTRACT = 'PERFORMANCE_OF_CONTRACT'
    CONSENT_WITH_NOTICE = 'CONSENT_WITH_NOTICE'
    NON_GDPR = 'NON_GDPR'
    PROCESS_AND_STORE = 'PROCESS_AND_STORE'
    LEGITIMATE_INTEREST_OTHER = 'LEGITIMATE_INTEREST_OTHER'


class SourceOfStatus(Enum):
    PORTAL_WIDE_STATUS = 'PORTAL_WIDE_STATUS'
    BRAND_WIDE_STATUS = 'BRAND_WIDE_STATUS'
    SUBSCRIPTION_STATUS = 'SUBSCRIPTION_STATUS'


class Status(Enum):
    SUBSCRIBED = 'SUBSCRIBED'
    NOT_SUBSCRIBED = 'NOT_SUBSCRIBED'


class PublicSubscriptionStatus(BaseModel):
    brandId: Optional[int] = Field(
        None,
        description='The ID of the brand that the subscription is associated with, if there is one.',
    )
    description: str = Field(..., description='A description of the subscription.')
    id: str = Field(..., description='The ID for the subscription.')
    legalBasis: Optional[LegalBasis] = Field(
        None, description='The legal reason for the current status of the subscription.'
    )
    legalBasisExplanation: Optional[str] = Field(
        None, description='A more detailed explanation to go with the legal basis.'
    )
    name: str = Field(..., description='The name of the subscription.')
    preferenceGroupName: Optional[str] = Field(
        None,
        description='The name of the preferences group that the subscription is associated with.',
    )
    sourceOfStatus: SourceOfStatus = Field(
        ...,
        description='Where the status is determined from e.g. PORTAL_WIDE_STATUS if the contact opted out from the portal.',
    )
    status: Status = Field(..., description='Whether the contact is subscribed.')


class PublicSubscriptionStatusesResponse(BaseModel):
    recipient: str = Field(..., description='Email address of the contact.')
    subscriptionStatuses: List[PublicSubscriptionStatus] = Field(
        ..., description="A list of all of the contact's subscriptions statuses."
    )


class PublicUpdateSubscriptionStatusRequest(BaseModel):
    emailAddress: str = Field(..., description="Contact's email address.")
    legalBasis: Optional[LegalBasis] = Field(
        None,
        description="Legal basis for updating the contact's status (required for GDPR enabled portals).",
    )
    legalBasisExplanation: Optional[str] = Field(
        None,
        description='A more detailed explanation to go with the legal basis (required for GDPR enabled portals).',
    )
    subscriptionId: str = Field(
        ..., description='ID of the subscription being updated for the contact.'
    )


class SubscriptionDefinition(BaseModel):
    communicationMethod: Optional[str] = Field(
        None, description='The method or technology used to contact.'
    )
    createdAt: datetime = Field(
        ..., description='Time at which the definition was created.'
    )
    description: str = Field(..., description='A description of the subscription.')
    id: str = Field(..., description='The ID of the definition.')
    isActive: bool = Field(
        ..., description='Whether the definition is active or archived.'
    )
    isDefault: bool = Field(
        ..., description='A subscription definition created by HubSpot.'
    )
    isInternal: bool = Field(
        ...,
        description='A default description that is used by some HubSpot tools and cannot be edited.',
    )
    name: str = Field(..., description='The name of the subscription.')
    purpose: Optional[str] = Field(
        None,
        description='The purpose of this subscription or the department in your organization that uses it.',
    )
    updatedAt: datetime = Field(
        ..., description='Time at which the definition was last updated.'
    )


class SubscriptionDefinitionsResponse(BaseModel):
    subscriptionDefinitions: List[SubscriptionDefinition] = Field(
        ..., description='A list of all subscription definitions.'
    )


class Error(BaseModel):
    category: str = Field(..., description='The error category')
    context: Optional[Dict[str, List[str]]] = Field(
        None,
        description='Context about the error condition',
        examples=[
            {
                'invalidPropertyName': ['propertyValue'],
                'missingScopes': ['scope1', 'scope2'],
            }
        ],
    )
    correlationId: UUID = Field(
        ...,
        description='A unique identifier for the request. Include this value with any error reports or support tickets',
        examples=['aeb5f871-7f07-4993-9211-075dc63e7cbf'],
    )
    errors: Optional[List[ErrorDetail]] = Field(
        None, description='further information about the error'
    )
    links: Optional[Dict[str, str]] = Field(
        None,
        description='A map of link names to associated URIs containing documentation about the error or recommended remediation steps',
    )
    message: str = Field(
        ...,
        description='A human readable message describing the error along with remediation steps where appropriate',
        examples=['An error occurred'],
    )
    subCategory: Optional[str] = Field(
        None,
        description='A specific category that contains more specific detail about the error',
    )
