"""Automatically close a PR as it opens."""

import gidgethub.routing

router = gidgethub.routing.Router()


@router.register("pull_request", action="opened")
@router.register("pull_request", action="reopened")
async def close_pr(event, gh, *args, **kwargs):
    data = {'state': 'closed',
            'maintainer_can_modify': True}
    await gh.patch(event.data["pull_request"]["url"], data=data)
    pr_comment = {'body': f"Thanks for the PR @{event.data['pull_request']['user']['login']}. "
                          f"But this repo is not accepting any PRs for now. "
                          f"From  Mariatta's personal GitHub bot 🤖"
                  }

    async for item in gh.getiter('https://api.github.com/repos/miss-islington/cpython/git/refs/heads'):
        print(item)
    await gh.post(event.data["pull_request"]["comments_url"], data=pr_comment)