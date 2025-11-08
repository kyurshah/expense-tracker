"""
SMS API endpoints for the expense tracker application.
Handles SMS parsing and processing for expense extraction.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create router for SMS-related endpoints
router = APIRouter(prefix="/sms", tags=["sms"])


class SMSParseRequest(BaseModel):
    """Request model for SMS parsing."""
    message: str
    sender: Optional[str] = None
    timestamp: Optional[str] = None


class SMSParseResponse(BaseModel):
    """Response model for SMS parsing."""
    success: bool
    message: str
    data: Optional[dict] = None


@router.post("/parse", response_model=SMSParseResponse)
async def parse_sms(request: SMSParseRequest):
    """
    Parse SMS message to extract expense information.
    
    Args:
        request: SMS parsing request containing message and metadata
        
    Returns:
        SMSParseResponse: Parsed expense information or error message
    """
    # TODO: Implement SMS parsing logic
    return SMSParseResponse(
        success=True,
        message="SMS parsing endpoint - not implemented yet",
        data=None
    )
