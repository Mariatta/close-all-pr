"""Automatically close a PR as it opens."""

import gidgethub.routing



router = gidgethub.routing.Router()


@router.register("pull_request", action="opened")
async def close_pr(event, gh, *args, **kwargs):
    data = {'state': 'closed',
            'maintainer_can_modify': True}
    await gh.patch(event.data["pull_request"]["url"], data=data)
    pr_comment = {'body': f"Thanks for the PR @{event.data['user']['login']}. "
                          f"But this repo is not accepting any PRs for now. "
                          f"Closing your PR. "
                          f"Signed, Mariatta's personal GitHub bot 🤖"
                  }
    await gh.post(event.data["pull_request"]["comments_url"], data=pr_comment)