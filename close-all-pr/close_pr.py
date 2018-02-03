"""Automatically close a PR as it opens."""

import gidgethub.routing



router = gidgethub.routing.Router()


@router.register("pull_request", action="opened")
async def close_pr(event, gh, *args, **kwargs):
    print("hello")
    print(event)
