from fastapi import APIRouter

lastfm = APIRouter(
    default="LastFM",
    tags=["LastFM"],
)

@lastfm.get(
    name="LastFM Status",
    path="/api/lastfm/status",
    summary="Get the status of the LastFM API.",
    response_description="The status of the LastFM API."
)
async def lastfm_status():
    """
    Get the status of the LastFM API.
    """

    return {"status": "online"}